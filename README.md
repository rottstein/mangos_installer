mangos_installer
================

MaNGOS Installer all written in python.
Tested on Ubuntu 12.04.
should work for debian users to, it will NOT work for windows user yet. (in development)

Script Features:
##########################################
* Download MaNGOS & ScriptDev2 & ACID
* Compile MaNGOS & ScriptDev2
* Setup Databases
* Edit Config files
* Create new Account & set gmlevel
* Update Current realm if needed
* Install all needed files
* Include AuctionHouseBot
* Include MangChat (Cataclysm Only)
* Start up servers (mangosd & realmd)

This script will download and compile MaNGOS including setting up database.
i basicly did because i grow tired of repeating my self. a lazy mands work ;)
the script collect all the needed info to setup core and edit conf files and databases.
it also comes whit a predefines allowing you to skip the Quest part and make it abit faster.

Current DB setup leaves you whit.
Cataclysm:
##########################################
          *DB Version: UDB 0.12.2 (405) for MaNGOS 12111 with SD2 SQL for rev. 2712
          *Acid Version: ACID 4.0.0 ALPHA DEVELOPMENT - Full Release for MaNGOS (4.3.4 Client) 
          *ScriptDev2 Version: ScriptDev2 (for MaNGOS 12026+)
##########################################


Wrath of the lich king:
##########################################
          *DB Version: YTDB_0.14.6_R630_MaNGOS_R12214_SD2_R2737_ACID_R310_RuDB_R56
          *Acid Version: ACID 3.1.0 'Another Wild Adventure' - Full Release for CMaNGOS (3.3.5a Client)
          *ScriptDev2 Version: ScriptDev2 (for C-MaNGOS 12316+)
##########################################

The Burning Crusaders:
##########################################
          *DB Version: TBC-DB 1.0.0 for MaNGOSOne s1725 and ScriptDevOne s2628
          *Acid Version: ACID 2.0.7 'Another Wild Adventure' - Full Release for MaNGOS (2.4.3 Client)
          *ScriptDev2 Version: ScriptDev2 (for C-MaNGOS s1846+)
##########################################

Cataclysm uses mangos/server as its main repo, and Wotlk and TBC is running of cmangos. if you rather use mangos repo simply open core/MaNGOS.py and edit the links in the top. :)
i will implemte a function to choose between cmangos and mangos on a later time.. but first of all i need to put the the last part of the mangos part (Classic - Mangos-zero)

How to:
##########################################
          open terminal
          cd ~/
          git clone git://github.com/gimli/mangos_installer.git
          cd mangos_installer
          sudo apt-get install python-mysqldb (Debian: apt-get install python-mysqldb)
          python setup.py
##########################################
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
            
            version 2.0
            written in class functions using self. to keep info stored in all functions
            new options.
            edit mangos configurations files (*.conf)
            colored output
            alot of fixes
            Cataclysm, Wrath Of The Lich King & The Burning Crusaders (Working.)
            system/network check
            multiple realm (Edit current realm Database instead of setting up a new one)
            create new account
            set gmlevel
            load servers
            etc..

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

##########################################################

TODO
##########################################
            TODO:
            *FIX Database backup
            *Add afew check along the realm database update function
            *Add log function
            *Add Classic support (mangos-zero)
            *Add Custom Patch function for all clients (in the feature, needs alot of work.)
            *ect..  
##########################################
