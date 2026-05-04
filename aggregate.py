#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Aggregate the daily CSV corpus in ./data into a single JSON for the static web app."""

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path


REQUIRED_COLUMNS = ("departure_from", "departure_to")


def parse_collection_date(filename: str) -> str | None:
    stem = Path(filename).stem
    date_str = stem.split("T", 1)[0]
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None
    return date_str


def parse_collection_timestamp(filename: str) -> str | None:
    stem = Path(filename).stem
    date_part, _, time_part = stem.partition("T")
    if not time_part:
        return None
    iso = f"{date_part}T{time_part.replace('_', ':')}"
    try:
        datetime.strptime(iso, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return None
    return iso


def read_csv_routes(path: Path) -> set[tuple[str, str]] | None:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if any(c not in (reader.fieldnames or ()) for c in REQUIRED_COLUMNS):
            return None
        routes: set[tuple[str, str]] = set()
        for row in reader:
            origin = (row.get("departure_from") or "").strip()
            dest = (row.get("departure_to") or "").strip()
            if origin and dest:
                routes.add((origin, dest))
        return routes


def build_aggregated_data(data_dir: Path) -> dict:
    csv_files = sorted(data_dir.glob("*.csv"))
    if not csv_files:
        raise SystemExit(f"no csv files in {data_dir}")

    per_date_routes: dict[str, set[tuple[str, str]]] = {}
    skipped: list[str] = []

    for path in csv_files:
        date = parse_collection_date(path.name)
        if date is None:
            skipped.append(f"{path.name}: bad date in filename")
            continue
        try:
            routes = read_csv_routes(path)
        except (OSError, csv.Error) as e:
            skipped.append(f"{path.name}: {e}")
            continue
        if routes is None:
            skipped.append(f"{path.name}: missing required columns")
            continue
        existing = per_date_routes.setdefault(date, set())
        existing.update(routes)

    if skipped:
        print(f"skipped {len(skipped)} files:", file=sys.stderr)
        for line in skipped:
            print(f"  {line}", file=sys.stderr)

    if not per_date_routes:
        raise SystemExit("no usable data")

    airport_set: set[str] = set()
    route_set: set[tuple[str, str]] = set()
    for routes in per_date_routes.values():
        for origin, dest in routes:
            airport_set.add(origin)
            airport_set.add(dest)
            route_set.add((origin, dest))

    airports = sorted(airport_set)
    airport_idx = {name: i for i, name in enumerate(airports)}

    sorted_routes = sorted(route_set)
    route_idx = {pair: i for i, pair in enumerate(sorted_routes)}
    routes_encoded = [[airport_idx[o], airport_idx[d]] for o, d in sorted_routes]

    availability = {
        date: sorted(route_idx[pair] for pair in per_date_routes[date])
        for date in sorted(per_date_routes)
    }

    latest_ts = next(
        (
            ts
            for ts in (parse_collection_timestamp(p.name) for p in reversed(csv_files))
            if ts
        ),
        None,
    )

    return {
        "generated_at": latest_ts,
        "airports": airports,
        "routes": routes_encoded,
        "availability": availability,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data"),
        help="directory containing daily CSV files (default: ./data)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("aggregated-data.json"),
        help="output JSON path (default: ./aggregated-data.json)",
    )
    args = parser.parse_args()

    data = build_aggregated_data(args.data_dir)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    size_kb = args.out.stat().st_size / 1024
    print(
        f"wrote {args.out} ({size_kb:.1f} KB): "
        f"{len(data['availability'])} days, "
        f"{len(data['airports'])} airports, "
        f"{len(data['routes'])} routes"
    )


if __name__ == "__main__":
    main()
