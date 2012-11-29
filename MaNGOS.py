#!/usr/bin/env python
# Ubuntu Script tested on 12.04
# MaNGOS python installer for newbies
# working whit lastest rev. (4.3.4) 
# should work for wotlk/tbc/classic to
# syntax: python MaNGOS.py
# first options:
# syntax: clean (clean install)
# syntax: update (update current source)
# syntax: quit (end script)
# Script does still need alot of work but,
# it will install download a clean copy of mangos

import os, re
from time import localtime, strftime

#############################################
# MaNGOS Install Config -                   #
#############################################

# Cataclysm
git_mangos='git://github.com/mangos/server.git'
git_scriptdev2='git://github.com/mangos/scripts.git'
git_acid='git://github.com/scriptdev2/acid.git'
git_database='git://github.com/mangos/database.git'

# Wotlk
git_mangos_wotlk='git://github.com/mangos-wotlk/server.git'
git_scriptdev2_wotlk='git://github.com/scriptdev2/scriptdev2.git'
svn_udb_wotlk='http://unifieddb.svn.sourceforge.net/'
svn_ytdb_wotlk='http://subversion.assembla.com/svn/ytdbase/'
svn_psmd_wotlk='http://subversion.assembla.com/svn/psmdb_wotlk/'
svn_acid_wotlk='https://sd2-acid.svn.sourceforge.net/svnroot/sd2-acid/trunk/wotlk/'

# TBC
git_mangos_tbc='git://github.com/mangos-one/server.git'
git_scriptdev2_tbc='git://github.com/mangos-one/scripts.git'
git_database_tbc='git://github.com/mangos-one/database.git'
svn_acid_tbc='https://sd2-acid.svn.sourceforge.net/svnroot/sd2-acid/trunk/tbc/'

# Classic
git_mangos_classic='git://github.com/mangos-zero/server.git'
git_scriptdev2_classic='git://github.com/mangos-zero/scriptdev0.git'
git_database_classic='git://github.com/mangos-zero/database.git'
svn_acid_classic='https://sd2-acid.svn.sourceforge.net/svnroot/sd2-acid/trunk/classic/'
git_php_read_classic='git://github.com/mangos-zero/php-dbc.git'

# Custom Databases
svn_ytdb='http://subversion.assembla.com/svn/ytdbase/'
svn_udb='https://unifieddb.svn.sourceforge.net/svnroot/unifieddb'

# Custom Repo
git_mangchat='git://github.com/gimli/server.git mangchat'

install_dir='/mnt/mangos'
work_dir='/tmp/mangos'
log='install.log'
###################################################
# Functions do not edit unless you know what todo!#
###################################################

