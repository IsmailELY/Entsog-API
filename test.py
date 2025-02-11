import json
import requests
from collections import defaultdict

def fetch_data_from_api():
    url = "https://transparency.entsog.eu/api/v1/operationaldatas?limit=5"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Failed to fetch data, status code: {response.status_code}")
        return None

def calculate_kpis(data):
    total_gas_flow = 0
    capacity_data = defaultdict(lambda: {"Firm Booked": 0, "Firm Technical": 0})
    
    for entry in data["operationaldatas"]:
        value = entry.get("value", 0)
        indicator = entry.get("indicator", "")
        point = entry.get("pointLabel", "Unknown Point")
        
        # KPI 1: Total Gas Flow
        total_gas_flow += value
        
        # KPI 2 & 3: Capacity Utilization & Available Capacity
        if indicator == "Firm Booked":
            capacity_data[point]["Firm Booked"] = value
        elif indicator == "Firm Technical":
            capacity_data[point]["Firm Technical"] = value
    
    # Calculate Utilization and Available Capacity
    capacity_kpis = {}
    for point, values in capacity_data.items():
        booked = values["Firm Booked"]
        technical = values["Firm Technical"]
        utilization = (booked / technical * 100) if technical > 0 else 0
        available_capacity = technical - booked
        
        capacity_kpis[point] = {
            "Capacity Utilization (%)": round(utilization, 2),
            "Available Capacity (kWh/d)": available_capacity
        }
    
    return {
        "Total Gas Flow (kWh/d)": total_gas_flow,
        "Capacity KPIs": capacity_kpis
    }

# Fetch data from API and calculate KPIs
data = fetch_data_from_api()
if data:
    kpis = calculate_kpis(data)
    print(json.dumps(kpis, indent=4))
