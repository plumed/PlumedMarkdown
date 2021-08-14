# PlumedMarkdown

This extension adds PLUMED input file support to !(https://github.com/Python-Markdown/markdown)[Python-Markdown]

# Installation

You can install this using the command:

````
pip installl PlumedMarkdown
````

# Usage

You can include PLUMED input files in your markdown files between `\plumedfile` and `\endplumedfile` as shown below:

````
\plumedfile
d1: DISTANCE ATOMS=1,2
PRINT ARG=d1 FILE=colvar
\endplumedfile
````

When you convert the resulting file to HTML using markdown you can then use a python script something like this:

````
import markdown
from PlumedMarkdown import PlumedExtension

markdown.markdownFromFile( input="myfile.md", extensions[PlumedExtension()], )
````
