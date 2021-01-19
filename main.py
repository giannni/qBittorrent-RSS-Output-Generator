import json
from pip._vendor.distlib.compat import raw_input


class rssObject:
    def __init__(self, addPaused, affectedFeeds, assignedCategory, enabled, episodeFilter, ignoreDays,
                 lastMatch, mustContain, mustNotContain, previouslyMatchedEpisodes, savePath, smartFilter,
                 torrentContentLayout, useRegex):
        self.addPaused = addPaused
        self.affectedFeeds = affectedFeeds
        self.assignedCategory = assignedCategory
        self.enabled = enabled
        self.episodeFilter = episodeFilter
        self.ignoreDays = ignoreDays
        self.lastMatch = lastMatch
        self.mustContain = mustContain
        self.mustNotContain = mustNotContain
        self.previouslyMatchedEpisodes = previouslyMatchedEpisodes
        self.savePath = savePath
        self.smartFilter = smartFilter
        self.torrentContentLayout = torrentContentLayout
        self.useRegex = useRegex


def jsonCreation():
    nameOfShow = raw_input("Paste the name of the show: ")
    savePath = raw_input("Paste save path directory: ")
    mustContain = raw_input("Paste what the show must contain to find it: ")
    feeds = ["https://google.com/?page=rss&u="]
    jsonObject = rssObject(None, feeds, "Anime", True, "", 0, "", mustContain, "*720 | *360 | *480 | *540 | *VRV", [],
                             savePath, False, None, False)
    jsonString = json.dumps(jsonObject.__dict__)
    jsonDict = json.loads(jsonString)
    jsonFormatted = json.dumps(jsonDict, indent=4, sort_keys=True)
    print(jsonFormatted)
    ourFile = open("rules.json", "w")
    ourFile.write(f'"{nameOfShow}":')
    ourFile.write(jsonFormatted)
    ourFile.close()


if __name__ == '__main__':
    jsonCreation()
