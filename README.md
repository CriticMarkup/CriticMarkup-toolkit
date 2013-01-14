![CriticMarkup](http://high90.com/img/CriticMarkup-400px.png)

Welcome to the CriticMarkup Toolkit
====================

The toolkit includes various code snippets and scripts to help you use CriticMarkup in your daily workflow.

For more information about the CriticMarkup syntax, visit the CriticMarkup website at [http://criticmarkup.com](http://criticmarkup.com) or check out our [Github Wiki](https://github.com/CriticMarkup/CriticMarkup-toolkit/wiki).

While Critic Markup can be used with any text editor on any device, we have created several convenient tools to make working with Critic easy and helpful. All the tools listed below assume adherence with the Critic standards outlined above. Deviation from the documented standards will render the tools below non-functional.

#### Marked Processors and CSS ####

There are a couple of processor scripts for use with Brett Terpstra's excellent Marked.app for Mac. If you are using Marked 1.5 there is a pre-processor script. Marked handles all the Markdown conversion and the pre-processor converts the Critic Markup to "ins", "del", and "aside" tags. The script also injects some styling for the these tags.

To configure the pre-processor, go to the preferences "behavior" section and point the pre-processor to the script. 


![](http://www.macdrifter.com/uploads/2013/01/Screen%20Shot%2020130113_152005.jpg)


You must make the python pre-processor script executeable with the following command:

    sudo chmod a+x <path_to_processor_script_file>
    
You must also disable the headline collapsing feature of Marked as this appears to conflict with the rendered file:

![](http://www.macdrifter.com/uploads/2013/01/Screen_Shot_20130113_200742.jpg)


If you are using an earlier version of Marked.app, there is a processor that also converts the markdown using the Python [markdown2 module](http://code.google.com/p/python-markdown2/). For this to work, you will need to install the markdown2 module on your system. Configure Marked.app to use the processor in the preferences by selecting the processor option and adding the path to the python script.

#### Mac System Plugins ####

There are two system services to use with Critic. These can be installed in the normal System Services folder:

    /Users/<user_name>/Library/Services

The system services will Accept or Reject a selected Critic mark as appropriate. Select a Critic mark in any Mac application and then trigger the service to change the markup to standard text.

For example:

    Lorem ipsum dolor{++ sit++} amet...

Is converted to:

    Lorem ipsum dolor sit amet...

**Development Note: There's still a bug with the system service when a snippet is replaced by an empty string (for example when accepting a Deletion). Apparently a system service can not replace selected text with an empty string.**

#### Sublime Text Tools ####

The Sublime Text package includes a language definition for Critic Markup. To install the Sublime Package, drop it in the packages folder:

"/Users/<user_name>/Library/Application Support/Sublime Text 2/Packages"

Select "Critic" as the language type in Sublime Text to reveal the syntax highlighting:

![](http://www.macdrifter.com/uploads/2013/01/Screen%20Shot%2020130111_111656.jpg)

The plugin package provides several functions for working with Critic Markup:

*list_critics*

This command produces a complete list of all Critic Markup tags in the current document. Selecting an item from the list 

![](http://www.macdrifter.com/uploads/2013/01/Screen%20Shot%2020130103_222655_std.jpg)

will scroll to the corresponding position in the document and select the entire Critic tag.

![](http://www.macdrifter.com/uploads/2013/01/Screen%20Shot%2020130103_222716_std.jpg)

*accept_critics_comments*

This command similarly lists all comments in the current document:

![](http://www.macdrifter.com/uploads/2013/01/Screen%20Shot%2020130103_223719_std.jpg)

Selecting a comment from the list will scroll the window to the comment and select the entire Critic tag.

*accept_critic*

This command is best when combined with the *list_critics* command. With an entire critic tag selected, the *accept_critic* command will display a choice of accepting or rejecting the current Critic Mark:

![](http://www.macdrifter.com/uploads/2013/01/Screen%20Shot%2020130103_224025_std.jpg)

Accepting a Critic deletion will delete the entire mark. Rejecting a Critic deletion will undo the tag and return the text to the original state as entered by the author.

![](http://www.macdrifter.com/uploads/2013/01/Screen%20Shot%2020130103_225247.jpg)

Critic Addition marks work similarly with the function.

*mark_critic*

This function provides a quick way to wrap the selected text in a Critic Markup tag. A Sublime Text quick panel provides three options:

![](http://www.macdrifter.com/uploads/2013/01/Screen%20Shot%2020130103_225821_std.jpg)

The *mark_critic* method works on multiple selections at once for synchronous marking of multiple words or phrase.


To bind these functions to keyboard shortcuts, add the following entries to the Sublime Text User Key Bindings:

    { "keys": ["ctrl+c"], "command": "list_critics" },
    { "keys": ["ctrl+a"], "command": "accept_critic" },
    { "keys": ["ctrl+shift+c"], "command": "list_critics_comments" },
    { "keys": ["ctrl+m"], "command": "mark_critic" }


#### BBEdit Tools ####

The BBEdit folder contains one Codeless Language Module and one AppleScript. The language module defines Critic comments as language comments and Critic additions and deletions as functions.

**Development Note: The BBEdit codeless language module is still under development. Defining additions and deletions has some advantages for scope selection but I'm not particularly happy with the current design. The regex matching for comments is still a bit hit and miss.**

The Critic marks can be selected from the function list in BBEdit. Selecting a mark in the list will completely select the string in the editor window.

![](http://www.macdrifter.com/uploads/2013/01/Screen%20Shot%2020130113_142157.jpg)

The AppleScript for BBEdit works similarly and can be used without the language module. The "Select Critic Mark" script will open a list selector window with a complete list of all Critic marks in the document. Select a mark and click "Ok" to select the entire mark in the editor window.

Once a mark is selected, it can be accepted or rejected using the System Services described above.

#### Keyboard Maestro Macros ####

There are three Keyboard Maestro macros to make entering Critic marks easier. If text is selected in an application, the macros will convert them into the corresponding Critic mark. Without text selected, a generic Critic mark will be inserted.

------------

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">CriticMarkup</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://criticmarkup.com" property="cc:attributionName" rel="cc:attributionURL">Gabriel Weatherhead and Erik Hess</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="http://daringfireball.net/projects/markdown/" rel="dct:source">http://daringfireball.net/projects/markdown/</a>.

------------
