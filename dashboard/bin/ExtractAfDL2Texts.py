#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import xml.etree.ElementTree as ET
import re
import codecs
import locale
reload(sys)
sys.setdefaultencoding("utf-8")

locale.setlocale(locale.LC_ALL, 'da_DK')

ns = {'xml': 'http://www.tei-c.org/ns/1.0'}
prefix = '{http://www.w3.org/XML/1998/namespace}'
divprefix = '{http://www.tei-c.org/ns/1.0}'

inputTextDir = 'xml/'
worksDir = 'AfDL2works/'

worksCatalog = open('AfDL2_catalog.txt', 'w')

keepNewlines = True

authName = None
authorName = None
thisWork = None
thisText = []
works = {}
workTypes = {}
workType = "misc"
workChapters = {}
inChapter = False
chapterText = []
chapterID = 0
dateInfo = "NA"

def bankChapter():

  global chapterText, chapterID, workChapters, inChapter

  if (not inChapter):
    print ("ERROR: not in a chapter!")
    return

  if (len(chapterText) == 0):
    print ("ERROR: empty chapter!")
    return

  if (keepNewlines):
    unsplitWords = "\n".join(chapterText)
    unsplitWords = ' '.join(unsplitWords.split(" "))
  else:
    unsplitWords = ' '.join(chapterText)
    unsplitWords = ' '.join(unsplitWords.split())

  workChapters[str(chapterID)] = unsplitWords

  chapterText = []
  inChapter = False

def writeChapters():

  global authorName, authName, thisWork, thisText, works, workType, workTypes, inChapter, chapterText, workChapters

  #workChapters = {}

  return

  authorString = authorName.replace(' ', '_').replace('/','_').replace(',', '')[0:20]
  if (not os.path.exists(worksDir + authorString)):
    os.mkdir(worksDir + authorString)

  for chapterID in workChapters:
    chapterText = workChapters[chapterID]

    chapterFileName = authorString + '_' + thisWork.replace(' ', '_').replace('/', '_')[0:20] + '_' + str(chapterID) + '.txt'

    if (not os.path.exists(worksDir + authorString + '/' + workType)):
      os.mkdir(worksDir + authorString + '/' + workType)
    if (not os.path.exists(worksDir + authorString + '/' + workType + '/chapters/')):
      os.mkdir(worksDir + authorString + '/' + workType + '/chapters/')

    print("writing chapter file " + worksDir + authorString + "/" + workType + '/chapters/' + chapterFileName)

    chapterFile = codecs.open(worksDir + authorString + "/" + workType + '/chapters/' + chapterFileName, 'w', 'utf-8')
    unsplitWords = ' '.join(chapterText)
    unsplitWords = ' '.join(unsplitWords.split())

    chapterFile.write(chapterText)

  #workChapters = {}

def writeWork(entity):

  global authorName, authName, thisWork, thisText, works, workType, workTypes, inChapter, chapterText, chapterID, dateInfo, worksCatalog

  writeChapters()
  inChapter = False
  chapterText = []

  return

  catData = [entity, authorName, thisWork, workType, dateInfo]
  worksCatalog.write("\t".join(catData) + "\n")

  authorString = authorName.replace(' ', '_').replace('/','_').replace(',', '')[0:20]
  if (not os.path.exists(worksDir + authorString)):
    os.mkdir(worksDir + authorString)

  workFileName = authorString + '_' + thisWork.replace(' ', '_').replace('/', '_')[0:20] + '.txt'

  workFile = codecs.open(worksDir + authorString + "/" + workFileName, 'w', 'utf-8')

  if (keepNewlines):
    unsplitWords = "\n".join(thisText)
    unsplitWords = ' '.join(unsplitWords.split(" "))
  else:
    unsplitWords = ' '.join(thisText)
    unsplitWords = ' '.join(unsplitWords.split())

  print("writing " + workFileName)

  workFile.write(unsplitWords)
  workFile.close()

  if (not os.path.exists(worksDir + authorString + '/' + workType)):
    os.mkdir(worksDir + authorString + '/' + workType)
  workFile = codecs.open(worksDir + authorString + "/" + workType + '/' + workFileName, 'w', 'utf-8')
  workFile.write(unsplitWords)
  workFile.close()

  writeChapters()
  inChapter = False
  chapterText = []

