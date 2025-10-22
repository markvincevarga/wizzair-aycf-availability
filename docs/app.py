import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Airport coordinates dictionary - corrected coordinates for actual airports
AIRPORT_COORDINATES = {
    'Aalesund': (62.5625, 6.1194),
    'Aberdeen': (57.2019, -2.1977),
    'Abu Dhabi': (24.4330, 54.6511),
    'Agadir': (30.3281, -9.4131),
    'Alexandria': (31.1884, 29.9489),
    'Alghero': (40.6322, 8.2908),
    'Alicante': (38.2822, -0.5581),
    'Almaty': (43.3517, 77.0400),
    'Amman': (31.7225, 35.9928),
    'Ancona': (43.6161, 13.3619),
    'Antalya': (36.8986, 30.8008),
    'Asyut': (27.0467, 31.0119),
    'Athens': (37.9364, 23.9475),
    'Bacau': (46.5211, 26.9103),
    'Baku': (40.4675, 50.0467),
    'Banja Luka': (44.9411, 17.2975),
    'Barcelona': (41.2974, 2.0833),
    'Bari': (41.1389, 16.7606),
    'Basel/Mulhouse': (47.5897, 7.5294),
    'Beirut': (33.8206, 35.4883),
    'Belgrade': (44.8184, 20.3092),
    'Bergen': (60.2934, 5.2181),
    'Berlin': (52.3512, 13.4936),
    'Bilbao': (43.3011, -2.9106),
    'Billund': (55.7403, 9.1522),
    'Birmingham': (52.4539, -1.7481),
    'Bishkek': (43.0611, 74.4761),
    'Bologna': (44.5353, 11.2889),
    'Brasov': (45.5950, 25.5156),
    'Bratislava': (48.1703, 17.2128),
    'Brussels': (50.9014, 4.4844),
    'Bucharest': (44.5711, 26.0850),
    'Budapest': (47.4381, 19.2556),
    'Burgas': (42.5697, 27.5153),
    'Castellon': (40.2097, 0.0703),
    'Catania': (37.4669, 15.0664),
    'Chania': (35.5317, 24.1497),
    'Chisinau': (46.9275, 28.9308),
    'Cluj': (46.7853, 23.6864),
    'Comiso': (36.9947, 14.6072),
    'Constanta': (44.3442, 28.4883),
    'Copenhagen': (55.6181, 12.6508),
    'Craiova': (44.3181, 23.8886),
    'Dalaman': (36.7133, 28.7925),
    'Dammam': (26.4711, 49.7978),
    'Debrecen': (47.4889, 21.6153),
    'Dortmund': (51.5178, 7.6122),
    'Dubai': (25.2522, 55.3644),
    'Dubrovnik': (42.5614, 18.2681),
    'Eindhoven': (51.4500, 5.3747),
    'Faro': (37.0144, -7.9658),
    'Frankfurt': (50.0379, 8.5622),
    'Friedrichshafen': (47.6719, 9.5114),
    'Fuerteventura': (28.4528, -13.8639),
    'Gabala': (40.8267, 47.7125),
    'Gdansk': (54.3775, 18.4661),
    'Genoa': (44.4133, 8.8375),
    'Girona': (41.9011, 2.7608),
    'Giza': (30.1203, 30.8067),
    'Glasgow': (55.8719, -4.4331),
    'Gothenburg': (57.6628, 12.2797),
    'Gran Canaria': (27.9319, -15.3867),
    'Gyumri': (40.7500, 43.8514),
    'Hamburg': (53.6304, 10.0067),
    'Haugesund': (59.3453, 5.2081),
    'Heraklion': (35.3387, 25.1803),
    'Hurghada': (27.1783, 33.7994),
    'Iasi': (47.1781, 27.6206),
    'Ibiza': (38.8728, 1.3731),
    'Istanbul': (41.2754, 28.7519),
    'Jeddah': (21.6796, 39.1564),
    'Karlsruhe/Baden-Baden': (48.7794, 8.0806),
    'Katowice': (50.4742, 19.0800),
    'Kaunas': (54.9639, 24.0844),
    'Kerkyra': (39.6017, 19.9119),
    'Kosice': (48.6631, 21.2411),
    'Krakow': (50.0778, 19.7847),
    'Kutaisi': (42.1761, 42.4825),
    'Larnaca': (34.8750, 33.6249),
    'Leeds/Bradford': (53.8658, -1.6603),
    'Leipzig/Halle': (51.4239, 12.2361),
    'Lisbon': (38.7813, -9.1361),
    'Liverpool': (53.3356, -2.8497),
    'Ljubljana': (46.2237, 14.4581),
    'London': (51.4700, -0.4543),
    'Lublin': (51.7225, 23.1714),
    'Lyon': (45.7256, 5.0811),
    'Madeira': (32.6978, -16.7745),
    'Madinah': (24.5536, 39.7050),
    'Madrid': (40.4936, -3.5667),
    'Malaga': (36.6750, -4.4992),
    'Male': (4.1917, 73.5289),
    'Malmo': (55.5361, 13.3675),
    'Malta': (35.8575, 14.4775),
    'Marrakech': (31.6067, -8.0361),
    'Marsa Alam': (25.5572, 34.5836),
    'Memmingen': (47.9881, 10.2394),
    'Milan': (45.6306, 8.7281),
    'Mykonos': (37.4350, 25.3483),
    'Naples': (40.8860, 14.2908),
    'Nice': (43.6653, 7.2150),
    'Nis': (43.3372, 21.8536),
    'Nur-Sultan': (51.0219, 71.4669),
    'Nuremberg': (49.4986, 11.0669),
    'Ohrid': (41.1800, 20.7428),
    'Olbia': (40.8986, 9.5181),
    'Oslo': (60.1939, 11.1003),
    'Palma De Mallorca': (39.5517, 2.7386),
    'Paphos': (34.7181, 32.4856),
    'Paris': (49.0097, 2.5478),
    'Perugia': (43.0956, 12.5133),
    'Pescara': (42.4317, 14.1811),
    'Pisa': (43.6839, 10.3928),
    'Plovdiv': (42.0678, 24.8508),
    'Podgorica': (42.3597, 19.2519),
    'Poprad/Tatry': (49.0736, 20.2406),
    'Porto': (41.2481, -8.6814),
    'Poznan': (52.4214, 16.8269),
    'Prague': (50.1008, 14.2600),
    'Pristina': (42.5728, 21.0361),
    'Radom': (51.3889, 21.2133),
    'Reykjavik': (63.9850, -22.6056),
    'Rhodes': (36.4054, 28.0864),
    'Riga': (56.9236, 23.9711),
    'Rimini': (44.0203, 12.6114),
    'Riyadh': (24.9578, 46.6983),
    'Rome': (41.8003, 12.2389),
    'Rzeszow': (50.1100, 22.0192),
    'Salalah': (17.0386, 54.0914),
    'Salerno': (40.6203, 14.9114),
    'Salzburg': (47.7931, 13.0044),
    'Samarkand': (39.7006, 66.9844),
    'Santorini': (36.3992, 25.4794),
    'Sarajevo': (43.8247, 18.3314),
    'Satu Mare': (47.7031, 22.8856),
    'Sevilla': (37.4181, -5.8931),
    'Sharm el-Sheikh': (27.9772, 34.3947),
    'Sibiu': (45.7856, 24.0914),
    'Skiathos': (39.1769, 23.5036),
    'Skopje': (41.9617, 21.6214),
    'Sofia': (42.6947, 23.4114),
    'Sohag': (26.3428, 31.7428),
    'Split': (43.5389, 16.2981),
    'Stavanger': (58.8767, 5.6378),
    'Stockholm': (59.6519, 17.9186),
    'Stuttgart': (48.6897, 9.2219),
    'Suceava': (47.6875, 26.3544),
    'Szczecin': (53.5847, 14.9019),
    'Tallinn': (59.4133, 24.8328),
    'Targu-Mures': (46.4681, 24.4119),
    'Tashkent': (41.2578, 69.2811),
    'Tel Aviv': (32.0114, 34.8867),
    'Tenerife': (28.0828, -16.5725),
    'Thessaloniki': (40.5197, 22.9706),
    'Timisoara': (45.8103, 21.3378),
    'Tirana': (41.4147, 19.7206),
    'Trieste': (45.8275, 13.4719),
    'Tromso': (69.6833, 18.9189),
    'Trondheim': (63.4578, 10.9242),
    'Turin': (45.2006, 7.6494),
    'Turkistan': (43.2733, 68.3072),
    'Turku': (60.5142, 22.2628),
    'Tuzla': (44.4586, 18.7250),
    'Valencia': (39.4894, -0.4814),
    'Varna': (43.2322, 27.8253),
    'Venice': (45.5053, 12.3519),
    'Verona': (45.3956, 10.8883),
    'Vienna': (48.1103, 16.5697),
    'Vilnius': (54.6342, 25.2858),
    'Warsaw': (52.1658, 20.9675),
    'Wroclaw': (51.1025, 16.8858),
    'Yerevan': (40.1475, 44.3956),
    'Zakinthos Island': (37.7508, 20.8828),
    'Zaragoza': (41.6661, -1.0406)
}

