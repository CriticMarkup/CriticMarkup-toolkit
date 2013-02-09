Critic Markup is intended to provide basic editorial change tracking in plain text files. The syntax is compatible with Markdown, MultiMarkdown and HTML.

### The Three Laws ###

1. Critic Markup shall be human readable. A human with a simple text editor can easily read and comprehend any text containing Critic Markup
2. Critic Markup shall be computer readable except where it conflicts with rule 1. Markup syntax should be easily parsed with simple regular expressions to support a wide variety of implementations.
3. Critic Markup shall be compatible with existing markup syntax for Markdown, MultiMarkdown and HTML except where it conflicts with rules one or two. Many users of plain text write in combinations of Markdown and HTML. Critic Markup should work alongside that syntax.

### The Goal ###

Critic Markup can be used in any writing environment without special applications or tool kits. While we have supplied processors and plugins that are compatible with popular apps, they are not required.

Critic Markup should be readable inline and clearly indicate the intent of the editor and author.

Critic Markup should support change tracking with multiple authors and editors.

### The Basic Syntax ###

There are three types of Critic marks: Addition, Deletion and Highlight. Copy editing is enabled by the application of these three basic marks.

#### Additions ####

Additions are inserted inline by surrounding the desired text with curly braces and double plus marks as shown:

    Lorem ipsum dolor{++ sit++} amet...

A space character and "sit" are to be added at the position of the left (or right) most curly brace. The additions are rendered as `<ins>` tags in the processed HTML:

    Lorem ipsum dolor<ins> sit</ins> amet...

Paragraphs may be inserted in the same manner.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum at orci magna. Phasellus augue justo, sodales eu pulvinar ac, vulputate eget nulla. Mauris massa sem, tempor sed cursus et, semper tincidunt lacus.{++

    ++}Praesent sagittis, quam id egestas consequat, nisl orci vehicula libero, quis ultricies nulla magna interdum sem. Maecenas eget orci vitae eros accumsan mollis. Cras mi mi, rutrum id aliquam in, aliquet vitae tellus. Sed neque justo, cursus in commodo eget, facilisis eget nunc. Cras tincidunt auctor varius.

To ensure the Markdown processor outputs valid HTML, the `<ins>` tags get wrapped in newlines. The result is that both paragraphs render separately with a block-type `<ins>` between. The non-breaking-space gives the tag enough content to render properly.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum at orci magna. Phasellus augue justo, sodales eu pulvinar ac, vulputate eget nulla. Mauris massa sem, tempor sed cursus et, semper tincidunt lacus.

    <ins>&nbsp;</ins>

    Praesent sagittis, quam id egestas consequat, nisl orci vehicula libero, quis ultricies nulla magna interdum sem. Maecenas eget orci vitae eros accumsan mollis. Cras mi mi, rutrum id aliquam in, aliquet vitae tellus. Sed neque justo, cursus in commodo eget, facilisis eget nunc. Cras tincidunt auctor varius.

