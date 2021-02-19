import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import json


def run():

    # open credentials json and read api keys
    with open('Tokens/credentials.json') as tokens:
        keys = json.load(tokens)

    client_id = keys["client_Id"]
    client_secret = keys["client_secret"]

    client_credentials_manager = SpotifyClientCredentials(
        client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    ids = getTrackIDs('razgrizstern', '5kwI1PlgREZW45n8MQbihz', sp)
    print(len(ids))
    print(ids)

    # loop over track ids
    tracks = []
    for i in range(len(ids)):
        time.sleep(.5)
        track = getTrackFeatures(ids[i], sp)
        tracks.append(track)

    # create dataset
    df = pd.DataFrame(tracks, columns=['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness',
                                       'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
    df.to_csv("data.csv", sep=',')


def getTrackIDs(user, playlist_id, spoti):
    ids = []
    playlist = spoti.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids


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


if __name__ == '__main__':
    run()
