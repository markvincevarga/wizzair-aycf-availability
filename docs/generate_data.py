#!/usr/bin/env python3
"""
Data processing script for Wizz Air AYCF visualization.
Processes CSV files and generates JSON data for the web dashboard.
"""

import json
import csv
from datetime import datetime
from pathlib import Path
from collections import defaultdict
import statistics
from typing import Dict, List, Any


def get_date_from_filename(filename: str) -> datetime | None:
    """Extract date from CSV filename."""
    try:
        date_part = filename.split('T')[0]
        return datetime.fromisoformat(date_part)
    except (ValueError, IndexError):
        return None


def get_weekday_name(date: datetime) -> str:
    """Get weekday name from date."""
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return weekdays[date.weekday()]


def process_csv_files(data_dir: Path) -> Dict[str, Any]:
    """Process all CSV files and return aggregated data."""
    weekday_data = defaultdict(list)
    route_counts = defaultdict(int)
    all_files = []
    
    csv_files = list(data_dir.glob("*.csv"))
    print(f"Processing {len(csv_files)} CSV files...")
    
    for csv_file in csv_files:
        date = get_date_from_filename(csv_file.name)
        if not date:
            print(f"Skipping {csv_file.name} - could not parse date")
            continue
            
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                flights = list(reader)
                
            weekday = get_weekday_name(date)
            weekday_data[weekday].append(len(flights))
            all_files.append(csv_file.name)
            
            # Count routes
            for flight in flights:
                departure_from = flight.get('departure_from', '').strip()
                departure_to = flight.get('departure_to', '').strip()
                
                if departure_from and departure_to:
                    # Create normalized route key (alphabetically sorted)
                    route_key = ' - '.join(sorted([departure_from, departure_to]))
                    route_counts[route_key] += 1
                    
        except Exception as e:
            print(f"Error processing {csv_file.name}: {e}")
            continue
    
    return {
        'weekday_data': dict(weekday_data),
        'route_counts': dict(route_counts),
        'processed_files': all_files
    }


def calculate_weekday_stats(weekday_data: Dict[str, List[int]]) -> Dict[str, Any]:
    """Calculate statistics for weekday data."""
    weekday_stats = {}
    
    for day, flights in weekday_data.items():
        if flights:
            avg = statistics.mean(flights)
            std_dev = statistics.stdev(flights) if len(flights) > 1 else 0
            weekday_stats[day] = {
                'average': round(avg),
                'stdDev': std_dev,
                'count': len(flights),
                'flights': flights
            }
        else:
            weekday_stats[day] = {
                'average': 0,
                'stdDev': 0,
                'count': 0,
                'flights': []
            }
    
    return weekday_stats


def calculate_summary_stats(weekday_stats: Dict[str, Any], processed_files: List[str]) -> Dict[str, Any]:
    """Calculate overall summary statistics."""
    total_days = sum(day['count'] for day in weekday_stats.values())
    total_flights = sum(day['average'] * day['count'] for day in weekday_stats.values())
    avg_daily = round(total_flights / total_days) if total_days > 0 else 0
    
    # Get date range
    dates = []
    for filename in processed_files:
        date = get_date_from_filename(filename)
        if date:
            dates.append(date)
    
    dates.sort()
    date_range = f"{dates[0].strftime('%Y-%m-%d')} - {dates[-1].strftime('%Y-%m-%d')}" if dates else "N/A"
    
    return {
        'totalDays': total_days,
        'avgDailyFlights': avg_daily,
        'dateRange': date_range
    }


def prepare_route_data(route_counts: Dict[str, int], top_n: int | None = None) -> List[Dict[str, Any]]:
    """Prepare route data for visualization, returning all routes or top N routes."""
    # Sort routes by count and take all or top N
    sorted_routes = sorted(route_counts.items(), key=lambda x: x[1], reverse=True)
    top_routes = sorted_routes if top_n is None else sorted_routes[:top_n]
    
    route_data = []
    for route_key, count in top_routes:
        cities = route_key.split(' - ')
        if len(cities) == 2:
            route_data.append({
                'cities': cities,
                'count': count,
                'routeKey': route_key
            })
    
    return route_data


def main():
    """Main function to process data and generate JSON files."""
    # Paths
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data"
    output_dir = script_dir
    
    print(f"Processing data from: {data_dir}")
    print(f"Output directory: {output_dir}")
    
    if not data_dir.exists():
        print(f"Data directory not found: {data_dir}")
        return
    
    # Process CSV files
    raw_data = process_csv_files(data_dir)
    
    if not raw_data['processed_files']:
        print("No valid CSV files found to process")
        return
    
    # Calculate statistics
    weekday_stats = calculate_weekday_stats(raw_data['weekday_data'])
    summary_stats = calculate_summary_stats(weekday_stats, raw_data['processed_files'])
    route_data = prepare_route_data(raw_data['route_counts'])  # Use all routes instead of top 50
    
    # Prepare final data structure
    dashboard_data = {
        'generated_at': datetime.now().isoformat(),
        'summary': summary_stats,
        'weekdayStats': weekday_stats,
        'topRoutes': route_data,
        'metadata': {
            'totalFiles': len(raw_data['processed_files']),
            'totalRoutes': len(raw_data['route_counts']),
            'topRoutesShown': len(route_data)
        }
    }
    
    # Write JSON file
    output_file = output_dir / "dashboard_data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated dashboard data: {output_file}")
    print(f"📊 Processed {len(raw_data['processed_files'])} files")
    print(f"📈 {summary_stats['totalDays']} days of data")
    print(f"✈️  {summary_stats['avgDailyFlights']} average daily flights")
    print(f"🗺️  {len(route_data)} top routes included")


if __name__ == "__main__":
    main()