Rules for proper use of the `<ins>` tag can be found in the [HTML 4 spec](http://www.w3.org/TR/REC-html40/struct/text.html#h-9.4).

#### Deletions ####

Deletions are denoted with a similar syntax. The text to be deleted is surrounded with curly braces and double dashes.

    Lorem{-- ipsum--} dolor sit amet...

The word "ipsum" and a space character are marked for deletion in the above example. These deletions are rendered as `<del>` tags in the processed HTML.

    Lorem<del> ipsum</del> dolor sit amet...

Paragraphs may also be deleted.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum at orci magna. Phasellus augue justo, sodales eu pulvinar ac, vulputate eget nulla. Mauris massa sem, tempor sed cursus et, semper tincidunt lacus.{--

    --}Praesent sagittis, quam id egestas consequat, nisl orci vehicula libero, quis ultricies nulla magna interdum sem. Maecenas eget orci vitae eros accumsan mollis. Cras mi mi, rutrum id aliquam in, aliquet vitae tellus. Sed neque justo, cursus in commodo eget, facilisis eget nunc. Cras tincidunt auctor varius.

The newlines will be removed by the processor and replaced by an inline <del> tag. Again, the non-breaking-space gives the tag enough content to render properly.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum at orci magna. Phasellus augue justo, sodales eu pulvinar ac, vulputate eget nulla. Mauris massa sem, tempor sed cursus et, semper tincidunt lacus.<del>&nbsp;</del>Praesent sagittis, quam id egestas consequat, nisl orci vehicula libero, quis ultricies nulla magna interdum sem. Maecenas eget orci vitae eros accumsan mollis. Cras mi mi, rutrum id aliquam in, aliquet vitae tellus. Sed neque justo, cursus in commodo eget, facilisis eget nunc. Cras tincidunt auctor varius.

Rules for proper use of the `<del>` tag can be found in the [HTML 4 spec](http://www.w3.org/TR/REC-html40/struct/text.html#h-9.4).

#### Substitutions ####

Substitutions combine an insertion and a deletion. The syntax reflects this.

    Lorem {--hipsum~>ipsum++} dolor sit amet...

Despite the shortened syntax, substitutions render just like a deletion followed by an insertion.

    Lorem <del>hipsum</del><ins>ipsum</ins> dolor sit amet...

Newlines are treated the same as a deletion or insertion, depending on where they're located.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum at orci magna. Phasellus augue justo, sodales eu pulvinar ac, vulputate eget nulla. {--Mauris massa sem, tempor sed cursus et, semper tincidunt lacus.~>

    ++}Praesent sagittis, quam id egestas consequat, nisl orci vehicula libero, quis ultricies nulla magna interdum sem. Maecenas eget orci vitae eros accumsan mollis. Cras mi mi, rutrum id aliquam in, aliquet vitae tellus. Sed neque justo, cursus in commodo eget, facilisis eget nunc. Cras tincidunt auctor varius.

After rendering this example, the deletion becomes an inline element at the end of the first paragraph and the insertion becomes a minimal block element.    

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum at orci magna. Phasellus augue justo, sodales eu pulvinar ac, vulputate eget nulla. <del>Mauris massa sem, tempor sed cursus et, semper tincidunt lacus.</del>

    <ins>;nbsp;</ins>

    Praesent sagittis, quam id egestas consequat, nisl orci vehicula libero, quis ultricies nulla magna interdum sem. Maecenas eget orci vitae eros accumsan mollis. Cras mi mi, rutrum id aliquam in, aliquet vitae tellus. Sed neque justo, cursus in commodo eget, facilisis eget nunc. Cras tincidunt auctor varius.

#### Highlights ####

Highlighted passages may be added as required by an editor or author. The text to be highlighted is surrounded by curly braces and double tilde (a.k.a twiddle) as shown:

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. {~~Vestibulum at orci magna. Phasellus augue justo, sodales eu pulvinar ac, vulputate eget nulla.~~} Mauris massa sem, tempor sed cursus et, semper tincidunt lacus.
    
Highlights are rendered as `<mark>` tags in the processed HTML. 

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. <mark>Vestibulum at orci magna. Phasellus augue justo, sodales eu pulvinar ac, vulputate eget nulla.</mark> Mauris massa sem, tempor sed cursus et, semper tincidunt lacus.

Rules for proper use of the `<mark>` tag can be found in the [HTML 5 spec](http://www.w3.org/html/wg/drafts/html/master/single-page.html#the-mark-element).

#### Comments ####

Comments may be added to any change via a set of square brackets prior to the closing brace of the tag.

    {++Lorem ipsum dolor sit amet.++[This is a comment]}
    {--Lorem ipsum dolor sit amet.--[This is a comment]}
    {--Lorem hipsum dolor sit amet.~>Lorem ipsum dolor sit amet.++[This is a comment]}
    {~~Lorem ipsum dolor sit amet.~~[This is a comment]}

Comments render as the `title` attribute of the relevant HTML tag. For substitutions, the title element is attached to the trailing `<ins>` tag.

    <ins title="This is a comment">Lorem ipsum dolor sit amet.</ins>
    <del title="This is a comment">Lorem ipsum dolor sit amet.</del>
    <del>Lorem hipsum dolor sit amet.</del><ins title="This is a comment">Lorem ipsum dolor sit amet.</ins>
    <mark title="This is a comment">Lorem ipsum dolor sit amet.</mark>

Comments can be used however you like, whether as explanations for the changes, timestamps or more. Rendering of newlines in the `title` attribute are inconsistent, so we recommend against using them in comments.

{--Lorem ipsum dolor sit amet.--[@EMH 2013.01.24.0621: This phrase is overused]}

Most desktop browsers display the `title` attribute as a popover.

![Way too picky.](http://high90.com/img/picky2.png)

 Rules for proper use of the `title` attribute can be found in the [HTML 4 spec](http://www.w3.org/TR/REC-html40/struct/global.html#h-7.4.3).

#### Putting it all together ####

When used in combination the marks can indicate more complex changes.

    {--Eighty-seven~>Four score and seven++[Has greater weight]} years ago our fathers brought forth on this continent a new {--state~>nation++[More inclusive]}, conceived in liberty, and dedicated to the proposition that all men {--and women--[Not THAT inclusive - we'll tackle this issue after the war]} are created equal.{++

    ++}Now we are engaged in a great {--struggle~>civil war++[Let's call this what it is]}, testing whether that nation, or any nation, so {--concieved~>conceived++[I before E except after C]} and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to {--consecrate~>dedicate++[They consecrated it, we can't do much more than dedicate now]} a portion of that field, as {--an ultimate~>a final++[simpler, clearer]} resting place for those who here gave their lives {~~that that~~[OK, but avoid if possible]} nation might live. It is {--all together~>altogether++[NB: Stop writing on trains]} fitting and proper that we should do this.

The above paragraphs should render to HTML in the following manner.

    <del>Eighty-seven</del><ins title="Has greater weight">Four score and seven</ins> years ago our fathers brought forth on this continent a new <del>state</del><ins title="More inclusive">nation</ins>, conceived in liberty, and dedicated to the proposition that all men <del title="Not THAT inclusive - we'll tackle this issue after the war">and women</del> are created equal.

    <ins>&nbsp;</ins>

    Now we are engaged in a great <del>struggle</del><ins title="Let's call this what it is">civil war</ins>, testing whether that nation, or any nation, so <del>concieved</del><ins title="I before E except after C">conceived</ins> and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to <del>consecrate</del><ins title="They consecrated it, we can't do much more than dedicate now">dedicate</ins> a portion of that field, as <del>an ultimate</del><ins title="simpler, clearer">a final</ins> resting place for those who here gave their lives <mark title="OK, but avoid if possible">that that</mark> nation might live. It is <del>all together</del><ins title="NB: Stop writing on trains">altogether</ins> fitting and proper that we should do this.


