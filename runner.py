import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import json
from spotifyClient import SpotifyClient

# main runner function
def run():

    # open credentials json and read api keys
    with open('Tokens/credentials.json') as tokens:
        keys = json.load(tokens)

    # connect to Spotify API
    client_id = keys["client_Id"]
    client_secret = keys["client_secret"]

    # create spotifyClient object
    spottyClient = SpotifyClient(client_id, client_secret)

    # use spotify client object to get related artists (dict)
    relatedArtists = spottyClient.getRelatedArtist("Drake")

    # siege_uri = 'spotify:artist:6Cny0Wt5OKLct1rGOLmu80'
    # let user choose artist

    # ids = getTrackIDs('razgrizstern', '5kwI1PlgREZW45n8MQbihz', spottyClient.sp)

    # TEST CODE: print number of IDs
    # print("Number of tracks in playlist: " + str(len(ids)))

    # TEST CODE: print ID of each track
    # print("Track IDs of playlist: \n")
    # print(ids)

    # TEST CODE: loop over track ids

    # tracks = []
    # for i in range(len(ids)):
    #     time.sleep(.5)
    #     track = getTrackFeatures(ids[i], sp)
    #     tracks.append(track)

    # TEST CODE: create dataset

    # df = pd.DataFrame(tracks, columns=['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness',
    #                                   'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
    #df.to_csv("data.csv", sep=',')

    # TEST CODE: get album names

    # siege_uri = 'spotify:artist:6Cny0Wt5OKLct1rGOLmu80'
    # results = sp.artist_albums(siege_uri, album_type='album')
    # albums = results['items']
    # while results['next']:
    #     results = sp.next(results)
    #     albums.extend(results['items'])

    # print("\nArtist's albums: \n")
    # for album in albums:
    #     print(album['name'])

    # TEST CODE: get related artists

    # related_artists = sp.artist_related_artists(siege_uri)
    # print("\nRelated Artists: \n")
    # for artist in related_artists['artists']:
    #     print('Name: ', artist['name'],
    #           '\n\tPopularity Value: ', artist['popularity'])
    #     # print(artist)
    #     #print(' ', artist['popularity'])

# function to retrieve IDs for each track


def getTrackIDs(user, playlist_id, spoti):
    ids = []
    playlist = spoti.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

# function to grab track info based on given ID


def getTrackFeatures(id, spoti):
    meta = spoti.track(id)
    features = spoti.audio_features(id)

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, release_date, length, popularity, danceability, acousticness,
             danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track

# function that returns a single artist given the artist’s ID, URI or URL


def getArtists(artistId, spoti):
    artist = spoti.artist(artistId)
    return artist

# function that returns a single album given the album’s ID, URIs or URL


def getAlbum(albumId, spoti):
    album = spoti.album(albumId)
    return album

# function that returns a single track given the track’s ID, URI or URL


def getTrack(trackId, spoti):
    track = spoti.track(trackId)
    return track

# Get Spotify catalog information about artists similar to an identified artist. Similarity is based on analysis of the Spotify community’s listening history.


def getRelatedArtists(artistId, spoti):
    track = spoti.track(artistId)
    return track


# run as main and first program
if __name__ == '__main__':
    run()
