import sublime, sublime_plugin

class MarkCritic(sublime_plugin.TextCommand):
    def run(self, edit):
        self.options = ['Deletion', 'Addition', 'Comment']
        # Need to find scope limits then do regex find within current scope
        self.view.window().show_quick_panel(self.options, self.process_critic_mark, sublime.MONOSPACE_FONT)

    def process_critic_mark(self, choice):
        # Choice 0 is accept
        sels = self.view.sel()
        for sel in sels:
            text = self.view.substr(sel)
            edit = self.view.begin_edit()
            # Deletion
            if choice == 0:
                self.view.replace(edit, sel, "{--"+text+"-- []}")
            if choice == 1:
                self.view.replace(edit, sel, "{++"+text+"++ []}")
            if choice == 2:
                self.view.replace(edit, sel, "{~~"+text+"~~ []}")

            self.view.end_edit(edit)
            


