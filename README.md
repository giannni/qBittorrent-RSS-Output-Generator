# qBittorrent RSS Output Generator
 Quick script to create a readable json format to input to the RSS autodownloading rules for qBittorrent.
```
Name of show input example: Sword Art Online

Save path input example: C:\Users\Name\Shows\Sword Art Online (Use notepad++ to replace outputted \\)

Must contain input example: Sword Art Online
```

**Output Example:**

```
"Sword Art Online":{
    "addPaused": null,
    "affectedFeeds": [
        "https://google.com/?page=rss&u="
    ],
    "assignedCategory": "Anime",
    "enabled": true,
    "episodeFilter": "",
    "ignoreDays": 0,
    "lastMatch": "",
    "mustContain": "Sword Art Online",
    "mustNotContain": "*720 | *360 | *480 | *540 | *VRV",
    "previouslyMatchedEpisodes": [],
    "savePath": "D:/Downloads/Shows/Sword Art Online",
    "smartFilter": false,
    "torrentContentLayout": null,
    "useRegex": false
}
```
