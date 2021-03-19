class MusicMap:

    # constructor
    def __init__(self, coreProfile, relationGraph):
        # save core profile and dict of related artists
        self.__coreProfile = coreProfile
        self.__graph = relationGraph

    # getter method for core profile
    def getCoreProfile(self):
        return self.__coreProfile

    # getter method for dict of related artists
    def getGraph(self):
        return self.__graph