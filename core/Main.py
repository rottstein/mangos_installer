#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 

import os
import platform
import fileinput
import sys
import time
import ctypes
from time import localtime, strftime
from termcolor import colored
from Menu import info
from predefines import loadPreDefines
from Collect import fetch_svn, fetch_git, fetch_mangchat, fetch_custom_git, fetch_scriptdev2, fetch_database
from DatabaseSetup import check_Database, backupDB, MaNGOS_Database, updateRealm, setupRealm, setupChar, setupScriptDev2
from MaNGOS import Cataclysm, Wotlk, TBC, Classic
from InstallDep import Install_dep
from Lang import welcome, Complete, Correct, Correct_w

new_path=''

class installer:
  def __init__(self,work_dir,backup_dir,log_file,cmd_install):

      # Div.
      self.work_dir=work_dir
      self.backup_dir=backup_dir
      self.log_file=log_file
      self.welcome=welcome
      self.Complete=Complete
      self.Install_dep=Install_dep
      self.cmd_install=cmd_install
      self.colored=colored
      self.info=info
      self.Correct=Correct
      self.Correct_w=Correct_w
      self.loadPreDefines=loadPreDefines

      # Collect SVN / GIT 
      self.fetch_svn=fetch_svn
      self.fetch_git=fetch_git
      self.fetch_mangchat=fetch_mangchat
      self.fetch_custom_git=fetch_custom_git
      self.fetch_scriptdev2=fetch_scriptdev2
      self.fetch_database=fetch_database

      # Database
      self.check_Database=check_Database
      self.backupDB=backupDB
      self.MaNGOS_Database=MaNGOS_Database
      self.updateRealm=updateRealm
      self.setupRealm=setupRealm
      self.setupChar=setupChar
      self.setupScriptDev2=setupScriptDev2

      # MaNGOS Support
      self.Cataclysm=Cataclysm
      self.Wotlk=Wotlk
      self.TBC=TBC
      self.Classic=Classic

      # TrinityCore Support // Might not be used!

      # Skyfire Emu Support // -ss-

      # ArcEmu Sopport // -ss-

  def mkdir(self,path):
      os.system('mkdir '+path)
      if self.checkFolder(path)==1:
         self.msg("\nPath: "+path+" Succesfully Created!",'green')
      else:
         self.msg("\nError: Failed to create path: "+path,'red')

  def checkFolder(self,path):
      if os.path.exists(path):
         return 1
      else:
         return 0

  def Quest(self,question):
      if question==0:
         question=self.colored('Select: ','yellow')
      else:
         question=question
      answer=raw_input(question)
      return answer

  def checkOS(self):
      bit=ctypes.sizeof(ctypes.c_voidp)
      if bit==8:
         bit='64bit'
      else:
         bit='32bit'
      os=platform.dist()
      self.msg('\nChecking OS Platform.','yellow')
      if os[0]=='Ubuntu':
         time.sleep(3)
         self.msg("\nFound OS: "+str(os[0])+", "+str(os[1]),'green') 
         self.msg("Version: "+str(os[2]),'green')
         self.msg('32/64Bit: '+str(bit),'green')
         self.msg('\nSystem check '+self.colored('[OK]','green'),'yellow')
         time.sleep(1)
      else:
         self.msg("\nOS: "+os[0]+" is currently not supported!",'red')
         self.msg("\nThis script is only for Ubuntu users! Quitting!",'red')
         exit()

  def del_folder(self,dir):
      if os.path.exists(dir):
         date=strftime("%Y_%m_%d ", localtime())
         self.msg("\nTheres already a folder by that name, you want to rename or delete it? ("+dir+")",'red')
         self.msg('Syntax: rename/del','red')
         del_current=self.Quest(self.colored('Select: ','yellow'))
         if del_current=='rename':
            os.system('mv '+dir+' '+dir+'_backup_'+date)
         elif del_current=='del':
            os.system('rm -rf '+dir)
         else:
            self.msg("\nPlease Delete or move your current files in path: "+dir,'red')
            print os.system('ls -la '+dir)
            exit()

  def replaceAll(self,file,searchExp,replaceExp):
      for line in fileinput.input(file, inplace=1):
          if searchExp in line:
             line = line.replace(searchExp,replaceExp)
          sys.stdout.write(line)

  def msg(self,msg,color):
      print self.colored(msg,color)

  def loadServer(self):
      self.shit='test'

  def checkVersion(version):
      return version, scriptdev2

  def createAccount():
      pass

  def main(self):
    try:
        print self.colored(self.welcome(),'green')
        self.checkOS()
        #self.loadServer()
    except:
        self.msg("\nError: Script ended! - Please Check "+self.log_file+"..",'red')
        exit()

    self.msg('\nDo you wish to Proceed?','green')
    q=self.Quest(0)
    if q=='yes':
       pass
    else:
       exit()

    self.msg('\nChoose witch version to install?\nSyntax: Cataclysm / Wotlk / TBC / Classic / quit','green')
    version=self.Quest(self.colored('Please enter your choise: ','yellow'))

    if version=='cataclysm':
        self.version='cataclysm'
        self.Install_dep(self)
        self.Cataclysm(self)
    elif version=='wotlk':
        self.version='wotlk'
        self.Install_dep(self)
        self.Wotlk(self)
    elif version=='tbc':
        self.Install_dep(self)
        self.TBC()
    elif version=='classic':
        self.Install_dep(self)
        self.Classic()
    elif version=='quit':
       exit()
    else:
      print "\nError: Syntax error!"
      exit()      
