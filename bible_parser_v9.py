# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:31:39 2021

@author: Curtis Taylor
"""

import time
import os, sys
import io
#import array
#import re

# Function inputs KJV bible text file then parses the file into
# dictionary variable 'scriptures'
def parser():
    
    # 'scripture' dictionary uses names of bible(ex Genesis) as key
    # and connects keys to their verses
    scriptures = {}
    
    # BOOK NAMES OF BIBLE List
    book_names = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua',
    'Judges', 'Ruth', '1st Samuel', '2nd Samuel', '1st Kings', '2nd Kings', '1st Chronicles',
    '2nd Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms',
    'Proverbs', 'Ecclesiastes', 'Song of Solomon',
    'Isaiah', 'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel',
    'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah',
    'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke',
    'John', 'Acts',
    'Romans', '1st Corinthians','2nd Corinthians',
    'Galatians',
    'Ephesians',
    'Philippians',
    'Colossians',
    '1st Thessalonians',
    '2nd Thessalonians',
    '1st Timothy',
    '2nd Timothy',
    'Titus',
    'Philemon',
    'Hebrews',
    'James',
    '1st Peter',
    '2nd Peter',
    '1st John',
    '2nd John',
    '3rd John',
    'Jude',
    'Revelation']
    
    verses = []
    
    # KJV input file path
    f = open(r"D:\1 -CURTIS C DRIVE\VSCode - March 2021\Bible PYTHON\kjv-1769.txt")
   
    
    count = 0
    for line in f:
        if not line.isspace():
          # IF statement run when 'scripture' is a certain length. 
          #Then files closed and this for loop is broken   
          if len(scriptures) > 66: 
               
               # test line
               scriptures.pop(book_names[count]) ####
               
               f.close()
               break 
          # For when "BOOK" IS NOT found in a file line. This means this is
          #means the line is a verse and will be appended to 'verses' list 
          elif line.find("BOOK:", 0, 7) == -1: 
             verses.append(line)
             scriptures[book_names[count]] = verses
 
         
          # This 'else:' is For when "BOOK" IS found in a file line. This means this
          #line is NOT a verse and is the start of an bible book. 
          #'verse' list is cleared and 'count' is incremented
          else:            
             #IF statement Does not activate until the 2nd loop, after 'verses' list has entries. 
             #During The first loop, 'count' needs to be '0' because 'count' is used as
             #a list address. 
             if len(verses) > 0:
               count = count + 1
               verses = []

               
    return (scriptures, book_names)

# Takes in Tuple(dictionary, list)   
# creates 3 file (1)Full text file per  book 2) blank line text file 
# per book 3) blank line text file per book with begining letter  ) 
def doc_maker(tup):
    book_names = tup[1]
    scriptures = tup[0]
    count = 1

    alt_name = {'1st Samuel' : 'samuel1', '2nd Samuel' : 'samuel2', '1st Kings' : 'king1', '2nd Kings' : 'king2', '1st Chronicles' : 'chronicles1', '2nd Chronicles' : 'chronicles2', 'Song of Solomon' : 'solomon', '1st Corinthians' : 'corinthians1', '2nd Corinthians' : 'corinthians2', '1st Thessalonians' : 'thessalonians1', '2nd Thessalonians' : 'thessalonians2', '1st Timothy' : 'timothy1', '2nd Timothy' : 'timothy2', '1st Peter' : 'peter1', '2nd Peter' : 'peter2', '1st John' : 'john1', '2nd John' : 'john2', '3rd John' : 'john3'}

    file_path7 = "D:/1 -CURTIS C DRIVE/VSCode - March 2021/Bible PYTHON/Files2/{}.html".format("Full HTML bible")
    f7 = open(file_path7, "a") # Use append because this is in a loop to make a full bible
    f7.write("<!DOCTYPE html>\n<html lang='en'>\n<head><meta charset='UTF-8'>")
    f7.write("<meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Side Menu</title></head>")
    f7.write("<body>")  

    #file_path8 = "D:/1 -CURTIS C DRIVE/VSCode - March 2021/Bible PYTHON/Files/{}.json".format("Full JSON bible")
    #f8 = open(file_path8, "a")
    #f8.write("[\n")


    for name in book_names:
        
        #if statement needed as fail safe if name is not in dictionary
        if name not in scriptures: # If statement breaks loop 
           break
       
        parent_dir = "D:/1 -CURTIS C DRIVE/VSCode - March 2021/Bible PYTHON/Files2/"
        directory1 = "Full verses Folder"
        directory2 = "Blank verses Folder"
        directory3 = "First Letter only verses Folder"
        directory4 = "Json"
        directory5 = "js"
        
        
        try:
           path = os.path.join(parent_dir, directory1) 
           os.mkdir(path)
           path = os.path.join(parent_dir, directory2) 
           os.mkdir(path)
           path = os.path.join(parent_dir, directory3) 
           os.mkdir(path)       
        except FileExistsError:
           print("{} directory already exists".format(path)) 
            
        try:
           path = os.path.join(parent_dir, directory4) 
           os.mkdir(path)
           path = os.path.join(parent_dir, directory5) 
           os.mkdir(path)
        except FileExistsError:
           print("{} directory already exists".format(path)) 


        file_path = "D:/1 -CURTIS C DRIVE/VSCode - March 2021/Bible PYTHON/Files2/Full verses Folder/{} - {}.txt".format(count, name)
        file_path2 = "D:/1 -CURTIS C DRIVE/VSCode - March 2021/Bible PYTHON/Files2/Blank verses Folder/{} - {}.txt".format(count, name)
        file_path3 = "D:/1 -CURTIS C DRIVE/VSCode - March 2021/Bible PYTHON/Files2/First Letter only verses Folder/{} - {}.txt".format(count, name)
        file_path4 = "D:/1 -CURTIS C DRIVE/VSCode - March 2021/Bible PYTHON/Files2/{}.txt".format("Full 1st Letter Bible")
        file_path5 = "D:/1 -CURTIS C DRIVE/VSCode - March 2021/Bible PYTHON/Files2/{}.txt".format("Full Blank letter Bible")
        file_path6 = "D:/1 -CURTIS C DRIVE/VSCode - March 2021/Bible PYTHON/Files2/{}.txt".format("Full King James Bible")
       

        f = open(file_path, "w") 
        f2 = open(file_path2, "w") 
        f3 = open(file_path3, "w") 
        f4 = open(file_path4, "a") # Use append because this is in a loop to make a full bible
        f5 = open(file_path5, "a") # Use append because this is in a loop to make a full bible
        f6 = open(file_path6, "a") # Use append because this is in a loop to make a full bible
        
        # Takes 1st Kings and puts kings1 in file_nameJS
        if name in alt_name:
            file_nameJS = alt_name[name]
        else:
            file_nameJS = name.lower()

        file_path9 = "D:/1 -CURTIS C DRIVE/VSCode - March 2021/Bible PYTHON/Files2/js/{}.js".format(name)
        f9 = open(file_path9, "w")

        


        txt = "let {}_full_data = [".format(file_nameJS)
        txt2 = "let {}_blank_data = [".format(file_nameJS)
        txt3 = "let {}_first_data = [".format(file_nameJS)
        txt4 = "let {}_misc_data = [".format(file_nameJS)
        #f9.write("var {}_data = [".format(name))

        f4.write('@' + name + '\n')
        f5.write('@' + name + '\n')
        f6.write('@' + name + '\n')
        
        f7.write("<div id='{}-chapter' class='chapter'>".format(name))
        f7.write('<div><h2>' + name + '</h2></div>')
        
        

        # FOR loop that writes the 4 types of documents
        for verse in scriptures[name]:
            # Writes ALL text to file for a certain bible book
            f.write("{}\n".format(verse))
            f6.write("{}\n".format(verse))
            
            f7.write("<div><a href='#' id='{}' class='verse'>{}</a></div><br></br>".format(verse_id(name, verse), verse))
            
            exception_words = ['THE', 'THY', 'THIS', 'THEY', 'THEE', 'THERE', 'THEM', 'TO', 'THAT', 'THAN', 'TOO', 'THUS', 'A', 'ALSO', 'ARE', 'AS', 'AT', 'ALL', 'AND', 'FOR', 'I', 'IF', 'IS', 'IN', 'IT', 'O', 'OR', 'OF', 'OUR', 'NOR', 'HE', 'SHE', 'HIM', 'HIS', 'HER', 'BUT', 'BY', 'WHICH', 'WHERE', 'WAS', 'WHAT', 'WHO', 'WHY', 'HOW', 'US', 'YOU', 'ME', 'MAY', 'NOT', 'LET']
            print(len(exception_words))
            #f8.write("{\n")
            #f8.write("  'book: {},\n'".format(name))
            #f8.write("  'full: {},\n'".format(verse))
            
            #test = '"{}",'.format(verse)
            #test2 = test.rstrip(test[-1])
            #f9.write(test2)
            
            #f9.write("{")
            #f9.write("book:'{}',".format(name))
            #f9.write("full:'{}',".format(verse))
            
            #txt = txt + '{ ' + 'book: "{}", '.format(name) + 'full: "{}", '.format(verse) 
            txt = txt + ' "{}",'.format(verse).replace('\n', ' ').replace('\r', '')
            
            first = verse.split(' ') # verse split into words
            first2 = [] 
            first3 = []
            first4 = []
            dash_list = [] # For blank formed verse 
            first_letter_list = [] # For 1st letter formed verse 
            misc_list = [] # list to leave certain words visible
            
            for i in first:  
              if i[:1] not in '0123456789':    
                #dash_list = ["_" for x in i if x.isalpha()]
                for x in i:
                    if x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       dash_list.append('_')
                       first_letter_list.append('_')

                       if i.upper() in exception_words:
                          misc_list.append(x)
                          #print("{} ++++".format(i.upper())) 
                          #print("{} ++++".format(i in exception_words)) 
                       else:
                          misc_list.append('_')                              
                    else:
                       dash_list.append(x) 
                       first_letter_list.append(x)   
                       misc_list.append(x) 
                       
                       
            #Line Was for list comprehension, but didn't work out #dash_list = ["-" for x in i if x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
                
                # This line put 1st letter infront of blank line
                first_letter_list[:1] = i[:1]
                
                # This line for making blank words
                first2.append(''.join(dash_list))
                first2.append(' ')
                dash_list = []
                
                # This line for making 1st letter + blank words
                first3.append(''.join(first_letter_list))
                first3.append(' ')
                first_letter_list = []

                 # This line for making content with exception words being visible
                first4.append(''.join(misc_list))
                first4.append(' ')
                misc_list = []
              else:
                first2.append(i + ' ')
                first3.append(i + ' ')
                first4.append(i + ' ')
            
            first2.append('\n') 
            f2.write("{}\n".format(''.join(first2))) 
            f5.write("{}\n".format(''.join(first2))) 
            
            first3.append('\n') 
            f3.write("{}\n".format(''.join(first3))) 
            f4.write("{}\n".format(''.join(first3))) 
            
            #f9.write("first: '{}',".format(''.join(first3)))
            #f9.write("blank: '{}'".format(''.join(first2)))
            #f9.write("},")
            #f9.write("{ book_name: '{}',\n full: '{}',\n first: '{}',\n blank: '{}'\n }, \n".format(name, verse, ''.join(first3), ''.join(first2)))
            #txt = txt + 'first: "{}",'.format(''.join(first3)) + 'blank: "{}"'.format(''.join(first2))
            #txt = txt + " }, \n"
            txt2 = txt2 + '"{}",'.format(''.join(first2)).replace('\n', ' ').replace('\r', '')
            txt3 = txt3 + '"{}",'.format(''.join(first3)).replace('\n', ' ').replace('\r', '')
            txt4 = txt4 + '"{}",'.format(''.join(first4)).replace('\n', ' ').replace('\r', '')
        f7.write("</div>")    
        count = count + 1

        #txt = txt[:-1]
        #txt2 = txt2[:-1]
        #txt3 = txt3[:-1]
        #txt4 = txt4[:-1]
         
        txt = txt[:-1] + "];"
        txt2 = txt2[:-1] + "];"
        txt3 = txt3[:-1] + "];"
        txt4 = txt4[:-1] + "];"
        f9.write(txt)
        f9.write("\n")
        f9.write(txt2)
        f9.write("\n")
        f9.write(txt3)
        f9.write("\n")
        f9.write(txt4)
        f9.write("\n")
        

        #f9.write("\n") 

        f.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        f6.close()

        
    f7.write("</body></html>")
    f7.close()
    #f9.write("];")
    f9.close()

def verse_id(name, verse_string):
      st = verse_string.split(" ")
      n = st[0].replace(":", "-")
      return name + n


doc_maker(parser()) 
    


    
    


