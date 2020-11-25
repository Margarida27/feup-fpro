# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:27:53 2019

@author: Margarida Viera
"""

def file_finder(dirs, file_name):

    if dirs == file_name:
            return file_name
         
    for i in dirs[1:]:
        if file_finder(i, file_name) != None:
            return dirs[0] + "/" + file_finder(i, file_name)
        
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'page.html'))
