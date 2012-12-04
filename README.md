mangos_installer
================

Just another lazy mand script, for a automated install. ;)

Just run script syntax: python MaNGOS.py

Features:
Download and compile MaNGOS and Scriptdev2
automated database setup for MaNGOS and ScriptDev2

 Cataclysm:
           Core: MangChat 1.7.8
                 TeleNPC Core Patch
                 Max Level & Stackable Core

           ScriptDev2:
                 Item Summon
                 TeleNPC 2
                 LevelNPC
                 ProfessionNPC

 TBC:
          Database:
                 ACID auto setup

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

Changelog: 
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
old logs
version 0.2

*fix some typo's
*rewrite log function
*add automated Database setup (so far only for Cataclysm not sure if this works whit wotlk,tbc,classic and only default database)
*all input moved to raw_input() (no need to edit MaNGOS.py)

needs fixing:

*log function
*update section
*database function



