from datetime import datetime
from pathlib import Path

import requests


def download_current_pdf(url: str, pdf_dir: Path) -> Path:
    """Download a pdf from the provided URL,
    name it the current timestamp, and place it in the provided directory.

    Returns: path of the newly created file
    """
    current_time = datetime.now().replace(microsecond=0)
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    pdf_dir.mkdir(exist_ok=True)
    pdf_name = Path(f"{current_time.isoformat()}_unparsed.pdf")
    pdf_path = pdf_dir / pdf_name

    with pdf_path.open("wb") as file:
        file.write(response.content)

    return pdf_path