def parseBody(tBody, entity):

  global authName, authorName, thisWork, thisText, works, workType, inChapter, chapterText, chapterID

  workType = "misc"
  inChapter = False
  chapterText = []
  chapterID = 0

  for item in tBody.iter():
    #print(item.tag)
    #print("Looking at div item")

    divID = item.get(prefix + "id")
    if ((item.tag == divprefix + 'div') and (divID.find('workid') >= 0)):
      bibID = item.get('decls')
      #print("workID is " + divID + " and bibID is " + bibID)
      if ((thisWork != "") and (len(thisText) != 0)):
        writeWork(entity)
        if (inChapter):
          bankChapter()
          inChapter = False
          chapterText = []
        workType = "misc"

      if (bibID is not None):
        bibID = bibID.replace('#', '')
        if (bibID in works):
          thisWork = works[bibID]
          workTypes[bibID] = "misc"
          #print("Text is from sub-work " + thisWork)
          thisText = []

    # Parsing strategies:
    # These are poems:
    # If a section begins with a <lg> tag, everything in a <l> tag below it
    # is text; maybe include <head> elements as well (this is usually titles).
    elif (item.tag == divprefix + 'lg'):
      if (workType != "drama"):
        workType = "poems"
      poemLG = item
      for lgItem in poemLG.iter():
        if (lgItem.tag == divprefix + 'l'):
          lIter = lgItem.itertext()
          for lText in lIter:
            thisText.append(lText.encode('utf-8'))
            if (inChapter):
              chapterText.append(lText.encode('utf-8'))

    # These tend to be monographs:
    # If a <div> is followed immediately by a <p>, just count all <p> sections
    # as text.
    # But if the <div> includes a type="chapter" n="1" then count everything
    # in <p> sections as text, and divide the book into chapters if desired
    elif (item.tag == divprefix + 'p'):
      if (workType != "drama"):
        workType = "monographs"
      textP = item
      pIter = textP.itertext()
      for pText in pIter:
        thisText.append(pText.encode('utf-8'))
        if (inChapter):
          chapterText.append(pText.encode('utf-8'))

    elif ((item.tag == divprefix + 'div') and (item.get('type') is not None) and (item.get('type') == 'chapter')):
      bankChapter()
      if (item.get('n') is None):
        #print("Empty chapter number")
        if (isinstance(chapterID, ( int, long ) )):
          chapterID += 1
        else:
          chapterID = 1
      else:
        #print("chapter number is " + item.get('n'))
        chapterID = item.get('n')
      inChapter = True
      chapterText = []

    # What about plays:
    # Most material falls inside <sp> tags; the speaker is identified in a
    # nested <speaker> tag, with the spoken text in a following <p> tag.
    # Stage directions are in a separate, following <stage> tag.
    # Introductory material (scene-setting descriptions, etc.) are in
    # separate <p> tags, but can be ignored if we're focusing on dialogue.
    elif (item.tag == divprefix + 'stage'):
      workType = "drama"

    elif (item.tag == divprefix + 'sp'):
      workType = "drama"
      #playSP = item
      #for spItem in playSP.iter():
      #  if (spItem.tag == divprefix + 'p'):
      #    pIter = spItem.itertext()
      #    for pText in pIter:
      #      thisText.append(pText.encode('utf-8'))
      #      if (inChapter):
      #        chapterText.append(pText.encode('utf-8'))
    workTypes[workID] = workType

  return workTypes


