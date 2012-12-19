#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 

import time
import os

def fetch_git(self,link):
    self.check_connectivity('https://github.com/')
    self.msg('\nFetching '+str(link)+'\n','green')
    for line in os.popen('cd '+self.work_dir+ ';git clone '+link+'').readlines():
           print line

def fetch_mangchat(self,link):
    print os.system("cd "+self.work_dir+"/server;git add .;git commit -a -m 'Commiting current work before fetching.'")
    print os.system('cd '+self.work_dir+'/server;git pull '+str(link))

def fetch_svn(self,link,version):
    os.system('mkdir '+self.install_dir+'/database;cd '+self.install_dir+'/database')
    self.check_connectivity('http://subversion.assembla.com/')
    os.system('cd '+self.install_dir+'/database/;svn co '+link+'')
    if self.checkFolder(self.install_dir+'/database/'+version)==1:
       print self.colored("\nSVN: "+link,'green')
       print self.colored("\nSuccesfully downloaded!",'green')
    else:
       print self.colored("\nError: Failed to download from: "+link,'red')
       exit()

def fetch_custom_git(self,path,link):
    for line in os.popen('cd '+path+';git clone '+link+'').readlines():
           print line

def fetch_scriptdev2(self,link,version):
    if version=='tbc':
       vers='mangos-tbc'
       folder='scripts'
    elif version=='classic':
       vers='mangos-classic'
       folder='ScriptDevZero'
    elif version=='cata':
       vers='server'
       folder='ScriptDev2'
    elif version=='wotlk':
       vers='mangos-wotlk'
       folder='ScriptDev2'
    self.check_connectivity('https://github.com/')
    self.msg('\nFetching '+str(link)+'\n','green')
    for line in os.popen('cd '+self.work_dir+ '/'+vers+';git clone '+link+' src/bindings/ScriptDev2').readlines():
           print line

def fetch_database(self,link,version):
       self.check_connectivity('https://github.com/')
       self.msg('\nFetching '+str(link)+'\n','green')
       print self.colored("\nFetching MaNGOS "+version+" Default database... ("+link+")",'green')
       os.system('mkdir '+self.install_dir+'/database;cd '+self.install_dir+'/database')
       for line in os.popen('cd '+self.install_dir+'/database/;git clone '+link):
           if os.path.exists(self.install_dir+'/database/database'):
              print "\nDone fecthing default database."
