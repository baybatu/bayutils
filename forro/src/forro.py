# Batuhan Bayrakci<batuhanbayrakci@gmail.com> - 16 Jan 2014
# Founds missing 'for' attributes of h:outputLabel and p:outputLabel tags

import os
import lxml.etree
import sys
import string

namespaces = {'p' : 'http://primefaces.org/ui',
              'h' : 'http://java.sun.com/jsf/html'}

exclude_paths = ["/target/"]

class ErrorTag:
    def __init__(self, filename, line, tagtype):
        self.filename = filename
        self.line = line
        self.tagtype = tagtype
    def __str__(self):
        return "File: %s, Line: %s, Tag Type: %s" % (self.filename, self.line, self.tagtype)

def generate_xpath():
    tag_list = []
    for key in namespaces.iterkeys():
        tag_list.append(".//%s:outputLabel" % (key))

    return string.join(tag_list, '|')

def get_all_xhtml_files(root_dir):
    file_list = []
    for r,d,f in os.walk(root_dir):
        if is_excluded(r, exclude_paths):
            continue
        #if r.find("/target/") != -1:
        #    continue
        for file in f:
            if str(file).endswith(".xhtml"):
                file_list.append((r, file))
    return file_list

def is_excluded(path, excluded_paths):
    for excluded_path in excluded_paths:
        if path.find(excluded_path) != -1:
            return True
    return False

def file_fullpath(file):
    return file[0] + "/" + file[1];

if len(sys.argv) != 2:
    print "Directory problem. exiting..."
    sys.exit(1)

print "checking 'for' attributes of outputLabel tags..."

rootpath = sys.argv[1]

xpath = generate_xpath()
files = get_all_xhtml_files(rootpath)

error_result = []

for f in files:
    filepath = file_fullpath(f)
    data = open(filepath, 'r').read()
    try:
        tree = lxml.etree.fromstring(data)
    except:
        continue

    foundElements = tree.xpath(xpath, namespaces=namespaces)
    for element in foundElements:
        try:
            forAttrib = element.attrib['for']
        except KeyError, ke:
            error_result.append(ErrorTag(filepath, element.sourceline, "%s:outputLabel" % (element.prefix)))

for result in error_result:
    print result

if error_result:
    print "Found %s corrupt attributes in %s directory" % (len(error_result), rootpath)
else:
    print "Clear!.."