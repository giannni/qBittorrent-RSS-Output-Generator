# qBittorrent RSS Output Generator
 Quick script to create a readable json format to input to the RSS autodownloading rules for qBittorrent.
```
Name of show input example: Sword Art Online

Save path input example: C:/Users/Name/Shows/Sword Art Online

Must contain input example: Sword Art Online
```

**Output Example:**

```
"Black Clover":{
    "addPaused": null,
    "affectedFeeds": [
        "https://nyaa.si/?page=rss&u=Judas",
        "https://nyaa.si/?page=rss&u=sff",
        "https://nyaa.si/?page=rss&u=subsplease"
    ],
    "assignedCategory": "Anime",
    "enabled": true,
    "episodeFilter": "",
    "ignoreDays": 0,
    "lastMatch": "",
    "mustContain": "Black Clover",
    "mustNotContain": "*720 | *360 | *480 | *540 | *VRV",
    "previouslyMatchedEpisodes": [],
    "savePath": "D:/Downloads/Anime Shows/Ongoing/Watching/Black Clover",
    "smartFilter": false,
    "torrentContentLayout": null,
    "useRegex": false
}
```
