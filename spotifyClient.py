import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify client object which calls Spotify Web API using spotipy python library
class SpotifyClient:

    # constructor
    def __init__(self, client_id, client_secret):
        # save API keys
        self.id = client_id
        self.secret = client_secret

        # authenticate API Keys for API calls
        client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # method which takes in the name of a searched artist and returns a dictionary of related artists (to the searched one)
    # Each name (key) is paired with a popularity (value) based on Spotify community
    def getRelatedArtist(self, searchString):
        # searches for artist and gets their items/attributes
        results = self.sp.search(q='artist:' + searchString, type='artist')
        items = results['artists']['items']

        # takes first result
        artist = items[0]
        
        # calls Spotify API for related artists
        related_artists = self.sp.artist_related_artists(artist['id'])
        names = {'name': 'popularity_value'}

        # Adds key/pair values to returning dictionary
        # print names of related artists and popularity value
        print("\nRelated Artists of " + artist['name'] + ": \n")
        for artist in related_artists['artists']:
            names[artist['name']] = artist['popularity']
            print('Name: ', artist['name'],
              '\n\tPopularity Value: ', artist['popularity'])

        return names
