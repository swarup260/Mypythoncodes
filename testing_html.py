# -*- coding: utf-8 -*-
"""
create File Structure for website projects


"""
import os
import sys


def create_folder(directory):
    """
    Create folder structure
    file_name
    |__css
    |__js
    |__img
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        css = directory +'/css'
        os.makedirs(css)
        js = directory +'/js'
        os.makedirs(js)
        img = directory +'/img'
        os.makedirs(img)
    else:
        print("file Exixts")

def create_file(directory):
    """
    Create files structure
    file_name
    |__css/style.css
    |__js/main.js
    |__img
    |_index.html
    """
    css_file = directory + '/css/style.css'
    js_file = directory + '/js/main.js'
    html_file = directory +'/index.html'
    if not os.path.isfile(css_file):
        write_file(css_file)
    if not os.path.isfile(js_file):
        write_file(js_file)
    if not os.path.isfile(html_file):
        write_file(html_file)
    print("Complete.....................")
        
def write_file(path):
    """
    Create files
    """
    f = open(path,'w')
    f.write("//Comments")
    f.close()

file_name = sys.argv[1]
create_folder(file_name)   
create_file(file_name)