import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from datetime import datetime
import numpy as np

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
    
    def get_daily_flight_counts(self):
        """Calculate daily flight counts"""
        if self.data.empty:
            return pd.DataFrame()
        
        daily_counts = self.data.groupby('collection_date').size().reset_index(name='flight_count')
        return daily_counts
    
    def get_average_daily_flights(self):
        """Calculate average number of daily available flights"""
        daily_counts = self.get_daily_flight_counts()
        if daily_counts.empty:
            return 0
        return daily_counts['flight_count'].mean()
    
    def get_data_collection_interval(self):
        """Get the interval of data collection"""
        if self.data.empty:
            return None, None
        
        min_date = self.data['collection_date'].min()
        max_date = self.data['collection_date'].max()
        return min_date, max_date
    
    def create_daily_flights_chart(self):
        """Create a chart showing daily flight counts"""
        daily_counts = self.get_daily_flight_counts()
        if daily_counts.empty:
            return None
        
        fig = px.line(daily_counts, x='collection_date', y='flight_count',
                     title='Daily Available Flights Over Time',
                     labels={'collection_date': 'Date', 'flight_count': 'Number of Flights'})
        
        # Add average line
        avg_flights = self.get_average_daily_flights()
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
    
    # Main statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_flights = analytics.get_average_daily_flights()
        st.metric("Average Daily Flights", f"{avg_flights:.0f}")
    
    with col2:
        start_date, end_date = analytics.get_data_collection_interval()
        if start_date and end_date:
            days = (end_date - start_date).days + 1
            st.metric("Data Collection Period", f"{days} days")
        else:
            st.metric("Data Collection Period", "N/A")
    
    with col3:
        total_records = len(analytics.data)
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
    
    # Daily flights chart
    chart = analytics.create_daily_flights_chart()
    if chart:
        config = {'displayModeBar': True, 'displaylogo': False}
        st.plotly_chart(chart, config=config, use_container_width=True)
    
    # Extensible section for future charts
    st.markdown("---")
    st.subheader("🔧 Additional Analytics")
    st.info("This section is ready for additional charts and analysis. Future diagrams can be easily added here.")
    
    # Data preview
    with st.expander("📋 Data Preview"):
        st.dataframe(analytics.data.head(100), width='stretch')

if __name__ == "__main__":
    main()