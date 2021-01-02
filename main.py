import json
from pip._vendor.distlib.compat import raw_input


class rss_object:
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


def json_creation():
    nameOfShow = raw_input("Paste the name of the show: ")
    savePath = raw_input("Paste save path directory: ")
    mustContain = raw_input("Paste what the show must contain to find it: ")
    feeds = ["https://nyaa.si/?page=rss&u=Judas",
             "https://nyaa.si/?page=rss&u=sff",
             "https://nyaa.si/?page=rss&u=subsplease"]
    json_object = rss_object(None, feeds, "Anime", True, "", 0, "", mustContain, "*720 | *360 | *480 | *540 | *VRV", [],
                             savePath, False, None, False)
    json_string = json.dumps(json_object.__dict__)
    json_dict = json.loads(json_string)
    json_formatted = json.dumps(json_dict, indent=4, sort_keys=True)
    print(json_formatted)
    ourFile = open("rules.json", "w")
    ourFile.write(f'"{nameOfShow}":')
    ourFile.write(json_formatted)
    ourFile.close()


if __name__ == '__main__':
    json_creation()
