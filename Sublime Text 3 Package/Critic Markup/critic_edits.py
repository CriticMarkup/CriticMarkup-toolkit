import sublime
import sublime_plugin

class CriticReplaceCommand(sublime_plugin.TextCommand):
    def run(self, edit, a, b, txt):
        sel = sublime.Region(a, b)
        self.view.replace(edit, sel, txt)

class CriticEraseCommand(sublime_plugin.TextCommand):
    def run(self, edit, a, b):
        sel = sublime.Region(a, b)
        self.view.erase(edit, sel)

class CriticReplaceAndMoveCommand(sublime_plugin.TextCommand):
    def run(self, edit, a, b, txt, newPos):
        sel = sublime.Region(a, b)
        self.view.replace(edit, sel, txt)
        self.view.sel().clear()
        self.view.sel().add(newPos)
        self.view.show(newPos)
