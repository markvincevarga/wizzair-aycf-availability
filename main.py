"""PDF Table Downloader for the WizzAir AYCF Availability table."""

import contextlib
import tempfile
from datetime import datetime
from pathlib import Path

import typer

import fetch as fetchlib
import parse as parselib

DEFAULT_AVAILABILITY_URL = "https://multipass.wizzair.com/aycf-availability.pdf"
app = typer.Typer()


@contextlib.contextmanager
def path_or_temp_dir(path: Path | None = None):
    if path is not None:
        yield path
    else:
        with tempfile.TemporaryDirectory() as tmpdir:
            yield tmpdir


def _parse(pdf_path: Path, data_dir: Path) -> tuple[str, datetime]:
    """
    Parse PDF without printing

    Returns:
        (data_file, data_generated_at)
    """
    metadata = parselib.get_metadata(pdf_path)
    data_generated_at = metadata[1]
    data = parselib.get_data(pdf_path)
    parselib.add_metadata(data, metadata)

    # Write to file
    data_name = Path(f"{data_generated_at.isoformat()}.csv")
    data_file = data_dir / data_name
    data.to_csv(data_file, index=False)

    return (data_file, data_generated_at)


@app.command()
def fetch(url: str = DEFAULT_AVAILABILITY_URL, pdf_dir: Path = Path("pdfs")):
    """Fetch today's availability PDF and store it in the given directory"""
    fetched = fetchlib.download_current_pdf(url, Path(pdf_dir))
    print(f"Currently published PDF downloaded and stored in {fetched}")


@app.command()
def parse(pdf_path: Path, data_dir: Path = Path("data")) -> str:
    """Parse the given PDF at `pdf_path`, and store the CSV data in the given `out_dir`"""
    data_file, _ = _parse(pdf_path, data_dir)
    print(f"PDF parsed and data stored in {data_file}")


@app.command()
def fetch_and_parse(
    url: str = DEFAULT_AVAILABILITY_URL,
    pdf_dir: Path | None = None,
    data_dir: Path = Path("data"),
):
    """Fetch today's availability PDF, parse it, and store the parsed data

    If pdf_dir is also defined, the source pdf is retained in the specified directory."""

    with path_or_temp_dir(pdf_dir) as pdf_workdir:
        unparsed = fetchlib.download_current_pdf(url, Path(pdf_workdir))

        data_file, data_generated_at = _parse(unparsed, data_dir)

        # In case all operations were successful, we reach this point.
        # Mark PDF as parsed, rename to data_generated_at timestamp
        parsed = pdf_workdir / Path(f"{data_generated_at.isoformat()}.pdf")
        unparsed.rename(parsed)
        print("Currently published availability PDF fetched and parsed.")
        if pdf_dir is not None:
            print(f"Parsed PDF stored in {parsed}")
        print(f"CSV data stored in {data_file}.")


if __name__ == "__main__":
    app()
