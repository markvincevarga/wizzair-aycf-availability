import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

class FlightAnalytics:
    def __init__(self, data_path="../data"):
        self.data_path = Path(data_path)
        self._load_data()
    
    def _load_data(self):
        """Load all CSV files from the data directory"""
        self.data = pd.DataFrame()  # Initialize data attribute
        
        csv_files = list(self.data_path.glob("*.csv"))
        if not csv_files:
            st.error(f"No CSV files found in {self.data_path}")
            return
        
        dfs = []
        for file in csv_files:
            try:
                df = pd.read_csv(file)
                # Extract date from filename
                date_str = file.stem.split('T')[0]
                df['collection_date'] = pd.to_datetime(date_str)
                dfs.append(df)
            except Exception as e:
                st.warning(f"Error loading {file}: {e}")
        
        if dfs:
            self.data = pd.concat(dfs, ignore_index=True)
            self.data['availability_start'] = pd.to_datetime(self.data['availability_start'])
            self.data['availability_end'] = pd.to_datetime(self.data['availability_end'])
            self.data['data_generated'] = pd.to_datetime(self.data['data_generated'])
    
    def get_unique_locations(self):
        """Get unique departure and destination locations"""
        if self.data.empty:
            return [], []
        
        departures = sorted(self.data['departure_from'].unique())
        destinations = sorted(self.data['departure_to'].unique())
        return departures, destinations
    
    def filter_data(self, hub=None, destination=None):
        """Filter data based on hub and/or destination"""
        if self.data.empty:
            return pd.DataFrame()
        
        filtered_data = self.data.copy()
        
        if hub and destination:
            # Show flights both directions: hub->destination and destination->hub
            filtered_data = filtered_data[
                ((filtered_data['departure_from'] == hub) & (filtered_data['departure_to'] == destination)) |
                ((filtered_data['departure_from'] == destination) & (filtered_data['departure_to'] == hub))
            ].copy()
            # Add direction column for separate tracking
            filtered_data['direction'] = filtered_data.apply(
                lambda row: f"{hub} → {destination}" if row['departure_from'] == hub 
                else f"{destination} → {hub}", axis=1
            )
        elif hub:
            # Show all flights from the hub
            filtered_data = filtered_data[filtered_data['departure_from'] == hub].copy()
            filtered_data['direction'] = f"From {hub}"
        elif destination:
            # Show all flights to the destination
            filtered_data = filtered_data[filtered_data['departure_to'] == destination].copy()
            filtered_data['direction'] = f"To {destination}"
        else:
            # No filtering
            filtered_data['direction'] = "All Flights"
        
        return filtered_data
    
    def get_daily_flight_counts(self, hub=None, destination=None):
        """Calculate daily flight counts with optional filtering"""
        filtered_data = self.filter_data(hub, destination)
        if filtered_data.empty:
            return pd.DataFrame()
        
        if hub and destination:
            # Create a complete date range
            all_dates = pd.date_range(
                start=filtered_data['collection_date'].min(),
                end=filtered_data['collection_date'].max(),
                freq='D'
            )
            
            # Get all possible directions
            directions = [f"{hub} → {destination}", f"{destination} → {hub}"]
            
            # Create a complete grid of dates and directions
            date_direction_grid = pd.MultiIndex.from_product(
                [all_dates, directions], 
                names=['collection_date', 'direction']
            ).to_frame(index=False)
            
            # Group actual data by date and direction
            actual_counts = filtered_data.groupby(['collection_date', 'direction']).size().reset_index(name='flight_count')
            
            # Merge with complete grid to include zero counts
            daily_counts = date_direction_grid.merge(
                actual_counts, 
                on=['collection_date', 'direction'], 
                how='left'
            ).fillna(0)
            daily_counts['flight_count'] = daily_counts['flight_count'].astype(int)
        else:
            # Group by date only
            daily_counts = filtered_data.groupby('collection_date').size().reset_index(name='flight_count')
            daily_counts['direction'] = filtered_data['direction'].iloc[0] if not filtered_data.empty else "All Flights"
        
        return daily_counts
    
    def get_average_daily_flights(self, hub=None, destination=None):
        """Calculate average number of daily available flights with optional filtering"""
        daily_counts = self.get_daily_flight_counts(hub, destination)
        if daily_counts.empty:
            return 0
        
        if hub and destination:
            # Return total average across both directions (sum per day, then average)
            daily_totals = daily_counts.groupby('collection_date')['flight_count'].sum()
            return daily_totals.mean()
        else:
            return daily_counts['flight_count'].mean()
    
    def get_data_collection_interval(self, hub=None, destination=None):
        """Get the interval of data collection with optional filtering"""
        filtered_data = self.filter_data(hub, destination)
        if filtered_data.empty:
            return None, None
        
        min_date = filtered_data['collection_date'].min()
        max_date = filtered_data['collection_date'].max()
        return min_date, max_date
    
    def create_daily_flights_chart(self, hub=None, destination=None):
        """Create a chart showing daily flight counts with optional filtering"""
        daily_counts = self.get_daily_flight_counts(hub, destination)
        if daily_counts.empty:
            return None
        
        # Create title based on filters
        if hub and destination:
            title = f'Daily Available Flights: {hub} ↔ {destination}'
            # Create separate lines for each direction
            fig = px.line(daily_counts, x='collection_date', y='flight_count', 
                         color='direction', title=title,
                         labels={'collection_date': 'Date', 'flight_count': 'Number of Flights'})
        elif hub:
            title = f'Daily Available Flights from {hub}'
            fig = px.line(daily_counts, x='collection_date', y='flight_count',
                         title=title,
                         labels={'collection_date': 'Date', 'flight_count': 'Number of Flights'})
        elif destination:
            title = f'Daily Available Flights to {destination}'
            fig = px.line(daily_counts, x='collection_date', y='flight_count',
                         title=title,
                         labels={'collection_date': 'Date', 'flight_count': 'Number of Flights'})
        else:
            title = 'Daily Available Flights Over Time'
            fig = px.line(daily_counts, x='collection_date', y='flight_count',
                         title=title,
                         labels={'collection_date': 'Date', 'flight_count': 'Number of Flights'})
        
        # Add average line(s)
        if hub and destination:
            # Add average lines for each direction
            for direction in daily_counts['direction'].unique():
                direction_data = daily_counts[daily_counts['direction'] == direction]
                avg_flights = direction_data['flight_count'].mean()
                fig.add_hline(y=avg_flights, line_dash="dash",
                             annotation_text=f"Avg {direction}: {avg_flights:.0f}")
        else:
            avg_flights = self.get_average_daily_flights(hub, destination)
            fig.add_hline(y=avg_flights, line_dash="dash", line_color="red",
                         annotation_text=f"Average: {avg_flights:.0f}")
        
        return fig

