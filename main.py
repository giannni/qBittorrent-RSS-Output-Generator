import json
import PySimpleGUI as sg

sg.theme('dark grey 9')

# create layout
layout = [[sg.Text("Name of show")], [sg.Input(key='-NAMEOFSHOW-')],
          [sg.Text("Save Path")], [sg.Input(key='-SAVEPATH-')],
          [sg.Text("Must Contain")], [sg.Input(key='-MUSTCONTAIN-')],
          [sg.Text("Category")], [sg.Input(key='-CATEGORY-')],
          [sg.Button('process'), sg.Button('Quit')]]

# Define Window
window = sg.Window('RSS Feed Generator', layout)


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


if __name__ == '__main__':
    while True:
        # Create our window and read the values
        event, values = window.read()

        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        # Grab our values from GUI
        nameOfShow = values['-NAMEOFSHOW-']
        savePath = values['-SAVEPATH-']
        mustContain = values['-MUSTCONTAIN-']
        category = values['-CATEGORY-']
        feeds = [""]

        # Fill our JSON data object
        jsonObject = rssObject(None, feeds, category, True, "", 0, "", mustContain, "*720 | *360 | *480 | *540 | *VRV",
                               [], savePath, False, None, False)
        jsonString = json.dumps(jsonObject.__dict__)
        jsonDict = json.loads(jsonString)
        jsonFormatted = json.dumps(jsonDict, indent=4, sort_keys=True)

        if event == 'process':
            # Write out to the file when we process the information
            ourFile = open("rules.json", "a")
            ourFile.write(f'"{nameOfShow}":')
            ourFile.write(jsonFormatted)
            ourFile.close()
