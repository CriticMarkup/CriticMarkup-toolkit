import sublime, sublime_plugin

class MarkCritic(sublime_plugin.TextCommand):
    def run(self, edit):
        self.options = ['Deletion', 'Addition', 'Substitution', 'Comment', "highlight"]
        # Need to find scope limits then do regex find within current scope
        self.view.window().show_quick_panel(self.options, self.process_critic_mark, sublime.MONOSPACE_FONT)

    def process_critic_mark(self, choice):
        # Choice 0 is accept
        sels = self.view.sel()
        edit = self.view.begin_edit()
        for sel in sels:
            text = self.view.substr(sel)
            # Deletion
            if choice == 0:
                self.view.replace(edit, sel, "{--"+text+"--}")
            if choice == 1:
                self.view.replace(edit, sel, "{++"+text+"++}")
            if choice == 2:
                self.view.replace(edit, sel, "{~~"+text+"~>~~}")
                myRegion = self.view.sel()
                oldPos = self.view.sel()[0].end()
                newPos = oldPos - 3
                self.view.sel().clear()
                self.view.sel().add(newPos)
                self.view.show(newPos)
            if choice == 3:
                self.view.replace(edit, sel, "{>>"+text+"<<}")
            if choice == 4:
                self.view.replace(edit, sel, "{=="+text+"==}")

            self.view.end_edit(edit)
            


