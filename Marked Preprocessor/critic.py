#!/usr/bin/python
import sys
import os
import re

add_pattern = r'''(?s)\{\+\+(?P<value>.*?)\+\+[ \t]*(\[(?P<meta>.*?)\])?[ \t]*\}'''

del_pattern = r'''(?s)\{\-\-(?P<value>.*?)\-\-[ \t]*(\[(?P<meta>.*?)\])?[ \t]*\}'''

comm_pattern = r'''(?s)\{~~(?P<value>.*?)~~[ \t]*(\[(?P<meta>.*?)\])?[ \t]*\}'''

# Converts Addition markup to HTML
def additionProcess(group_object):
	replaceString = '<ins>'+group_object.group('value')
	if group_object.group('meta'):
		replaceString = replaceString+'<span class="criticmeta">'+group_object.group('meta')+'</span>'
	replaceString = replaceString+'</ins>'
	return replaceString


def deletionProcess(group_object):
	replaceString = '<del>'+group_object.group('value')
	if group_object.group('meta'):
		replaceString = replaceString+'<span class="criticmeta">'+group_object.group('meta')+'</span>'
	replaceString = replaceString+'</del>'
	return replaceString


def commentProcess(group_object):
	replaceString = '<aside>'+group_object.group('value')
	if group_object.group('meta'):
		replaceString = replaceString+'<span class="criticmeta">'+group_object.group('meta')+'</span>'
	replaceString = replaceString+'</aside>'
	return replaceString

a = '''

<style>
	#wrapper {
		padding-top: 30px !important;
	}

	#criticnav {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		box-shadow: 0 1px 1px 1px #777;
		margin: 0;
		padding: 0;
		background-color: white;
		font-size: 12px;
	}

	#criticnav ul {
		list-style-type: none;
		width: 90%;
		margin: 0 auto;
		padding: 0;
	}

	#criticnav ul li {
		display: block;
		width: 33%;
		text-align: center;
		padding: 10px 0 5px!important;
		margin: 0 !important;
		line-height: 1em;
		float: left;
		border-left: 1px solid #ccc;
		text-transform: uppercase;
	}

	#criticnav ul li#markup-button {
		border-right: 1px solid #ccc;
	}

	#criticnav ul li.active {
		background-image: -webkit-linear-gradient(top, white, #cccccc)
	}

	.original del {
		
			text-decoration: none;
	}	

	.original ins,
	.original aside,
	.original del span {
		display: none;
	}

	.edited ins {
		
			text-decoration: none;
	}	

	.edited del,
	.edited aside,
	.edited ins span {
		display: none;
	}

	.markup aside {
	    font-size: 0.9em;
	    color: #ff0000;
	}

	.markup del {
	    background-color: #f6a9a9;
	    text-decoration: none;
	}

	.markup ins {
	    background-color: #a9f6a9;
	    text-decoration: none;
	}

	.markup del span.criticmeta,
	.markup ins span.criticmeta {
	    display: none;
	}

	.markup aside span.criticmeta {
	    display: block;
	    color: #999;
	}

	.markup del:hover span.criticmeta,
	.markup ins:hover span.criticmeta {
	    display: block;
	    position: absolute;
	    left: 20%;
	    font-size: 0.8em; 
	    color: #ccc;
	    background-color: #333;
	    z-index: 10;
	    padding: 0.5em 1em;
	    border-radius: 0.5em;
	}

	@media (min-width:640px) {
	
		.markup {
			margin-right: 35% !important;
		}

		.markup aside {
		    display: block;
		    position: absolute;
		    left: 70%;
		    width: 25%;
		    font-size: 0.9em;
		    color: #ff0000;
		}

    }
}

</style>

<div id="criticnav">
	<ul>
		<li id="markup-button">Markup</li>
		<li id="original-button">Original</li>
		<li id="edited-button">Edited</li>
	</ul>

</div>

<script type="text/javascript">

	function critic() {

		$('#firstdiff').remove();
		$('#wrapper').addClass('markup');
		$('#markup-button').addClass('active');

	}  

	function original() {
		$('#original-button').addClass('active');
		$('#edited-button').removeClass('active');
		$('#markup-button').removeClass('active');

		$('#wrapper').addClass('original');
		$('#wrapper').removeClass('edited');
		$('#wrapper').removeClass('markup');
	}

	function edited() {
		$('#original-button').removeClass('active');
		$('#edited-button').addClass('active');
		$('#markup-button').removeClass('active');

		$('#wrapper').removeClass('original');
		$('#wrapper').addClass('edited');
		$('#wrapper').removeClass('markup');
	} 

	function markup() {
		$('#original-button').removeClass('active');
		$('#edited-button').removeClass('active');
		$('#markup-button').addClass('active');

		$('#wrapper').removeClass('original');
		$('#wrapper').removeClass('edited');
		$('#wrapper').addClass('markup');
	}

	var o = document.getElementById("original-button");
	var e = document.getElementById("edited-button");
	var m = document.getElementById("markup-button");

	window.onload = critic;
	o.onclick = original;
	e.onclick = edited;
	m.onclick = markup;

</script>
'''

# Accept input from Marked.app
inputText = sys.stdin.read()

h = re.sub(add_pattern, additionProcess, inputText)

h = re.sub(del_pattern, deletionProcess, h)

h = re.sub(comm_pattern, commentProcess, h)

z = h + a

sys.stdout.write(z)