def parseFile(entity):

  global works, authorName, authName, thisWork, thisText, works, workType, inChapter, chapterText, chapterID, dateInfo

  print("parsing " + entity)

  thisText = []
  thisWork = None
  authorName = None
  authName = None
  works = {} # List of biblid => title mappings for the sub-works in this file
  workTypes = {}
  inChapter = False
  chapterText = []
  chapterID = 0
  dateInfo = "NA"

  filePath = inputTextDir + entity
  if os.path.isfile(filePath):
    print "Parsing from " + filePath
    # Probably should check to make sure it has XML inside, not PDF...
    #if (True):
    tsTitle = None
    tsAuthor = None

    fTree = ET.parse(filePath)
    if (fTree is None):
      print "ERROR: cannot build XML tree for " + entity
      return None

    fRoot = fTree.getroot()

    fHeader = fRoot.find('xml:teiHeader', ns)

    fDesc = fHeader.find('xml:fileDesc', ns)

    titleStatement = fDesc.find('xml:titleStmt', ns)

    if (titleStatement is not None):
      tsTitle = titleStatement.find('xml:title', ns).text
      tsAuthor = titleStatement.find('xml:author', ns).text

    #print("title statement title is " + tsTitle + ", author is " + tsAuthor)

    pubStatement = fDesc.find('xml:publicationStmt', ns)

    if (pubStatement is not None):
      # NOTE: this often contains a pub date (YYYY), though it could be
      # for an entire anthology, rather than the works it contains
      psPublisher = pubStatement.find('xml:publisher', ns).text

    # Also parse the sourceDesc? Seems somewhat redundant...
    sDesc = fDesc.find('xml:sourceDesc', ns)

    if (tsAuthor is not None):
      authorName = tsAuthor
      authName = tsAuthor
    else:
      authorName = None
      authName = None

    if (sDesc is not None):
      bibInfo = sDesc.find('xml:bibl', ns)
      if (bibInfo is not None):
        authorInfo = bibInfo.find('xml:author', ns)
        if (authorInfo is not None):
          aName = authorInfo.find('xml:name', ns)
          if (aName is not None):
            surnameElt = aName.find('xml:surname', ns)
            if (surnameElt is not None):
              authorSurname = surnameElt.text
            else:
              authorSurname = ""
            authorForename = aName.find('xml:forename', ns).text
            if (authorSurname == ""):
              authorName = authorForename
              authName = authorForename
            else:
              authorName = authorSurname + " " + authorForename
              authName = authorSurname + "_" + authorForename
        titleElt = bibInfo.find('xml:title', ns)
        if (titleElt is not None):
          titleInfo = ' '.join(titleElt.text.replace("\n", " ").split(' '))
        else:
          titleInfo = "NA"
        dateElt = bibInfo.find('xml:date', ns)
        if (dateElt is not None):
          dateInfo = dateElt.text

        print("title from bib is " + titleInfo + ", author name is " + authorName + ", pub date is " + dateInfo)
        thisWork = titleInfo

      # Probably should iterate through the bibList; the item biblid elements
      # can be used to detect new works in the body text
      bibList = sDesc.find('xml:listBibl', ns)

      if (bibList is not None):
        for bibl in bibList.findall('xml:bibl', ns):
          #print(bibl.attrib)
          workID = bibl.get(prefix + 'id')
          #print(workID)
          workTitleElt = bibl.find('xml:title', ns)
          if (workTitleElt is not None):
            workTitle = workTitleElt.text
            works[workID] = workTitle

    fText = fRoot.find('xml:text', ns)

    if (fText is None):
      print("Unable to find text, skipping ")
      return

    tFront = fText.find('xml:front', ns)
    # Maybe parse titlePage for docAuthor, docTitle, docImprint -- but it's
    # probably in the source description above

    thisText = []

    # <text> tags can also mark the beginning of a work
    for textItem in fText.iter():

      textID = textItem.get(prefix + "id")
      if ((textItem.tag == divprefix + 'text') and (textID.find('workid') >= 0)):
        bibID = textItem.get('decls')
        if (bibID is not None):
          bibID = bibID.replace('#', '')
          if (bibID in works):
            if ((thisWork != "") and (len(thisText) != 0)):
              writeWork(entity)
              if (inChapter):
                bankChapter()
                inChapter = False
                chapterText = []
              workType = "misc"

            thisWork = works[bibID]
            #print("Text is from sub-work " + thisWork)
            thisText = []

      elif (textItem.tag == divprefix + 'body'):
        bodyWorks = parseBody(textItem, entity)
        for bWorkID in bodyWorks:
          workTypes[bWorkID] = bodyWorks[bWorkID]


    #else:
    #  for tGroup in fText.findall('xml:group', ns):
    #  #tGroup = fText.find('xml:group', ns)
    #    if (tGroup is not None):
    #      tText2 = tGroup.find('xml:text', ns)
    #      if (tText2 is not None):
    #        print("tText2 is not None, ID is " + tText2.get(prefix + "id"))
    #        tBody = tText2.find('xml:body', ns)
    #        if (tBody is None):
    #          tGroup2 = tText2.find('xml:group', ns)
    #          if (tGroup2 is not None):
    #            tText3 = tGroup2.find('xml:text', ns)
    #            if (tText3 is not None):
    #              tBody = tText3.find('xml:body', ns)
    #        if (tBody is None):
    #          print("unable to find text body, skipping")
    #        else:
    #          parseBody(tBody)

    tBack = fText.find('xml:back', ns) # Probably should skip

    #print("thisWork is " + thisWork + ", length of this text is " + str(len(thisText)))

    if ((thisWork != "") and (len(thisText) != 0)):
      #writeWork(authName, thisWork, thisText)
      writeWork(entity)
      if (inChapter):
        bankChapter()
        inChapter = False
    else:
      print("WARNING: empty work title or text")

  return [works, workTypes]

