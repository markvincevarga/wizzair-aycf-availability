"""PDF Table Downloader for the WizzAir AYCF Availability table."""

# %%
from datetime import datetime
from pathlib import Path

import camelot
import pandas as pd
import requests

# %%
time_mark = datetime.now().replace(microsecond=0).isoformat()
time_mark

# %%
url = "https://multipass.wizzair.com/aycf-availability.pdf"
response = requests.get(url, timeout=10)
response.raise_for_status()

pdf_dir = Path("pdfs")
pdf_dir.mkdir(exist_ok=True)
pdf_name = Path(f"{time_mark}_unparsed.pdf")
pdf_path = pdf_dir / pdf_name
with pdf_path.open("wb") as file:
    file.write(response.content)

# %%
# Extract metadata
headers = camelot.read_pdf(pdf_dir / pdf_name, pages="1", flavor="stream")

# %%
# Get time strings
departure_period_s = headers[0].df[1][1]
data_generated_s = headers[0].df[3][1]

# Parse into datetime objects
availability_start, availability_end = map(
    datetime.fromisoformat, departure_period_s[:-6].split(" - ")
)
data_generated = datetime.fromisoformat(data_generated_s[:-6])

# %%
# Parse actual data
tables = camelot.read_pdf(pdf_dir / pdf_name, pages="all", flavor="lattice")

# %%
dataframes = map(lambda table: table.df[1:], tables)  # remove headers
df = pd.concat(dataframes)
df.columns = ["departure_from", "departure_to"]

# %%
# Add constants
df["availability_start"] = availability_start
df["availability_end"] = availability_end
df["data_generated"] = data_generated

# %%
# Write to file
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
data_name = Path(f"{data_generated.isoformat()}.csv")
data_path = data_dir / data_name
df.to_csv(data_path, index=False)

# %%
# Rename original PDF
# To make the operation idempotent until a new PDF is generated, rename the original pdf to the
# parsed date, so that it would simply get overwritten in case a new pdf was found.
# This doesn't run in case of an error anywhere above, leaving a PDF postfixed with _unparsed
parsed_pdf_name = Path(f"{data_generated.isoformat()}.pdf")
parsed_pdf_path = pdf_dir / parsed_pdf_name
pdf_path.rename(parsed_pdf_path)
