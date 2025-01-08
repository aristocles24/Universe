# exoplanet_analysis.py

import requests
import pandas as pd

def fetch_nasa_exoplanet_data():
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps&format=csv"
    response = requests.get(url)
    
    with open("nasa_exoplanets.csv", "wb") as file:
        file.write(response.content)
    
    print("Data fetched and saved as nasa_exoplanets.csv")

def main():
    fetch_nasa_exoplanet_data()
    # Add more functions to categorize exoplanets and leverage AI/ML/RL

if __name__ == "__main__":
    main()
