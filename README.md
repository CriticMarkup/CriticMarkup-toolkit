Welcome to the CriticMarkup Toolkit
====================

The toolkit includes various code snippets and scripts to help you use CriticMarkup in your daily workflow.

## The Critic Markup Syntax ##

Critic Markup is intended to provide basic editorial change tracking in plain text files. The syntax is compatible with Markdown, MultiMarkdown and HTML.

### The Goal ###

Critic Markup can be used in any writing environment without special applications or tool kits. While we have supplied processors and plugins that are compatible with popular apps, they are not required.

Critic Markup should be readable inline and clearly indicate the intent of the editor and author.

Critic Markup should support change tracking with multiple authors and editors.

### The Basic Syntax ###

There are three types of Critic marks: Addition, Deletion and Comment. Copy editing is enabled by the application of these three basic marks.

#### Additions ####

Additions are inserted inline by surrounding the desired text with curly braces and double plus marks as shown:

    Lorem ipsum dolor{++ sit++} amet...

A space character and "sit" are to be added at the position of the left (or right) most curly brace. The additions are rendered as `<ins>` tags in the processed HTML:

    <p>Lorem ipsum dolor<ins> sit</ins> amet...</p>

#### Deletions ####

Deletions are denoted with a similar syntax. The text to be deleted is surrounded with curly braces and double dashes as shown:

    Lorem{-- ipsum--} dolor sit amet...

The word "ipsum" and a space character are marked for deletion in the above example. These deletions are rendered as `<del>` tags in the processed HTML:

    <p>Lorem<del> ipsum</del> dolor sit amet...</p>

#### Comments ####

Comments may be added as required by an editor or author. Comments are surrounded by curly braces and double tilde (a.k.a twiddle) as shown:

    Lorem ipsum dolor sit amet...
    
    {~~This is a stand alone comment~~}
    
Comments are rendered as `<aside` tags in the processed HTML. Remember that `<aside>` tags are block-level elements and will render as such.

    <p>Lorem ipsum dolor sit amet...</p>
    
    <aside>This is a stand alone comment</aside>

#### Putting it all together ####

The three marks can be used in combination to indicate more complex changes:

**Word Change**

    Lorem ipsum {--color--}{++dolor++} sit amet, consectetur adipisicing elit.

**Capitalization**

    {--l--}{++L++}orem ipsum dolor sit amet, consectetur adipisicing elit.

### Extended Syntax ###

Critic Markup supports meta data within each edit. Meta data such as author initials, date and comment may be included in square brackets as shown:

    Lorem{--ipsum -- [@GSW 2013-01-03 22:03:58  I don't like this word]} dolor sit amet...

The extended meta data is free-form and is designed to satisfy a variety of needs. We suggest prefixing the author initials with an apetail ("@") where needed.

### The Tools ###

While Critic Markup can be used with any text editor on any device, we have created several convenience tools to make working with Critic easy and helpful.

All of the tools listed below assume adherence with the Critic standards outlined above. Deviation from the documented standards will render the tools below non-functional.

#### Mac System Plugins ####

There are two system services to use with Critic. These can be installed in the normal System Services folder:

/Users/<user_name>/Library/Services

The system services will Accept or Reject a selected Critic mark as appropriate. Select a Critic mark in any Mac application and then trigger the service to change the markup to standard text.

For example:

*Lorem ipsum dolor{++ sit++} amet...*

Is converted to:

*Lorem ipsum dolor sit amet...*


#### Sublime Text Tools ####

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

To install the Sublime Package, drop it in the packages folder:

"/Users/<user_name>/Library/Application Support/Sublime Text 2/Packages"

To bind these functions to keyboard shortcuts, add the following entries to the Sublime Text User Key Bindings:

    { "keys": ["ctrl+c"], "command": "list_critics" },
    { "keys": ["ctrl+a"], "command": "accept_critic" },
    { "keys": ["ctrl+shift+c"], "command": "list_critics_comments" },
    { "keys": ["ctrl+m"], "command": "mark_critic" }


#### BBEdit Tools ####

The BBEdit folder contains one Codeless Language Module and one AppleScript. The language module defines Critic comments as language comments and Critic additions and deletions as functions.

The Critic marks can be selected from the function list in BBEdit. Selecting a mark in the list will completely select the string in the editor window.

The AppleScript for BBEdit works similarly and can be used without the language module. The "Select Critic Mark" script will open a list selector window with a complete list of all Critic marks in the document. Select a mark and click "Ok" to select the entire mark in the editor window.

Once a mark is selected, it can be accepted or rejected using the System Services described above.

#### Keyboard Maestro Macros ####

There are three Keyboard Maestro macros to make entering Critic marks easier. If text is selected in an application, the macros will convert them into the corresponding Critic mark. Without text selected, a generic Critic mark will be inserted.





