forro
---
Forro founds missing 'for' attributes of outputLabel tags in JSF facelets. Missing 'for' attributes cause unnecessary logs. It allows you to find them and fix.

usage
---
forro.py [FACELET_PATH]

It will be search recursively for all facelet (.xhtml) files.

usage example
---
forro.py ./workspace/my_lovely_jsf_project/

output example
---
File: ./workspace/my_lovely_jsf_project/index.xhtml, Line: 51, Tag Type: h:outputLabel
File: ./workspace/my_lovely_jsf_project/ezba1.xhtml, Line: 31, Tag Type: p:outputLabel