import re
import xml.etree.ElementTree as etree
from PlumedToHTML import test_and_get_html, get_html_header
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension

class PlumedProcessor(Preprocessor):
     def run(self, lines):
         inside_plumed_block = False
         plumed_block_start = None
         plumed_blocks = []

         # Find all the plumed blocks in the markdown
         for line_number, line in enumerate(lines):
            if line.strip() == '\\plumedfile' and not inside_plumed_block:
                plumed_block_start = line_number
                inside_plumed_block = True
            if line.strip() == '\\endplumedfile' and inside_plumed_block:
                plumed_blocks.append((plumed_block_start, line_number))
                inside_plumed_block = False
         
         # Now run over the plumed blocks 
         num = 1
         for plumed_block_start, plumed_block_end in reversed(plumed_blocks):
             # Retrieve the html that is output by plumed
             html = test_and_get_html( '\n'.join(lines[plumed_block_start+1:plumed_block_end]), "plinp" + str(num) )
             placeholder = self.md.htmlStash.store(html) 
             lines[plumed_block_start:plumed_block_end+1] = [placeholder]
             num = num + 1
         return lines

class PlumedPostprocessor(Postprocessor):
     def run(self, text):
         return get_html_header() + text

class PlumedExtension(Extension):
     def extendMarkdown(self, md):
         # Priority here  is the same as the priority for `fenced_code_block`
         md.preprocessors.register(PlumedProcessor(md), 'plumed_inputs', 25)
         md.postprocessors.register(PlumedPostprocessor(md), 'plumed_scripts',30) 
