import sublime, sublime_plugin
import re

class AcceptCriticCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.options = ['Accept', 'Reject']
        # Need to find scope limits then do regex find within current scope
        self.view.window().show_quick_panel(self.options, self.process_critic, sublime.MONOSPACE_FONT)

    def process_critic(self, choice):
        # Choice 0 is accept
        sels = self.view.sel()
        caret = []
        add_edit = re.compile(r'(?s)\{\+\+(.*?)\+\+[ \t]*(\[(.*?)\])?[ \t]*\}')
        del_edit = re.compile(r'(?s)\{\-\-(.*?)\-\-[ \t]*(\[(.*?)\])?[ \t]*\}')
        sub_edit = re.compile(r'''(?s)\{\~\~(?P<original>(?:[^\~\>]|(?:\~(?!\>)))+)\~\>(?P<new>(?:[^\~\~]|(?:\~(?!\~\})))+)\~\~\}''')
        for sel in sels:
            text = self.view.substr(sel)
            # If something is selected...
            if len(text) > 0:
                a = add_edit.search(text)
                d = del_edit.search(text)
                s = sub_edit.search(text)
                # edit = self.view.begin_edit()
                if choice == 0:
                    if a:
                        # self.view.replace(edit, sel, a.group(1))
                        self.view.run_command("critic_replace", {"a": sel.a, "b": sel.b, "txt": a.group(1)})
                    if d:
                        # self.view.erase(edit, sel)
                        self.view.run_command("critic_erase", {"a": sel.a, "b": sel.b})
                    if s:
                        # self.view.replace(edit, sel, s.group('new'))
                        self.view.run_command("critic_replace", {"a": sel.a, "b": sel.b, "txt": s.group('new')})

                    #if m.group(2)
                    # ... turn the selected text into the link text
                    #view.replace(edit, sel, "[{0}][{1}]".format(text, title))
                # Reject
                elif choice == 1:
                    if a:
                        # self.view.erase(edit, sel)
                        self.view.run_command("critic_erase", {"a": sel.a, "b": sel.b})
                    if d:
                        # self.view.replace(edit, sel, d.group(1))
                        self.view.run_command("critic_replace", {"a": sel.a, "b": sel.b, "txt": d.group(1)})
                    if s:
                        # self.view.replace(edit, sel, s.group('original'))
                        self.view.run_command("critic_replace", {"a": sel.a, "b": sel.b, "txt": s.group('original')})
