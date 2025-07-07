#Spotify Artist Top Track Analysis

This project retrieves the top 10 most popular songs of selected artists using the Spotify Web API. The goal is to analyze various aspects of the artists' musical data such as:

- Artist popularity (based on average song popularity)
- Most-followed artists
- Artists with the longest average song duration
- Visualizations of key insights

The analysis is presented through visualizations using Matplotlib and Seaborn to explore patterns and trends in music data.

---

#Features

- Extracts top 10 tracks per artist from Spotify API
- Collects key metadata: track name, album, popularity, duration, and artist followers
- Cleans and organizes the dataset into CSV format
- Visualizes key insights via bar charts, scatter plots, and regressions

---

#Tech Stack

- Python 3.x
- [Spotipy](https://spotipy.readthedocs.io/) – for accessing Spotify Web API
- Pandas – for data manipulation
- Matplotlib / Seaborn – for data visualization
- dotenv – for environment variable management

---

#Project Structure
Spotify_Project/
├── data/
│ └── artist_top10_track_clean
│ └── artist_top10_track_raw.csv
├── notebook/
│ └── analysis_data.ipynb
│ └── graph.ipynb
│ └── sort_data.ipynb
├── visual/
│ └── \*.png
├── src/
│ └── spotify_api.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

---

#Environment Variables
Create a `.env` file in the root directory with your Spotify API credentials:
dotenv
client_id=your_spotify_client_id
client_secret=your_spotify_client_secret

#How to Run
- Clone this repository
- Set up a virtual environment(optional but recommended)
- Install dependencies by "pip install -r requirements.txt"
- Add your .env file
- Run the script by "python main.py" then open notebook to analysis the data
