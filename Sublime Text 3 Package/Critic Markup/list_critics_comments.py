import sublime, sublime_plugin
import re

class ListCriticsCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.markers = []
        self.view.find_all(r'''(?s)((\{>>(.*?)<<\})|(\{==(.*?)==\}\{>>(.*?)<<\}))''', 0, "$1", self.markers)
        self.view.window().show_quick_panel(self.markers, self.goto_critic, sublime.MONOSPACE_FONT)

    def goto_critic(self, choice):
        if choice == -1:
            return
        else:
            findmarker = self.markers[choice]
            #print re.escape(findmarker)
            self.view.sel().clear()

            # re.escape escapes a single quote. That breaks the Sublime find function.
            # Need to substitute escaped single quote with just single quote
            findmarker = findmarker.replace("{", "\{").replace("}", "\}")
            pt = self.view.find(findmarker, 0)
            self.view.sel().add(pt)
            self.view.show(pt)