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
    def __init__(self, addPaused, affectedFeeds, assignedCategory, enabled, episodeFilter, ignoreDays, lastMatch, mustContain, mustNotContain, previouslyMatchedEpisodes, priority, savePath, smartFilter, torrentContentLayout, torrentParams, useRegex):
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
        self.priority = priority
        self.savePath = savePath
        self.smartFilter = smartFilter
        self.torrentContentLayout = torrentContentLayout
        self.torrentParams = torrentParams
        self.useRegex = useRegex
        
class nestedObject:
    def __init__(self, category, download_limit, download_path, inactive_seeding_time_limit, operating_mode, ratio_limit, save_path, seeding_time_limit, share_limit_action, skip_checking, ssl_certificate, ssl_dh_params, ssl_private_key, tags, upload_limit, use_auto_tmm):
        self.category = category
        self.download_limit = download_limit
        self.download_path = download_path
        self.inactive_seeding_time_limit = inactive_seeding_time_limit
        self.operating_mode = operating_mode
        self.ratio_limit = ratio_limit
        self.save_path = save_path
        self.seeding_time_limit = seeding_time_limit
        self.share_limit_action = share_limit_action
        self.skip_checking = skip_checking
        self.ssl_certificate = ssl_certificate
        self.ssl_dh_params = ssl_dh_params
        self.ssl_private_key = ssl_private_key
        self.tags = tags
        self.upload_limit = upload_limit
        self.use_auto_tmm = use_auto_tmm

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
        
         # create nested fiel   d
        jsonObject2 = nestedObject(category, -1, "", -2, "AutoManaged", -2, savePath, -2, "Default", False, "", "", "", [""], -1, False)
        jsonString2 = json.dumps(jsonObject2.__dict__)
        jsonDict2 = json.loads(jsonString2)
        
        # Fill our JSON data object
        # addPaused, affectedFeeds, assignedCategory, enabled, episodeFilter, ignoreDays, lastMatch, mustContain, mustNotContain, previouslyMatchedEpisodes, priority, savePath, smartFilter, torrentContentLayout, torrentParams, useRegex
        jsonObject = rssObject(None, feeds, category, True, "", 0, "", mustContain, "*720 | *360 | *480 | *540 | *VRV", [], 0, savePath, False, None, jsonDict2, False)
        jsonString = json.dumps(jsonObject.__dict__)
        jsonDict = json.loads(jsonString)
        jsonFormatted = json.dumps(jsonDict, indent=4, sort_keys=True)

        if event == 'process':
            # Write out to the file when we process the information
            ourFile = open("rules.json", "a")
            ourFile.write(f'"{nameOfShow}":')
            ourFile.write(jsonFormatted)
            ourFile.close()
