mangos_installer
================

Just another lazy mand script, for a automated install. ;)

needed files: python-MySQLdb
syntax: sudo apt-get install python-MySQLdb

then just run script syntax: python setup.py

Features:
Download and compile MaNGOS and Scriptdev2

           Cataclysm:
           Core: MangChat 1.7.8

This script will install the following packages 

##################################################

          *build-essential 
          *gcc 
          *g++ 
          *automake 
          *git-core 
          *autoconf 
          *make 
          *patch 
          *libmysql++-dev 
          *mysql-server 
          *libtool 
          *libssl-dev 
          *grep 
          *binutils 
          *zlibc 
          *libc6 
          *libbz2-dev 
          *cmake 
          *subversion 
          *phpmyadmin
          *screen

##########################################
Current ChangeLog

            Changelog:

            version 1.5
            complete rewrite
            Cataclysm working
            set realm info
            setup databases
            check & backup current dbs
            option to use current realm db (in case of multiple realms)
            acid working
            and much more..
 
            version 1.0
            Script simplyfied
            fixed alot of typo's
            removed log function
            add svn for acid/ytdb/udb
            new option for AuctionHouseBot since its precompiled into the core
            new option fireup server when done
            show all needed info at the end of the install
            new function Quest(0) helps make the script abit more clean

            TODO:
            Fixing Mangos-zero scriptdevzero patch (note. it will download and compile mangos-zero just whitout the sdz part..)
            Finde correct version sd2 for wotlk
            Update MaNGOS_Database() to setup udb and ytdb for wotlk 

##########################################################



