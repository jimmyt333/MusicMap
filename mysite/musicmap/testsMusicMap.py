from django.test import TestCase
from .spotifyClient import SpotifyClient
import unittest
import json


class TestMusicMap(unittest.TestCase):

    # run each time before
    @classmethod
    def setUpClass(self):
        with open("musicmap/Tokens/credentials.json") as tokens:
            keys = json.load(tokens)

        # connect to Spotify API
        client_id = keys["client_Id"]
        client_secret = keys["client_secret"]

        # create spotifyClient object
        self.spottyClient = SpotifyClient(client_id, client_secret)

    # test core profile of Drake to make sure it matches expected values and isn't empty
    def test_coreProfile(self):
        musicMap = self.spottyClient.createMusicMap("Drake")
        coreProf = musicMap.getCoreProfile()
        self.assertEqual(coreProf.getName(), "Drake",
                         "Core Profile names match")
        self.assertTrue(coreProf.getGenre(), "Genres are present, not empty")
        self.assertTrue(bool(coreProf.getImgURL()),
                        "ImgURL is present, not empty")
        self.assertTrue(bool(coreProf.getURL()), "URL is present, not empty")
        self.assertTrue(
            coreProf.getNumFollowers() > 0,
            "Drake has more than 0 followers on Spotify, not zero",
        )

test = TestMusicMap()
test.setUpClass()
