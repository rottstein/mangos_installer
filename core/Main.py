#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 

import os
import platform
from Collect import fetch_svn, fetch_git, fetch_custom_git, fetch_scriptdev2, fetch_database
from DatabaseSetup import check_Database, MaNGOS_Database
from InstallDep import Install_dep
from Lang import welcome

new_path=''

class installer:
  def __init__(self,work_dir,log_file):

      self.work_dir=work_dir
      self.log_file=log_file
      self.welcome=welcome
      self.Install_dep=Install_dep

      # Collect SVN / GIT 
      self.fetch_svn=fetch_svn
      self.fetch_git=fetch_git
      self.fetch_custom_git=fetch_custom_git
      self.fetch_scriptdev2=fetch_scriptdev2
      self.fetch_database=fetch_database

      # Database
      self.check_Database=check_Database
      self.MaNGOS_Database=MaNGOS_Database

  def mkdir(self,path):
      os.system('mkdir '+path)
      if self.checkFolder(path)==1:
         print "\nPath: "+path+" Succesfully Created!"
      else:
         print "\nError: Failed to create path: "+path

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

  def checkOS(self):
      os=platform.dist()
      if os[0]=='Ubuntu':
         print "\n OS check: "+str(os[0])+", "+str(os[1])+" - "+str(os[2])+" - [ok]"
      else:
         print "\nOS: "+os[0]
         print "\nThis script is only for Ubuntu users! Quitting!"
         exit()

  def checkVersion():
      pass

  def main(self):
    try:
        print self.welcome()
        self.checkOS()
    except:
        print "\nError: Script ended! - Please Check "+self.log_file+".."
        exit()

    print "\nProceed?"
    q=self.Quest(0)
    if q=='yes':
       self.Install_dep(self)
    else:
       exit()

    print "\nChoose witch version to install?\nSyntax: Cataclysm / Wotlk / TBC / Classic / quit\n"
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

    
      #print "Work Path: "+self.work_dir
      #print "Log File: "+self.log_file
      #if self.checkFolder(self.work_dir)==1:
      #   print "\nError: Please Delete "+self.work_dir+" or rename it!\n"
      #   exit()
      #else:
      #   self.mkdir(self.work_dir)
      
