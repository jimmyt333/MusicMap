class MusicProfile:

    # constructor
    def __init__(self, name, genre, url, numFollowers):
        # save name (String), genre (list of Strings), URL (String), number of followers (int)
        self.__name = name
        self.__genre = genre
        self.__url = url
        self.__numFollowers = numFollowers

    # getter method for music profile name
    def getName(self):
        return self.__name

    # getter method for music profile genre/genres
    def getGenre(self):
        return self.__genre

    # getter method for music profile URL
    def getURL(self):
        return self.__url

    # getter method for music profile number of followers
    def getNumFollowers(self):
        return self.__numFollowers