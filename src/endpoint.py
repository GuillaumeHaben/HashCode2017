class Endpoint():

    def __init__(self, ld, caches):
        # self.ld      = Latence du Data Center vers l'Endpoint
        # caches = Listes des cacheServers connectes a l'Endpoint | format : Map < idCacheServer, Latence >
        self.ld = ld
        self.requests = []
        self.caches = caches

    def sortCaches(self):
        caches.sort(key=lambda tup: tup[1])

    def chooseCache(self, video):
    	# On trie le tableau
    	cachesSorted = self.sortCaches()
    	# On retourne le premier cacheServer : celui avec le ping le plus petit
    	return cachesSorted[0][0]
