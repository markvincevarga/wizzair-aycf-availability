# Flight Analytics

A Streamlit application for analyzing Wizz Air flight data.

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Run the Streamlit app:
```bash
uv run streamlit run app.py
```

## Features

- Average number of daily available flights
- Data collection interval display
- Daily flight counts over time chart
- Extensible structure for additional analytics

## Data Structure

The app expects CSV files in the `data` directory with the following columns:
- `departure_from`: Origin airport
- `departure_to`: Destination airport
- `availability_start`: Flight availability start time
- `availability_end`: Flight availability end time
- `data_generated`: Timestamp when data was generated

CSV files should be named with the format: `YYYY-MM-DDTHH_MM_SS.csv`