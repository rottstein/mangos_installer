#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 

import time
import os

def fetch_git(self,link):
    for line in os.popen('cd '+self.work_dir+ ';git clone '+link+'').readlines():
           print line

def fetch_mangchat(self,link):
    print os.system("cd "+self.work_dir+"/server;git add .;git commit -a -m 'Commiting current work before fetching.'")
    print os.system('cd '+self.work_dir+'/server;git pull '+str(link))

def fetch_svn(self,install_dir,link,version):
    os.system('cd '+install_dir+'/database/;svn co '+link+'')
    if self.checkFolder(install_dir+'/database/'+version)==1:
       print self.colored("\nSVN: "+link,'green')
       print self.colored("\nSuccesfully downloaded!",'green')
    else:
       print self.colored("\nError: Failed to download from: "+link,'red')
       print self.colored("\nScript will continue!",'red')
       time.sleep(5)

def fetch_custom_git(self):
     pass

def fetch_scriptdev2(self,link,version):
    if version=='tbc':
       folder='scripts'
    elif version=='classic':
       folder='ScriptDevZero'
    elif version=='cata':
       folder='ScriptDev2'
    elif version=='wotlk':
       folder='ScriptDev2'
    for line in os.popen('cd '+self.work_dir+ '/server;git clone '+link+' src/bindings/'+folder).readlines():
           print line

def fetch_database(self,install_dir,link,version):
       print self.colored("\nFetching MaNGOS "+version+" Default database... ("+link+")",'green')
       os.system('mkdir '+install_dir+'/database;cd '+install_dir+'/database')
       for line in os.popen('cd '+install_dir+'/database/;git clone '+link):
           if os.path.exists(install_dir+'/database/database'):
              print "\nDone fecthing default database."
