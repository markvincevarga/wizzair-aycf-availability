"""PDF Table Downloader for the WizzAir AYCF Availability table."""

from pathlib import Path

import fetch
import parse


def main():
    url = "https://multipass.wizzair.com/aycf-availability.pdf"
    pdf_dir = Path("pdfs")

    unparsed = fetch.download_current_pdf(url, pdf_dir)

    metadata = parse.get_metadata(unparsed)
    data_generated = metadata[1]
    data = parse.get_data(unparsed)
    parse.add_metadata(data, metadata)

    # Write to file
    data_dir = Path("data")
    data_name = Path(f"{data_generated.isoformat()}.csv")
    data.to_csv(data_dir / data_name, index=False)

    # In case all operations were successful, we reach this point.
    # Mark PDF as parsed, rename to data_generated timestamp
    parsed = pdf_dir / Path(f"{data_generated.isoformat()}.pdf")
    unparsed.rename(parsed)


if __name__ == "__main__":
    main()
