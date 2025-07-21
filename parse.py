"""Module to parse an AYCF availability PDF."""

from datetime import datetime
from pathlib import Path

import pandas as pd
from camelot.io import read_pdf as parse_pdf


def parse_timestamp(raw: str) -> datetime:
    stripped = raw.replace("(CET)", "").replace("(CEST)", "").strip()
    return datetime.fromisoformat(stripped)


def get_metadata(pdf_path: Path) -> tuple[tuple[datetime, datetime], datetime]:
    headers = parse_pdf(pdf_path, pages="1", flavor="stream")
    # Get time strings
    avail_start_s, avail_end_s = headers[0].df[1][1].split(" - ")
    data_generated_s = headers[0].df[3][1]

    availability_start = parse_timestamp(avail_start_s)
    availability_end = parse_timestamp(avail_end_s)
    data_generated = parse_timestamp(data_generated_s)

    return ((availability_start, availability_end), data_generated)


def get_data(pdf_path: Path) -> pd.DataFrame:
    tables = parse_pdf(pdf_path, pages="all", flavor="lattice")
    dataframes = map(lambda table: table.df[1:], tables)  # remove headers
    df = pd.concat(dataframes)
    df.columns = ["departure_from", "departure_to"]
    df.sort_values(["departure_from", "departure_to"], inplace=True)
    return df


def add_metadata(
    df: pd.DataFrame, metadata: tuple[tuple[datetime, datetime], datetime]
):
    availability_range, data_generated = metadata
    availability_start, availability_end = availability_range

    df["availability_start"] = availability_start.isoformat()
    df["availability_end"] = availability_end.isoformat()
    df["data_generated"] = data_generated.isoformat()
