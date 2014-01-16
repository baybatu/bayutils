forro
---
Forro founds missing 'for' attributes of outputLabel tags in JSF facelets. Missing 'for' attributes cause unnecessary logs. It allows you to find them and fix.

usage
---
forro.py _[FACELETPATH]_

It will be search recursively for all facelet (*.xhtml) files.

usage example
---
forro.py ./workspace/mylovelyjsfproject/

output example
---
File: ./workspace/mylovelyjsfproject/index.xhtml, Line: 51, Tag Type: h:outputLabel

File: ./workspace/mylovelyjsfproject/ezba1.xhtml, Line: 31, Tag Type: p:outputLabel