from .musicMap import MusicMap
from .musicProfile import MusicProfile
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify client object which calls Spotify Web API using spotipy python library
class SpotifyClient:

    # constructor
    def __init__(self, client_id, client_secret):
        # save API keys
        self.__id = client_id
        self.__secret = client_secret

        # authenticate API Keys for API calls
        client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
        self.__sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # method which takes in the name of a searched artist and returns a dictionary of related artists (to the searched one)
    # Each name (key) is paired with a popularity (value) based on Spotify community
    #
    # @param searchString is string given to find artist with
    # @param choice is integer value to represent nth choice of results (starting with 0 as 1st choice)
    # @return dict of related artists and popularity value
    def getRelatedArtist(self, searchString, choice):
        # searches for artist from search results and gets their items/attributes
        results = self.__getSearchResults(searchString)
        #print(results)
        items = results['artists']['items']
        #print("\n\n")
        #print(items)

        # takes nth result
        artist = items[choice]
        
        # calls Spotify API for related artists
        spClient = self.getSpotClient()
        related_artists = spClient.artist_related_artists(artist['id'])
        names = {'name': 'popularity_value'}

        # Adds key/pair values to returning dictionary
        # print names of related artists and popularity valuesp
        print("\nRelated Artists of " + artist['name'] + ": \n")
        for artist in related_artists['artists']:
            names[artist['name']] = artist['popularity']
            print('Name: ', artist['name'],
              '\n\tPopularity Value: ', artist['popularity'])

        return names

    # helper function to get overall search results of given search string
    # could be tweaked to give user options in selecting from search results
    #
    # @param searchString is string given to find artist with
    def __getSearchResults(self, searchString):
        spClient = self.getSpotClient()
        results = spClient.search(q='artist:' + searchString, type='artist')
        return results
        
    # getter method for spotify client field
    def getSpotClient(self):
        return self.__sp

    # creates and initializes/reinitializes music map for spotify client based on search string
    #
    # @param searchString is string given to find artist with
    def createMusicMap(self, searchString):

        # dict to hold music profiles of related artists
        relationGraph = {}

        results = self.__getSearchResults(searchString)
        items = results['artists']['items']

        # takes 1st result
        artist = items[0]

        # get dict of related artists
        spClient = self.getSpotClient()
        related_artists = spClient.artist_related_artists(artist['id'])
        
        # create core profile of searched artist
        coreProfile = MusicProfile(artist['name'], artist['genres'], artist['external_urls']['spotify'], artist['followers']['total'], artist['images'][0]['url'])

        # fill relation graph with MusicProfiles of related artists
        for artist in related_artists['artists']:
            relationGraph[artist['name']] = MusicProfile(artist['name'], artist['genres'], artist['external_urls']['spotify'], artist['followers']['total'], artist['images'][0]['url'])

        # create and return MusicMap object using coreProfile and relationGraph
        map = MusicMap(coreProfile, relationGraph)

        return map

    # returns list of top five results based on the searched artist
    # the results are artists' names which can be used to create music maps of
    # if the searchString does not result in 5 results, then the top 4 or less amount
    # will be included in the list
    #
    # @param searchString is string given to find artist with
    def getTopFiveResults(self, searchString):
        list = []

        # call spotify api for search results based on searchString
        results = self.__getSearchResults(searchString)
        items = results['artists']['items']

        # get top 5 (or less) results and put into list
        for i in range(5):
            if(items[i] is not None):
                list.append(items[i]['name'])

        print(list)

        return list