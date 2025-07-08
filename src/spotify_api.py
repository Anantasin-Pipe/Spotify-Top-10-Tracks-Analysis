import csv
import spotipy as spy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()  
client_id = os.getenv("client_id")
client_secret = os.getenv('client_secret')

# Create Spotify API client
sp = spy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://127.0.0.1:8000/callback",
    scope="user-top-read"
))

# Search for artist information: name, ID, followers
def search_artist_info(artist_name):
    search_artist_id = sp.search(q=artist_name,type = 'artist') #Search artist by artist_name to find artist id
    artist_list = search_artist_id['artists']['items'] 
    for artist in artist_list:
        name = artist['name']
        if name.lower() == artist_name.strip().lower():
            artist_id = artist['id']
            artist_info = sp.artist(artist_id) #Find artist using artist id
            return artist_info
    print("Artist Not Found")
    return None

# Get top 10 tracks of the artist (by popularity) in the specified country
def search_top_track(artist_id,country = 'TH'):
    artist_top_track = sp.artist_top_tracks(artist_id, country )
    top_track = artist_top_track["tracks"] 
    return top_track

#Write top track data to CSV file 
def write_top_track(top_track, artist_name, follower ,write_header = False, write_mode = 'a'):
    with open('data/artist_top10_track_raw.csv', write_mode, newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        if write_header:
            csv_writer.writerow(['track_rank','album','artist','track_name','popularity','track_in_album', 'duration','follower'])
        sort_top_track = sorted(top_track, key=lambda track: track['popularity'], reverse=True)
        for idx,track in enumerate(sort_top_track):
            rank = idx+1
            albums = track['album']['name']
            song = track['name']
            popularity = track['popularity']
            track_num = track['track_number']
            duration  = track['duration_ms']
            csv_writer.writerow([rank,albums,artist_name,song,popularity,track_num,duration,follower])
        print(f'Write Artist: {artist_name} To CSV File')