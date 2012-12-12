#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 
import os, subprocess

packages=['build-essential',
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
          'screen']

def checkPackage(package):
    devnull = open(os.devnull,"w")
    retval = subprocess.call(["dpkg","-s",""+package+""],stdout=devnull,stderr=subprocess.STDOUT)
    devnull.close()
    if retval != 0:
       print "Installing Package: "+package
       os.system('sudo apt-get install '+package)
    else:
       print "Package: "+package+" ---- [OK]."

def Install_dep(self):
    for package in packages:
        checkPackage(package)
