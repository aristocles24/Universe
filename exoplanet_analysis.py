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

# exoplanet_analysis.py

import requests
import pandas as pd

def fetch_nasa_exoplanet_data():
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps&format=csv"
    response = requests.get(url)
    
    with open("nasa_exoplanets.csv", "wb") as file:
        file.write(response.content)
    
    print("Data fetched and saved as nasa_exoplanets.csv")

def categorize_exoplanets():
    df = pd.read_csv("nasa_exoplanets.csv")
    # Example criteria for categorization
    habitable_zone = df[(df['pl_orbper'] > 200) & (df['pl_orbper'] < 400)]
    habitable_zone.to_csv("habitable_exoplanets.csv", index=False)
    print("Categorized exoplanets and saved to habitable_exoplanets.csv")

def main():
    fetch_nasa_exoplanet_data()
    categorize_exoplanets()
    # Add more functions to leverage AI/ML/RL

if __name__ == "__main__":
    main()

# exoplanet_analysis.py

import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def fetch_nasa_exoplanet_data():
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps&format=csv"
    response = requests.get(url)
    
    with open("nasa_exoplanets.csv", "wb") as file:
        file.write(response.content)
    
    print("Data fetched and saved as nasa_exoplanets.csv")

def categorize_exoplanets():
    df = pd.read_csv("nasa_exoplanets.csv")
    habitable_zone = df[(df['pl_orbper'] > 200) & (df['pl_orbper'] < 400)]
    habitable_zone.to_csv("habitable_exoplanets.csv", index=False)
    print("Categorized exoplanets and saved to habitable_exoplanets.csv")

def train_ml_model():
    df = pd.read_csv("habitable_exoplanets.csv")
    features = df[['pl_orbper', 'pl_rade', 'pl_bmasse']]  # Example features
    labels = df['habitable']  # This column needs to be defined based on your criteria

    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    joblib.dump(model, "exoplanet_model.pkl")
    print("Model trained and saved as exoplanet_model.pkl")

def main():
    fetch_nasa_exoplanet_data()
    categorize_exoplanets()
    train_ml_model()

if __name__ == "__main__":
    main()


