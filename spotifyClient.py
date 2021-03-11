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
    #
    # @param searchString is string given to find artist with
    # @param choice is integer value to represent nth choice of results (starting with 0 as 1st choice)
    # @return dict of related artists and popularity value
    def getRelatedArtist(self, searchString, choice):
        # searches for artist from search results and gets their items/attributes
        results = self.getSearchResults(searchString)
        items = results['artists']['items']

        # takes nth result
        artist = items[choice]
        
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

    # helper function to get overall search results of given search string
    # could be tweaked to give user options in selecting from search results
    def getSearchResults(self, searchString):
        results = self.sp.search(q='artist:' + searchString, type='artist')
        return results
