#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 
import os, subprocess, time, sys

packages=[
          'build-essential',
          'gcc',
          'g++',
          'automake',
          'git-core',
          'autoconf',
          'make',
          'patch',
          'libmysql++-dev',
          'mysql-server',
          'libtool',
          'libssl-dev',
          'grep',
          'binutils',
          'zlibc',
          'libc6',
          'libbz2-dev',
          'cmake',
          'subversion',
          'phpmyadmin',
          'screen'
         ]

def checkPackage(self,package):
    devnull = open(os.devnull,"w")
    retval = subprocess.call(["dpkg","-s",""+package+""],stdout=devnull,stderr=subprocess.STDOUT)
    devnull.close()
    if retval != 0:
       self.msg("\nInstalling Package: "+package,'red')
       os.system(self.cmd_install+' '+package)
    else:
       self.msg('Package: '+self.colored(package,'yellow')+' '+self.colored('[OK]','green')+'', 'green')

def Install_dep(self):
    self.msg('\nChecking needed files.','green')
    for package in packages:
        checkPackage(self,package)
