## Introduction ##

The Critic Markup CLI is for use with the [Critic Markup Syntax](http://criticmarkup.com). The CLI is a Command Line Interface to convert a Critic Markup file into styled HTML for use with any browser.

## Dependencies ##

The CLI script requires a Python module for converting Multimarkdown into HTML. The default is for the CLI to use the [Python-Markdown](http://pythonhosted.org/Markdown/) module with the 'extra', 'codehilite', 'meta' extensions enabled.

To use the Critic Markup CLI, please [install the module](http://pythonhosted.org/Markdown/install.html).

As an alternative, the CLI can use the [Python-Markdown2](https://github.com/trentm/python-markdown2) module with the 'footnotes', 'fenced-code-blocks', 'cuddled-lists', 'code-friendly' extensions enabled.

To use Python-Markdown2, please [install the library manually](https://github.com/trentm/python-markdown2/#install), using one of several methods.

## Features ##

To see the basic usage of the parser, execute the script as follows:

    >> python criticParser_CLI.py -h
    usage: criticParser_CLI.py [-h] [-m2] [-o out-file] [-css in-file] [-b] source

    Convert Critic Markup to HTML

    positional arguments:
      source                The source file path, including file name

    optional arguments:
      -h, --help            show this help message and exit
      -m2                   Use the markdown2 python module. If left blank then markdown module is used
      -o out-file, --output out-file
                            Path to store the output file, including file name
      -css in-file, --css in-file
                            Path to a custom CSS file, including file name
      -b, --browser         View the output file in the default browser after saving.

The Critic Markup CLI requires at least one argument consisting of the file path to a text file and is executed from the command line as a Python script.

    python criticParser_CLI.py <path_to_source_file>

By default, the CLI tool will output an HTML file in the same location as the source file appended with _CriticParserOut.

### Options ###

There are several optional flags available with the CLI.

The `-m2` option allows the user to convert Markdown using the Python-Markdown2 module. Some may prefer the results of this module in comparison to the original Python-Markdown module.

The `-o` option allows a user to specify an output file and location. The result file saves with overwrite.

The `-css` option allows a uer to override the default CSS, JavaScript and JQuery imports with a user specified file. The `-css` option must be followed by the file path to an alternative.

The `-b` flags immediately opens the output file in the default browser.

### Example Usage ###

From the terminal, the following command will convert a Critic Markup file to HTML using a custom CSS file and open it in the default browser.

     python criticParser_CLI.py 'my_CM_File.md' -o 'my_CM_Output.html' -m2 -css custom_CM_CSS.css -v



