#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import re
import sys

BUNDLE_MAP  = {"msg":"messages", "lbl":"labels"}
LANGS       = ["tr", "en"]

XHTML_REGEX = "(%s)\['(.*?)'\]" % ("|").join(BUNDLE_MAP)

def get_all_java_files(root_dir):
    file_list = []
    for r,d,f in os.walk(root_dir):
        for file in f:
            if str(file).endswith(".java"):
                file_list.append((r, file))
    return file_list

def get_all_xhtml_files(root_dir):
    file_list = []
    for r,d,f in os.walk(root_dir):
        for file in f:
            if str(file).endswith(".xhtml"):
                file_list.append((r, file))
    return file_list

def get_bundle_files(root_dir):
    file_list = []
    for r,d,f in os.walk(root_dir):
        if r.startswith("%starget" % (root_dir)):
            continue
        for file in f:
            for k, v in BUNDLE_MAP.iteritems():
                for lang in LANGS:
                    if str(file) == "%s_%s.properties" % (v, lang):
                        file_list.append({k:(r, file)})
    return file_list

def search_in_xhtml(line):
    result = []
    xhtml_regex = re.compile(XHTML_REGEX)    
    li = re.findall(xhtml_regex, line) 
    if li != []:
        for element in li:
            result.append([i.strip() for i in element])
    return result 

def get_all_entries_in_xhtml(xhtml_file_handler):
    result_entries = []
    for line in xhtml_file_handler:
        line_result = search_in_xhtml(line)
        if line_result != []:
            for i in line_result:
                result_entries.append(i)
    return result_entries
        
def get_all_entries_in_bundle(bundle_file_handler):
    result_entries = []
    for line in bundle_file_handler:
        if line.strip() != "":
            result_entries.append(get_key(line))
    return result_entries

def read_file(file_tuple):
    return open(file_tuple[0] + "/" + file_tuple[1])

# (abc)=deneme
def get_key(line):
    return line.split("=")[0].strip()

try:
    project = sys.argv[1]
    if project[-1] != "/":
        project = project + "/"
except:
    print "Proje Adi Belirtilmeli. Ornek: bandil backoffice"
    sys.exit()

xhtml_files = get_all_xhtml_files(project)
bundle_files = get_bundle_files(project) 

for xhtml_file in xhtml_files:
    xhtml_handler = read_file(xhtml_file)
    xhtml_entries = get_all_entries_in_xhtml(xhtml_handler)    

    for entry in xhtml_entries:
       for file in bundle_files:
           for k, v in file.iteritems():
               if entry[0] == k:
                   f = read_file(v)
                   bundle_keys = get_all_entries_in_bundle(f)
                   if entry[1] not in bundle_keys:
                       print "%s dosyasindaki '%s', %s dosyasinda yok" % (xhtml_file[0] + "/" + xhtml_file[1], entry[1], v[1])
