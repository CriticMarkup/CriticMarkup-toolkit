# BBEdit Find Next/Previous CriticMarkup Scripts

These scripts provide a way to move between CriticMarkup marks in a file in BBEdit.

You can put these scripts in the `Scripts` folder of your BBEdit configuration folder (`~/Library/Application Support/BBEdit/Scripts` unless you've moved your configuration directory to Dropbox). Once you've placed them there, you'll find them in the BBEdit Scripts menu.

 Each selects the entire mark and the text it contains. This behavior can be changed by opening the scripts in an AppleScript editor and removing "with selecting match" from the end of the find command.

If the end of the file is reached and no mark is found, the scripts wrap around. This behavior can be changed by opening the scripts in an AppleScript editor and changing "wrap around:true" to "wrap around:false".

You can also assign keyboard shortcuts to each of the scripts:

- Open BBEdit's preferences
- Click the "Menus & Shortcuts" entry
- Click the "Scripts" item
- Doubleclick the greyed out "none" next to each script and enter a keyboard shortcut.

The "control" combinations are largely unused in BBEdit (with the exception of control-s, which is used for progressive search).

Finally, you can make the scripts appear at the top of the BBEdit scripts menu by appending `00)` to the beginning of the filename for each.