class FlightAnalytics:
    def __init__(self, data_path=None):
        if data_path is None:
            # Try different paths depending on where the script is run from
            possible_paths = [Path("../data"), Path("data"), Path("./data")]
            self.data_path = None
            for path in possible_paths:
                if path.exists() and list(path.glob("*.csv")):
                    self.data_path = path
                    break
            if self.data_path is None:
                self.data_path = Path("../data")  # fallback
        else:
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
                             annotation_text=f"Avg {direction}: {avg_flights:.2f}")
        else:
            avg_flights = self.get_average_daily_flights(hub, destination)
            fig.add_hline(y=avg_flights, line_dash="dash", line_color="red",
                         annotation_text=f"Average: {avg_flights:.2f}")
        
        
        return fig
    
    def create_route_map(self, hub=None, destination=None):
        """Create a route map showing flight routes with optional filtering"""
        filtered_data = self.filter_data(hub, destination)
        if filtered_data.empty:
            return None
        
        airport_dot_size = 15

        # Get total collection days from the original unfiltered data for accurate percentages
        total_collection_days = len(self.data['collection_date'].unique())
        
        # Prepare data for map with flight statistics
        airports_data = []
        
        if hub and not destination:
            # Hub selected: show ONLY hub + destinations reachable from hub
            hub_outbound = filtered_data[filtered_data['departure_from'] == hub]
            hub_inbound = self.data[self.data['departure_to'] == hub]  # Use unfiltered data for inbound
            destinations_from_hub = set(hub_outbound['departure_to'].unique())
            
            # Add hub airport with available destinations
            if hub in AIRPORT_COORDINATES:
                hub_destinations = sorted(set(hub_outbound['departure_to'].unique()))
                coords = AIRPORT_COORDINATES[hub]
                
                # Format destinations for hover text (limit to reasonable length)
                if len(hub_destinations) <= 10:
                    dest_text = ', '.join(hub_destinations)
                else:
                    dest_text = ', '.join(hub_destinations[:10]) + f', ... (+{len(hub_destinations)-10} more)'
                
                airports_data.append({
                    'lat': coords[0],
                    'lon': coords[1],
                    'name': hub,
                    'color': 'red',
                    'size': airport_dot_size,
                    'hover_text': f"{hub} (Hub)<br>Available Destinations: {len(hub_destinations)}<br>{dest_text}"
                })
            
            # Add ONLY destinations reachable from hub (sorted for consistency)
            for dest in sorted(destinations_from_hub):
                if dest in AIRPORT_COORDINATES:
                    # Calculate bidirectional probabilities
                    outbound_flights = hub_outbound[hub_outbound['departure_to'] == dest]
                    inbound_flights = hub_inbound[hub_inbound['departure_from'] == dest]
                    
                    outbound_days = len(outbound_flights['collection_date'].unique()) if len(outbound_flights) > 0 else 0
                    inbound_days = len(inbound_flights['collection_date'].unique()) if len(inbound_flights) > 0 else 0
                    
                    outbound_prob = (outbound_days / total_collection_days * 100) if total_collection_days > 0 else 0
                    inbound_prob = (inbound_days / total_collection_days * 100) if total_collection_days > 0 else 0
                    
                    coords = AIRPORT_COORDINATES[dest]
                    hover_parts = [f"{dest}"]
                    if outbound_prob > 0:
                        hover_parts.append(f"From {hub}: {outbound_prob:.1f}% ({outbound_days}/{total_collection_days} days)")
                    if inbound_prob > 0:
                        hover_parts.append(f"To {hub}: {inbound_prob:.1f}% ({inbound_days}/{total_collection_days} days)")
                    
                    airports_data.append({
                        'lat': coords[0],
                        'lon': coords[1],
                        'name': dest,
                        'color': 'blue',
                        'size': airport_dot_size,
                        'hover_text': "<br>".join(hover_parts)
                    })
                    
        elif destination and not hub:
            # Destination selected: show ONLY destination + origins that fly to destination
            dest_inbound = filtered_data[filtered_data['departure_to'] == destination]
            dest_outbound = self.data[self.data['departure_from'] == destination]  # Use unfiltered data for outbound
            origins_to_dest = set(dest_inbound['departure_from'].unique())
            
            # Add destination airport with available origins
            if destination in AIRPORT_COORDINATES:
                dest_origins = sorted(set(dest_inbound['departure_from'].unique()))
                coords = AIRPORT_COORDINATES[destination]
                
                # Format origins for hover text (limit to reasonable length)
                if len(dest_origins) <= 10:
                    origins_text = ', '.join(dest_origins)
                else:
                    origins_text = ', '.join(dest_origins[:10]) + f', ... (+{len(dest_origins)-10} more)'
                
                airports_data.append({
                    'lat': coords[0],
                    'lon': coords[1],
                    'name': destination,
                    'color': 'green',
                    'size': 15,
                    'hover_text': f"{destination} (Destination)<br>Available Origins: {len(dest_origins)}<br>{origins_text}"
                })
            
            # Add ONLY origins that connect to destination (sorted for consistency)
            for origin in sorted(origins_to_dest):
                if origin in AIRPORT_COORDINATES:
                    # Calculate bidirectional probabilities
                    inbound_flights = dest_inbound[dest_inbound['departure_from'] == origin]
                    outbound_flights = dest_outbound[dest_outbound['departure_to'] == origin]
                    
                    inbound_days = len(inbound_flights['collection_date'].unique()) if len(inbound_flights) > 0 else 0
                    outbound_days = len(outbound_flights['collection_date'].unique()) if len(outbound_flights) > 0 else 0
                    
                    inbound_prob = (inbound_days / total_collection_days * 100) if total_collection_days > 0 else 0
                    outbound_prob = (outbound_days / total_collection_days * 100) if total_collection_days > 0 else 0
                    
                    coords = AIRPORT_COORDINATES[origin]
                    hover_parts = [f"{origin}"]
                    if inbound_prob > 0:
                        hover_parts.append(f"To {destination}: {inbound_prob:.1f}% ({inbound_days}/{total_collection_days} days)")
                    if outbound_prob > 0:
                        hover_parts.append(f"From {destination}: {outbound_prob:.1f}% ({outbound_days}/{total_collection_days} days)")
                    
                    airports_data.append({
                        'lat': coords[0],
                        'lon': coords[1],
                        'name': origin,
                        'color': 'blue',
                        'size': airport_dot_size,
                        'hover_text': "<br>".join(hover_parts)
                    })
                    
        elif hub and destination:
            # Both selected: show just these two airports with bidirectional stats
            if hub in AIRPORT_COORDINATES:
                hub_to_dest = filtered_data[(filtered_data['departure_from'] == hub) & (filtered_data['departure_to'] == destination)]
                dest_to_hub = filtered_data[(filtered_data['departure_from'] == destination) & (filtered_data['departure_to'] == hub)]
                
                coords = AIRPORT_COORDINATES[hub]
                hover_parts = [f"{hub}"]
                if len(hub_to_dest) > 0:
                    hover_parts.append(f"To {destination}: {len(hub_to_dest)} flights")
                if len(dest_to_hub) > 0:
                    hover_parts.append(f"From {destination}: {len(dest_to_hub)} flights")
                
                airports_data.append({
                    'lat': coords[0],
                    'lon': coords[1],
                    'name': hub,
                    'color': 'red',
                    'size': airport_dot_size,
                    'hover_text': "<br>".join(hover_parts)
                })
            
            if destination in AIRPORT_COORDINATES:
                hub_to_dest = filtered_data[(filtered_data['departure_from'] == hub) & (filtered_data['departure_to'] == destination)]
                dest_to_hub = filtered_data[(filtered_data['departure_from'] == destination) & (filtered_data['departure_to'] == hub)]
                
                coords = AIRPORT_COORDINATES[destination]
                hover_parts = [f"{destination}"]
                if len(dest_to_hub) > 0:
                    hover_parts.append(f"To {hub}: {len(dest_to_hub)} flights")
                if len(hub_to_dest) > 0:
                    hover_parts.append(f"From {hub}: {len(hub_to_dest)} flights")
                
                airports_data.append({
                    'lat': coords[0],
                    'lon': coords[1],
                    'name': destination,
                    'color': 'green',
                    'size': airport_dot_size,
                    'hover_text': "<br>".join(hover_parts)
                })
        else:
            # No filters: show all airports with flight data
            routes = filtered_data[['departure_from', 'departure_to']].drop_duplicates()
            all_airports = set(routes['departure_from'].tolist() + routes['departure_to'].tolist())
            
            # Show all airports (no artificial limit) - sorted for consistency
            for airport in sorted(all_airports):
                if airport in AIRPORT_COORDINATES:
                    # Calculate flight availability percentages
                    outbound_flights = filtered_data[filtered_data['departure_from'] == airport]
                    inbound_flights = filtered_data[filtered_data['departure_to'] == airport]
                    
                    outbound_days = len(outbound_flights['collection_date'].unique()) if len(outbound_flights) > 0 else 0
                    inbound_days = len(inbound_flights['collection_date'].unique()) if len(inbound_flights) > 0 else 0
                    
                    outbound_prob = (outbound_days / total_collection_days * 100) if total_collection_days > 0 else 0
                    inbound_prob = (inbound_days / total_collection_days * 100) if total_collection_days > 0 else 0
                    
                    coords = AIRPORT_COORDINATES[airport]
                    hover_parts = [f"{airport}"]
                    if outbound_prob > 0:
                        hover_parts.append(f"Outbound flights: {outbound_prob:.1f}% ({outbound_days}/{total_collection_days} days)")
                    if inbound_prob > 0:
                        hover_parts.append(f"Inbound flights: {inbound_prob:.1f}% ({inbound_days}/{total_collection_days} days)")
                    
                    total_flights = len(outbound_flights) + len(inbound_flights)
                    
                    airports_data.append({
                        'lat': coords[0],
                        'lon': coords[1],
                        'name': airport,
                        'color': 'blue',
                        'size': airport_dot_size,
                        'hover_text': "<br>".join(hover_parts)
                    })
        
        airports_df = pd.DataFrame(airports_data)
        
        if airports_df.empty:
            return None
        
        # Create scatter map with custom hover text using go.Scattermapbox for better control
        import plotly.graph_objects as go
        
        fig = go.Figure()
        
        # Group airports by color for proper rendering
        color_groups = airports_df.groupby('color')
        
        for color, group in color_groups:
            fig.add_trace(go.Scattermap(
                lat=group['lat'],
                lon=group['lon'],
                mode='markers',
                marker=dict(
                    size=group['size'],
                    color=color
                ),
                text=group['hover_text'],
                hovertemplate='%{text}<extra></extra>',
                showlegend=False
            ))
        
        # Update layout for map
        fig.update_layout(
            title=self._get_map_title(hub, destination),
            map=dict(
                style="open-street-map",
                zoom=3,
                center=dict(lat=50, lon=10)
            ),
            height=500,
            margin=dict(l=0, r=0, t=30, b=50)
        )
        
        return fig
    
    def _get_map_title(self, hub, destination):
        """Helper to generate map title"""
        if hub and destination:
            return f'{hub} ↔ {destination}'
        elif hub:
            return f'Routes from {hub}'
        elif destination:
            return f'Routes to {destination}'
        else:
            return 'All Available Routes'
    
    def get_weekday_analysis(self, hub=None, destination=None):
        """Analyze flights by weekday with different logic based on filtering"""
        filtered_data = self.filter_data(hub, destination)
        if filtered_data.empty:
            return pd.DataFrame()
        
        # Add weekday information
        filtered_data = filtered_data.copy()
        filtered_data['weekday'] = filtered_data['collection_date'].dt.day_name()
        filtered_data['weekday_num'] = filtered_data['collection_date'].dt.dayofweek
        
        if hub and destination:
            # For hub+destination: Calculate percentage of days with flights for each direction
            weekday_stats = []
            
            for direction in [f"{hub} → {destination}", f"{destination} → {hub}"]:
                direction_data = filtered_data[filtered_data['direction'] == direction]
                
                for weekday_num, weekday_name in enumerate(['Monday', 'Tuesday', 'Wednesday', 
                                                           'Thursday', 'Friday', 'Saturday', 'Sunday']):
                    # Get all dates for this weekday in the data range
                    all_dates = filtered_data['collection_date'].unique()
                    weekday_dates = [d for d in all_dates if pd.to_datetime(d).dayofweek == weekday_num]
                    total_possible_days = len(weekday_dates)
                    
                    # Count how many of those days had flights
                    days_with_flights = len(direction_data[
                        direction_data['weekday_num'] == weekday_num
                    ]['collection_date'].unique())
                    
                    percentage = (days_with_flights / total_possible_days * 100) if total_possible_days > 0 else 0
                    
                    weekday_stats.append({
                        'weekday': weekday_name,
                        'weekday_num': weekday_num,
                        'direction': direction,
                        'percentage': percentage,
                        'days_with_flights': days_with_flights,
                        'total_days': total_possible_days
                    })
            
            return pd.DataFrame(weekday_stats)
        
        else:
            # For hub-only or no filtering: Calculate average flights per weekday
            weekday_counts = filtered_data.groupby(['collection_date', 'weekday', 'weekday_num']).size().reset_index(name='flight_count')
            weekday_avg = weekday_counts.groupby(['weekday', 'weekday_num'])['flight_count'].mean().reset_index()
            weekday_avg = weekday_avg.sort_values('weekday_num')
            
            return weekday_avg
    
    def create_weekday_chart(self, hub=None, destination=None):
        """Create a chart showing weekday flight analysis"""
        weekday_data = self.get_weekday_analysis(hub, destination)
        if weekday_data.empty:
            return None
        
        if hub and destination:
            # Create percentage chart with bars for each direction
            title = f'Flight Availability by Weekday: {hub} ↔ {destination}'
            fig = px.bar(weekday_data, x='weekday', y='percentage', color='direction',
                        title=title, barmode='group',
                        labels={'weekday': 'Day of Week', 'percentage': 'Percentage of Days with Flights (%)'})
            
            # Sort x-axis by weekday order
            fig.update_xaxes(categoryorder='array', 
                           categoryarray=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
            
            # Add percentage labels on bars
            fig.update_traces(texttemplate='%{y:.2f}%', textposition='outside', hovertemplate='%{x}: %{y:.2f}%<extra></extra>')
            
        else:
            # Create average flights chart
            if hub:
                title = f'Average Flights by Weekday from {hub}'
            elif destination:
                title = f'Average Flights by Weekday to {destination}'
            else:
                title = 'Average Flights by Weekday'
                
            fig = px.bar(weekday_data, x='weekday', y='flight_count',
                        title=title,
                        labels={'weekday': 'Day of Week', 'flight_count': 'Average Number of Flights'})
            
            # Sort x-axis by weekday order
            fig.update_xaxes(categoryorder='array', 
                           categoryarray=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
            
            # Add value labels on bars
            fig.update_traces(texttemplate='%{y:.2f}', textposition='outside', hovertemplate='%{x}: %{y:.2f}<extra></extra>')
        
        # Customize layout
        fig.update_layout(
            xaxis_title="Day of Week",
            showlegend=bool(hub and destination),
            height=400
        )
        
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
        st.metric("Average Daily Flights", f"{avg_flights:.2f}")
    
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
    
    # Weekday analysis chart
    st.markdown("---")
    weekday_chart = analytics.create_weekday_chart(hub, destination)
    if weekday_chart:
        config = {'displayModeBar': True, 'displaylogo': False}
        st.plotly_chart(weekday_chart, config=config, use_container_width=True)
    else:
        st.warning("No weekday data available for the selected filters.")
    
    # Route map
    st.markdown("---")
    st.subheader("🗺️ Airport Map")
    route_map = analytics.create_route_map(hub, destination)
    if route_map:
        config = {'displayModeBar': True, 'displaylogo': False}
        st.plotly_chart(route_map, config=config, use_container_width=True)
        
        # Add legend information
        st.info("🔴 Hub airport | 🟢 Destination airport | 🔵 Other airports")
    else:
        st.warning("No airport data available for the selected filters.")
    
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