def clean_MaNGOS():
    print "Preparing MaNGOS setup...\n"
    print "Installing necessary packages to compile and run MaNGOS? yes/no"
    install_dep=raw_input('Selection: ')
    if install_dep=='yes':
       os.system('sudo apt-get install build-essential gcc g++ automake git-core autoconf make patch libmysql++-dev mysql-server libtool libssl-dev grep binutils zlibc libc6 libbz2-dev cmake subversion phpmyadmin')
       print ""
    elif install_dep=='no':
       print ""
    print "What version would you like to install?"
    print "Syntax: cataclysm/wotlk/tbc/classic\n"
    version=raw_input('Selection: ')
    if version=='cataclysm':
       mangos=git_mangos
       server='server'
       scriptdev2=git_scriptdev2
       acid=git_acid
       database=git_database
    elif version=='wotlk':
       mangos=git_mangos_wotlk
       server='mangos-wotlk'
       scriptdev2=git_scriptdev2_wotlk
       acid=svn_acid_wotlk
       database=svn_ytdb_wotlk
    elif version=='tbc':
       mangos=git_mangos_tbc
       server='mangos-one'
       scriptdev2=git_scriptdev2_tbc
       acid=svn_acid_tbc
       database=svn_acid_tbc
    elif version=='classic':
       mangos=git_mangos_classic
       server='mangos-zero'
       scriptdev2=git_scriptdev2_classic
       acid=svn_acid_classic
       database=git_database_classic
    else:
       print "I wasnt able to read you input!"
       restart_script()
    #print ""
    #print "Select where to install. default: "+work_dir
    #print "Syntax: default or /path/to/new/location"
    #new_work_dir=raw_input('Place: ')
    #if new_work_dir=='default':
    new_work_dir=work_dir
    print ""
    print ""
    print "Select where to install. default: "+install_dir
    print "Syntax: default or /path/to/new/location"
    new_install_dir=raw_input('Place: ')
    if new_install_dir=='default':
       new_install_dir=install_dir
       print ""
    if os.path.exists(work_dir):
       print ""
       print "Delete Current work in "+new_work_dir+"? yes/no"
       delete=raw_input('Selection: ')
       if delete=='yes':
          os.system('rm -rf '+new_work_dir)
          print ""
       elif delete=='no':
          print "Please edit MaNGOS.py and change your current work_dir value to keep your current work."
          print "Current Value: "+new_workdir
          print ""
          exit()
    if os.path.exists(new_install_dir):
       print ""
       print "Delete Current server "+new_install_dir+"? yes/no"
       delete=raw_input('Selection: ')
       if delete=='yes':
          os.system('rm -rf '+new_install_dir)
          print ""
       elif delete=='no':
          print "Please edit MaNGOS.py and change your current install_dir value to keep your current work."
          print "Current Value: "+new_install_dir
          print ""
          exit()
    print ""
    print "Install ScriptDev2? yes/no"
    scriptdev2=raw_input('Selection: ')
    print ""
    if version=='cataclysm':
       print "Install Mangchat_rewrite eng. ? yes/no"
       mangchat=raw_input('Selection: ')
       global mangchat
       print ""
    else:
       mangchat='no'
       global mangchat
    print ""
    print "Select database: default/ytdb/udb"
    database=raw_input('Selection: ')
    print ""
    print "Database info: "
    db_host=raw_input('Host: ')
    db_user=raw_input('User: ')
    db_pass=raw_input('Password: ')
    print ""
    print "CPU info. Nr. of cpu's?"
    cores=int(raw_input('Cores: '))
    print ""
    print "Script will now do its tricks, sit back relaxe and grab a beer.. :)\n"
    os.system('mkdir '+new_work_dir)
    print "Fetching MaNGOS source files... ("+mangos+")"
    for line in os.popen('cd '+new_work_dir+ ';git clone '+mangos+'').readlines():
           print line
    print "Fetching ScriptDev2 source files... ("+scriptdev2+")"
    for line in os.popen('cd '+new_work_dir+'/server/;git clone '+scriptdev2+' src/bindings/ScriptDev2').readlines():
           print line
    print ""
    print "Patching MaNGOS..."
    os.system('cd  '+new_work_dir+'/server;git apply src/bindings/ScriptDev2/patches/MaNGOS-*-ScriptDev2.patch')
    if os.path.exists(new_work_dir+'/server') and os.path.exists(new_work_dir+'/server/src/bindings/ScriptDev2'):
       print "MaNGOS Succesfully Downloaded and patched! Continuing."
    else:
       print "Something went wrong.. Please check you have permission to create: "+new_work_dir
       exit()
    if mangchat=='yes' and version=='cataclysm':
       print "\n Fetching Manchat_rewrite source files... ("+git_mangchat+")\n"
       print os.system("cd "+new_work_dir+"/server;git add .;git commit -a -m 'Commiting current work before fetching mangchat.'")
       print os.system('cd '+new_work_dir+'/server;git pull '+git_mangchat)
       print ""
    print os.system('cd '+new_work_dir+'/server;mkdir '+new_work_dir+'/server/objdir;cd '+new_work_dir+'/server/objdir;cmake .. -DPREFIX='+str(new_install_dir)+';make -j'+str(cores)+';make install')
    if os.path.exists(new_install_dir):
       print "MaNGOS Successfully compile and installed into: "+new_install_dir
    else:
       print "Error: Didnt compile? please check "+log
       exit()
    print "Copying/renaming MaNGOS *.conf files, place: "+new_install_dir+"/etc"
    os.system('cd '+new_install_dir+'/etc/;cp mangosd.conf.dist mangosd.conf;cp realmd.conf.dist realmd.conf;cp scriptdev2.conf.dist scriptdev2.conf;rm *.dist')
    print ""
    print os.system('ls -la '+new_install_dir+'/etc/')
    print ""
    if database=='default':
       print "Fetching MaNGOS Default database... ("+database+")"
       os.system('mkdir '+new_install_dir+'/database;cd '+new_install_dir+'/database')
       for line in os.popen('cd '+new_install_dir+'/database/;git clone '+database):
           if os.path.exists(new_install_dir+'/database/database'):
              print "Done fecthing default alpha (cataclysm) database."
              database_install(db_host,db_user,db_pass,new_work_dir,new_install_dir,'server')
              print ""
              print "Copying MaNGOS default sql files to "+new_install_dir+"/sql/"
              print "This is only as a backup if you choosed a default install."
              print ""
              os.system('cp -r '+new_work_dir+'/server/sql '+new_install_dir+'/')
              if mangchat=='yes':
                 print ""
                 print "Injecting Mangchat sql files into the world db (mangos)."
                 print "Remember to edit mangchat in your world db."
                 print 'http://'+db_host+'/phpmyadmin'
                 print ""
                 os.system('mysql -h '+db_host+' -u '+db_user+' -p'+db_pass+' mangos < '+new_work_dir+'/server/sql/custom/mangchat_world.sql')
              print "remember to edit files in "+new_install_dir+"/etc/"
              print os.system('ls -la '+new_install_dir+'/etc/')
              print ""
              print "Install Finish. Enjoy!"
              print ""
              exit()
    elif database=='ytdb':
       print "Fetching MaNGOS YTDB database... ("+svn_ytdb+")"
       os.system('mkdir '+new_install_dir+'/database;cd '+new_install_dir+'/database')
       for line in os.popen('cd '+new_install_dir+'/database/;svn co '+svn_ytdb):
           if os.path.exists(new_install_dir+'/database/ytdb'):
              print "Done fecthing YTDB alpha (cataclysm) database."
              exit()           
    elif database=='udb':
       print "Fetching MaNGOS UDB database... ("+svn_udb+")"
       os.system('mkdir '+new_install_dir+'/database;cd '+new_install_dir+'/database')
       for line in os.popen('cd '+new_install_dir+'/database/;svn co '+svn_udb):
           if os.path.exists(new_install_dir+'/database/unifieddb'):
              print "Done fecthing UDB database."
              exit() 
    else:
           print "I didnt read your choise, install is ending now. we hope you'll enjoy your new MMO Wow Server. \n Remember to setup your database! ;)"
           exit()
    print ""
    print "Enjoy! ;)"

