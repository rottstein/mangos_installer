#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 

import os
import platform
from Collect import fetch_svn, fetch_git, fetch_custom_git, fetch_scriptdev2, fetch_database
from DatabaseSetup import check_Database, MaNGOS_Database
from MaNGOS import Cataclysm, Wotlk, TBC, Classic
from InstallDep import Install_dep
from Lang import welcome

new_path=''

class installer:
  def __init__(self,work_dir,backup_dir,log_file):

      self.work_dir=work_dir
      self.backup_dir=backup_dir
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

      # MaNGOS Support
      self.Cataclysm=Cataclysm
      self.Wotlk=Wotlk
      self.TBC=TBC
      self.Classic=Classic

      # TrinityCore Support // Might not be used!

      # ArcEmu Sopport // -ss-

  def mkdir(self,path):
      os.system('mkdir '+path)
      if self.checkFolder(path)==1:
         self.msg("\nPath: "+path+" Succesfully Created!")
      else:
         self.msg("\nError: Failed to create path: "+path)

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
         self.msg("\n OS check: "+str(os[0])+", "+str(os[1])+" - "+str(os[2])+" - [ok]")
      else:
         self.msg("\nOS: "+os[0])
         self.msg("\nThis script is only for Ubuntu users! Quitting!")
         exit()

  def del_folder(self,dir):
      if os.path.exists(dir):
         self.msg("\nTheres already a folder by that name, you want to rename or delete it? ("+dir+")")
         self.msg('Syntax: rename/del')
         del_current=self.Quest('Select: ')
         if del_current=='rename':
            os.system('mv '+dir+' '+dir+'_backup')
         elif del_current=='del':
            os.system('rm -rf '+dir)
         else:
            self.msg("\nPlease Delete or move your current files in path: "+dir)
            print os.system('ls -la '+dir)
            exit()

  def msg(self,msg):
      print msg

  def checkVersion(version):
      return version, scriptdev2

  def main(self):
    try:
        print self.welcome()
        self.checkOS()
    except:
        self.msg("\nError: Script ended! - Please Check "+self.log_file+"..")
        exit()

    self.msg("\nDo you wish to Proceed?")
    q=self.Quest(0)
    if q=='yes':
       self.Install_dep(self)
    else:
       exit()

    self.msg("\nChoose witch version to install?\nSyntax: Cataclysm / Wotlk / TBC / Classic / quit")
    version=self.Quest('Please enter your choise: ')

    if version=='cataclysm':
        self.Cataclysm(self)
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
      
