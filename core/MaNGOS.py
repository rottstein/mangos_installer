#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 
import os
from InstallDep import Install_dep
from Lang import welcome

new_path=''

class installer:
  def __init__(self,work_dir,log_file):

      self.work_dir=work_dir
      self.log_file=log_file
      self.welcome=welcome
      self.Install_dep=Install_dep

  def mkdir(self,path):
      os.system('mkdir '+path)
      if self.checkFolder(path)==1:
         print "Path: "+path+" Succesfully Created!"
      else:
         print "Error: Failed to create path: "+path

  def checkFolder(self,path):
      if os.path.exists(path):
         return 1
      else:
         return 0

  def Quest(self,question):
      if question==0:
         question='Select: '
      else:
         question=question
      answer=raw_input(question)
      return answer

  def main(self):
    try:
        print self.welcome()
    except:
        print "Error: Script ended! - Please Check "+self.log_file+".."
        exit()

    print "\nProceed?"
    q=self.Quest(0)
    if q=='yes':
       self.Install_dep(self)
    else:
       exit()

    print "\nChoose witch version to install?\n Syntax: Cataclysm / Wotlk / TBC / Classic / quit\n"
    version=self.Quest('Please enter your choise: ')

    if version=='cataclysm':
        self.Cataclysm()
    elif version=='wotlk':
        self.Wotlk()
    elif version=='tbc':
        self.TBC()
    elif version=='classic':
        self.Classic()
    elif version=='quit':
       exit()
    else:
      print "\nError: Syntax error!"
      exit()


      # syntax_error('Cataclysm/Wotlk/TBC/Classic/quit')
      # restart_script()      
      #print "Work Path: "+self.work_dir
      #print "Log File: "+self.log_file
      #if self.checkFolder(self.work_dir)==1:
      #   print "\nError: Please Delete "+self.work_dir+" or rename it!\n"
      #   exit()
      #else:
      #   self.mkdir(self.work_dir)
      
