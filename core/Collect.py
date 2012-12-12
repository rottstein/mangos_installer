#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 

import time

def fetch_git(self,work_dir,link):
    for line in os.popen('cd '+work_dir+ ';git clone '+link+'').readlines():
           print line

def fetch_svn(self,install_dir,link,version):
    os.system('cd '+install_dir+'/database/;svn co '+link+'')
    if self.checkFolder(install_dir+'/database/'+version)==1:
       print "\nSVN: "+link
       print "\nSuccesfully downloaded!"
    else:
       print "\nError: Failed to download from: "+link
       print "\nScript will continue!"
       time.sleep(5)

def fetch_custom_git(self):
     pass

def fetch_scriptdev2(self,work_dir,link,version):
    if version=='tbc':
       folder='scripts'
    elif version=='classic':
       folder='ScriptDevZero'
    elif version=='cata':
       folder='ScriptDev2'
    elif version=='wotlk':
       folder='ScriptDev2'
    for line in os.popen('cd '+work_dir+ '/server;git clone '+link+' src/bindings/'+folder).readlines():
           print line

def fetch_database(install_dir,link,version):
       print "\nFetching MaNGOS "+version+" Default database... ("+link+")"
       os.system('mkdir '+install_dir+'/database;cd '+install_dir+'/database')
       for line in os.popen('cd '+install_dir+'/database/;git clone '+link):
           if os.path.exists(install_dir+'/database/database'):
              print "\nDone fecthing default database."