#parseFile('heibergjl04val.xml')
#sys.exit()

#XMLDirFiles = os.listdir(inputTextDir)
#for entity in XMLDirFiles:

  #grundtvig01val.xml

newTSVFile = open('metadata_adl_genres.txt', 'w')

with open('metadata/metadata_adl.tsv', 'r') as mFile:

  for line in mFile:

    lineA = line.strip().split("\t")
    objID = lineA[0]

    if (objID == 'file_id'):
      newTSVFile.write(line.strip() + "\tgenre\n")
      continue

    print("objID", objID)

    authorID = objID.split("_workid")[0]
    workID = objID.split("_workid")[1]

    volumeTitle = lineA[3]

    mFileName = authorID + '.xml'

    print("workID",workID)

    workType = "misc"
    [theseWorks, theseTypes] = parseFile(mFileName)
    #print(theseWorks)
    #print(theseTypes)

    thisID = 'biblid' + workID

    if (thisID in theseTypes):
      thisType = theseTypes[thisID]
      print("workID",thisID,"found, type is",thisType)
    else:
      print("workID not found",thisID)

    if (thisID in theseWorks):
      thisWork = theseWorks[thisID]
      print("workID",thisID,"found, title is",thisWork)

      #lowerWork = thisWork.lower()
      lowerWork = volumeTitle.lower()

      if ((lowerWork.find('digt') >= 0) or (lowerWork.find('lyrik') >= 0) or (lowerWork.find('sang') > 0) or (lowerWork.find('epistl') >= 0)): # lyrik, sang, epistler
        workType = "poems"
        print("work title",thisWork,"type set to",workType)

      elif ((lowerWork.find('novel') >= 0) or (lowerWork.find('fortæl') >= 0)):
        workType = 'short fiction'
        print("work title",thisWork,"type set to",workType)
      
      elif (lowerWork.find('forspil') >= 0):
        workType = 'drama'
        print("work title",thisWork,"type set to",workType)
    else:
      print("workID not found in works",thisID)

    newTSVFile.write(line.strip() + "\t" + workType + "\n")


  #if (not entity.endswith('.xml')):
  #  #print("Entity name does not end with xml")
  #  continue

  #if (entity.find('tom') >= 0):
  #  #print(entity + " seems to be a facsimile catalog rather than a text. Skipping.")
  #  continue

  #workType = parseFile(entity)
  #sys.exit()
