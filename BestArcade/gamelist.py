# -*- coding: utf-8 -*-
import os.path

def init(outputDir):
    gamelist = open(os.path.join(outputDir,"gamelist.xml"),'w',encoding="utf-8")
    gamelist.write('<?xml version="1.0"?>\n')
    gamelist.write("<gameList>\n")
    return gamelist

def writeGamelistHiddenEntry(gamelist,romName,genre,useGenreFolder) :
    romPath = (genre + "/" + romName) if useGenreFolder else romName
    gamelist.write("    <game>\n")
    gamelist.write("        <path>./"+romPath+"</path>\n")
    gamelist.write("        <hidden>true</hidden>\n")    
    gamelist.write("    </game>\n")

def writeGamelistEntry(gamelist,romName,name,desc,year,frontPic,developer,publisher,genre,useGenreFolder):
    romPath = (genre + "/" + romName) if useGenreFolder else romName
    gamelist.write("    <game>\n")
    gamelist.write("        <path>./"+romPath+"</path>\n")
    gamelist.write("        <name>"+name+"</name>\n")
    gamelist.write("        <desc>"+desc+"</desc>\n")    
    gamelist.write("        <releasedate>"+year+"0101T000000</releasedate>\n")
    gamelist.write("        <image>"+frontPic+"</image>\n")
    gamelist.write("        <developer>"+developer+"</developer>\n")
    gamelist.write("        <publisher>"+publisher+"</publisher>\n")
    gamelist.write("        <genre>"+genre+"</genre>\n")
    gamelist.write("    </game>\n")
    
def close(gamelist) :
    gamelist.write("</gameList>\n")
    gamelist.close()
    