def main():
    st.set_page_config(
        page_title="Wizz Air Flight Analytics",
        page_icon="✈️",
        layout="wide"
    )
    
    st.title("✈️ Wizz Air Flight Analytics")
    st.markdown("---")
    
    # Initialize analytics
    analytics = FlightAnalytics()
    
    if analytics.data.empty:
        st.error("No data available. Please check the data directory.")
        return
    
    # Get unique locations for selectors
    departures, destinations = analytics.get_unique_locations()
    
    # Filters section
    st.subheader("🔍 Filters")
    col1, col2 = st.columns(2)
    
    with col1:
        selected_hub = st.selectbox(
            "Select Hub (Optional)",
            options=["All"] + departures,
            index=0,
            help="Filter flights departing from this hub"
        )
        hub = None if selected_hub == "All" else selected_hub
    
    with col2:
        selected_destination = st.selectbox(
            "Select Destination (Optional)",
            options=["All"] + destinations,
            index=0,
            help="Filter flights arriving at this destination"
        )
        destination = None if selected_destination == "All" else selected_destination
    
    # Show filter status
    if hub or destination:
        filter_text = []
        if hub and destination:
            filter_text.append(f"Showing flights between **{hub}** and **{destination}** (both directions)")
        elif hub:
            filter_text.append(f"Showing flights from **{hub}**")
        elif destination:
            filter_text.append(f"Showing flights to **{destination}**")
        
        st.info(" • ".join(filter_text))
    
    st.markdown("---")
    
    # Main statistics (filtered)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_flights = analytics.get_average_daily_flights(hub, destination)
        st.metric("Average Daily Flights", f"{avg_flights:.0f}")
    
    with col2:
        start_date, end_date = analytics.get_data_collection_interval(hub, destination)
        if start_date and end_date:
            days = (end_date - start_date).days + 1
            st.metric("Data Collection Period", f"{days} days")
        else:
            st.metric("Data Collection Period", "N/A")
    
    with col3:
        filtered_data = analytics.filter_data(hub, destination)
        total_records = len(filtered_data)
        st.metric("Total Flight Records", f"{total_records:,}")
    
    st.markdown("---")
    
    # Data collection interval
    st.subheader("📅 Data Collection Interval")
    if start_date and end_date:
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Start Date:** {start_date.strftime('%Y-%m-%d')}")
        with col2:
            st.write(f"**End Date:** {end_date.strftime('%Y-%m-%d')}")
    
    st.markdown("---")
    
    # Charts section
    st.subheader("📊 Flight Analytics")
    
    # Daily flights chart (filtered)
    chart = analytics.create_daily_flights_chart(hub, destination)
    if chart:
        config = {'displayModeBar': True, 'displaylogo': False}
        st.plotly_chart(chart, config=config, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")
    
    # Data preview (filtered)
    with st.expander("📋 Data Preview"):
        filtered_data = analytics.filter_data(hub, destination)
        if not filtered_data.empty:
            # Show relevant columns for preview
            preview_cols = ['departure_from', 'departure_to', 'availability_start', 'availability_end', 'collection_date']
            if 'direction' in filtered_data.columns:
                preview_cols.append('direction')
            
            st.dataframe(filtered_data[preview_cols].head(100), width='stretch')
        else:
            st.warning("No data available for the selected filters.")

if __name__ == "__main__":
    main()