def database_install(db_host,db_user,db_pass,new_work_dir,new_install_dir,server):
    print ""
    print "Preparing Databases..."
    os.system('mysql -h '+db_host+' -u '+db_user+' -p'+db_pass+' < '+new_work_dir+'/'+server+'/sql/create_mysql.sql')
    os.system('mysql -h '+db_host+' -u '+db_user+' -p'+db_pass+' characters < '+new_work_dir+'/'+server+'/sql/characters.sql')
    os.system('mysql -h '+db_host+' -u '+db_user+' -p'+db_pass+' mangos < '+new_work_dir+'/'+server+'/sql/mangos.sql')
    os.system('mysql -h '+db_host+' -u '+db_user+' -p'+db_pass+' realmd < '+new_work_dir+'/'+server+'/sql/realmd.sql')
    #ScriptDev2  Setup
    os.system('mysql -h '+db_host+' -u '+db_user+' -p'+db_pass+' < '+new_work_dir+'/'+server+'/src/bindings/ScriptDev2/sql/scriptdev2_create_database.sql')
    os.system('mysql -h '+db_host+' -u '+db_user+' -p'+db_pass+' scriptdev2 < '+new_work_dir+'/'+server+'/src/bindings/ScriptDev2/sql/scriptdev2_create_structure_mysql.sql')
    os.system('mysql -h '+db_host+' -u '+db_user+' -p'+db_pass+' scriptdev2 < '+new_work_dir+'/'+server+'/src/bindings/ScriptDev2/sql/scriptdev2_script_full.sql')
    print "Createing full alpha database.."
    os.system('cd '+new_install_dir+'/database/database;sh make_full_db.sh')
    os.system('mysql -h '+db_host+' -u '+db_user+' -p'+db_pass+' mangos < '+new_install_dir+'/database/database/full_db.sql')
    print "Database setup done."
    print ""

def install_log(msg):
    timeStamp=strftime("%Y-%m-%d %H:%M:%S ", localtime())
    f = open(log,'a')
    f.write('Time: ['+str(now)+'] - MSG: '+msg+'\n')
    f.close()

def update_current():
    print "Work in progress! - This should be working soon."

def restart_script():
    clean_MaNGOS()

def welcome():
    greet="\n Welcome to my install script, yet another lazy mans work ;)\n This has been tested and works whit the latest rev of MaNGOS and Ubuntu 12.04\n so fare its setup for latest client: 4.3.4 \n Please dont blame me if anything goes wrong its just a help i will try to keep it updated but i still lifes irl to ;) \n anyways sit back grab a beer and relaxe and let it work!\n Enjoy! ;)"
    return greet

####################################################

try:
    print welcome()
    print "\n Syntax: clean (clean install) / update (update your current work to latest rev.) / quit\n"
    selection=raw_input('Please enter your choise: \n')
except:
    print "Script ended! \n"
    exit()
if selection=='clean':
   clean_MaNGOS()
elif selection=='update':
   update_current()
elif selection=='quit':
   exit()
else:
   print "I wasnt able to read your input, Please try again."
   restart_script()
