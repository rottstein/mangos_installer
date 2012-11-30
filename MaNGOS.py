#!/usr/bin/env python

import os, re, MySQLdb
from time import localtime, strftime

#############################################
# MaNGOS Install Config -                   #
#############################################

# Cataclysm
git_mangos='git://github.com/mangos/server.git'
git_scriptdev2='git://github.com/scriptdev2/scriptdev2.git'
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

################################################

def Install_dep():
    print ""
    print "Preparing MaNGOS setup...\n"
    print "Installing necessary packages to compile and run MaNGOS? yes/no"
    install_dep=raw_input('Selection: ')
    if install_dep=='yes':
       os.system('sudo apt-get install build-essential gcc g++ automake git-core autoconf make patch libmysql++-dev mysql-server libtool libssl-dev grep binutils zlibc libc6 libbz2-dev cmake subversion phpmyadmin')
    else:
       pass

def MaNGOS_Classic():
    print "\nPreparing MaNGOS Classic.. \n"
    print "\nWhere to install Classic? syntax: /path/to/install"
    install_dir=Quest(0)
    del_folder(install_dir)
    print "\nInstalling into: "+install_dir
    del_folder(work_dir)
    print "\nInstall ScriptDev2?"
    q_scriptdev2=Quest(0)
    print "\nDatabase info."
    host=Quest('Host: ')
    user=Quest('User: ')
    password=Quest('Pass: ')
    print "\nCpu info - nr. of cpu's?"
    cores=int(Quest(0))
    print "\nkick back and relaxe, and enjoy!"
    os.system('mkdir '+work_dir)
    print "\nFecthing MaNGOS..."
    fetch_git(work_dir,git_mangos_classic)
    if q_scriptdev2=='yes' or q_scriptdev2=='y':
       print "\nFetching ScriptDev2..."
       fetch_scriptdev2(work_dir,git_scriptdev2_classic,'classic')
       if os.path.exists(work_dir+'/server/src/bindings/ScriptDevZero'):
          print "\nScriptDev2 Succesfully downloaded!"
          print "\nPatching MaNGOS..."
          os.system('cd  '+work_dir+'/server;git apply src/bindings/ScriptDevZero/patches/MaNGOSZero-ScriptDevZero.patch')
       else:
          print "\nScriptDev2 Failed to download!"
          print "\nContinue compile or Quit?"
          move_on=Quest(0)
          if move_on=='yes':
             pass
          else:
             exit()
    else:
       pass
    print os.system('cd '+work_dir+'/server;mkdir '+work_dir+'/server/objdir;cd '+work_dir+'/server/objdir;cmake .. -DPREFIX='+str(install_dir)+';make -j'+str(cores)+';make install')
    if os.path.exists(install_dir):
       print "\nMaNGOS Succesfully installed!"
       Fetch_Database(install_dir,git_database_classic)
       MaNGOS_Database(host,user,password,work_dir,install_dir,'ScriptDevZero')
       print "\nCopying/renaming MaNGOS *.conf files, place: "+install_dir+"/etc\n"
       os.system('cd '+install_dir+'/etc/;cp mangosd.conf.dist mangosd.conf;cp realmd.conf.dist realmd.conf;cp scriptdev2.conf.dist scriptdev2.conf;rm *.dist')
       print os.system('ls -la '+install_dir+'/etc/')
       print "\nInstall ready to go!"    
       Complete()
       exit()

def MaNGOS_Tbc():
    print "\nPreparing MaNGOS TBC.. "
    print "\nWhere to install TBC? syntax: /path/to/install"
    install_dir=Quest(0)
    del_folder(install_dir)
    print "\nInstalling into: "+install_dir
    del_folder(work_dir)
    print "\nInstall ScriptDev2?"
    q_scriptdev2=Quest(0)
    print "\nDatabase info."
    host=Quest('Host: ')
    user=Quest('User: ')
    password=Quest('Pass: ')
    print "\nCpu info - nr. of cpu's?"
    cores=int(Quest(0))
    print "\nkick back and relaxe, and enjoy!"
    os.system('mkdir '+work_dir)
    print "\nFecthing MaNGOS..."
    fetch_git(work_dir,git_mangos_tbc)
    if q_scriptdev2=='yes' or q_scriptdev2=='y':
       print "\nFetching ScriptDev2..."
       fetch_scriptdev2(work_dir,git_scriptdev2_tbc,'tbc')
       if os.path.exists(work_dir+'/server/src/bindings/scripts'):
          print "\nScriptDev2 Succesfully downloaded!"
          print "\nPatching MaNGOS..."
          os.system('cd  '+work_dir+'/server;git apply src/bindings/scripts/patches/MaNGOS-*-ScriptDev2.patch')
       else:
          print "\nScriptDev2 Failed to download!"
          print "\nContinue compile or Quit?"
          move_on=Quest(0)
          if move_on=='yes':
             pass
          else:
             exit()
    else:
       pass
    print os.system('cd '+work_dir+'/server;mkdir '+work_dir+'/server/objdir;cd '+work_dir+'/server/objdir;cmake .. -DPREFIX='+str(install_dir)+';make -j'+str(cores)+';make install')
    if os.path.exists(install_dir):
       print "\nMaNGOS Succesfully installed!"
       Fetch_Database(install_dir,git_database_tbc)
       MaNGOS_Database(host,user,password,work_dir,install_dir,'scripts')
       print "\nCopying/renaming MaNGOS *.conf files, place: "+install_dir+"/etc\n"
       os.system('cd '+install_dir+'/etc/;cp mangosd.conf.dist mangosd.conf;cp realmd.conf.dist realmd.conf;cp scriptdev2.conf.dist scriptdev2.conf;rm *.dist')
       print os.system('ls -la '+install_dir+'/etc/')
       print "\nInstall ready to go!"
       Complete()
       exit()

def MaNGOS_Wotlk():
    print "\nPreparing MaNGOS Wotlk.. "
    print "\nWhere to install Wotlk? syntax: /path/to/install"
    install_dir=Quest(0)
    del_folder(install_dir)
    print "\nInstalling into: "+install_dir
    del_folder(work_dir)
    print "\nInstall ScriptDev2?"
    q_scriptdev2=Quest(0)
    print "\nCpu info - nr. of cpu's?"
    cores=int(Quest(0))
    print "\nkick back and relaxe, and enjoy!"
    os.system('mkdir '+work_dir)
    print "\nFecthing MaNGOS..."
    fetch_git(work_dir,git_mangos_wotlk)
    if q_scriptdev2=='yes' or q_scriptdev2=='y':
       print "\nFetching ScriptDev2..."
       fetch_scriptdev2(work_dir,git_scriptdev2_wotlk,'wotlk')
       if os.path.exists(work_dir+'/server/src/bindings/ScriptDev2'):
          print "\nScriptDev2 Succesfully downloaded!"
          print "\nPatching MaNGOS..."
          os.system('cd  '+work_dir+'/server;git apply src/bindings/ScriptDev2/patches/MaNGOS-*-ScriptDev2.patch')
       else:
          print "\nScriptDev2 Failed to download!"
          print "\nContinue compile or Quit?"
          move_on=Quest(0)
          if move_on=='yes':
             pass
          else:
             exit()
    else:
       pass
    print os.system('cd '+work_dir+'/server;mkdir '+work_dir+'/server/objdir;cd '+work_dir+'/server/objdir;cmake .. -DPREFIX='+str(install_dir)+';make -j'+str(cores)+';make install')
    if os.path.exists(install_dir):
       print "\nMaNGOS Succesfully installed!"
       print "\nCopying/renaming MaNGOS *.conf files, place: "+install_dir+"/etc\n"
       os.system('cd '+install_dir+'/etc/;cp mangosd.conf.dist mangosd.conf;cp realmd.conf.dist realmd.conf;cp scriptdev2.conf.dist scriptdev2.conf;rm *.dist')
       print os.system('ls -la '+install_dir+'/etc/')
       print "\nInstall ready to go! Remember to setup your databases find sql files in "+install_dir+"/sql"
       Complete()
       exit()

def MaNGOS_Cataclysm():
    print "\nPreparing MaNGOS Cataclysm.. "
    print "\nWhere to install Cataclysm? syntax: /path/to/install"
    install_dir=Quest(0)
    del_folder(install_dir)
    print "\nInstalling into: "+install_dir
    del_folder(work_dir)
    print "\nInstall ScriptDev2?"
    q_scriptdev2=Quest(0)
    print "\nInstall MangChat?"
    q_mangchat=Quest(0)
    print "\nDatabase info."
    host=Quest('Host: ')
    user=Quest('User: ')
    password=Quest('Pass: ')
    print "\nCpu info - nr. of cpu's?"
    cores=int(Quest(0))
    print "\nkick back and relaxe, and enjoy!"
    os.system('mkdir '+work_dir)
    print "\nFecthing MaNGOS..."
    fetch_git(work_dir,git_mangos)
    if q_scriptdev2=='yes' or q_scriptdev2=='y':
       print "\nFetching ScriptDev2..."
       fetch_scriptdev2(work_dir,git_scriptdev2,'cata')
       if os.path.exists(work_dir+'/server/src/bindings/ScriptDev2'):
          print "\nScriptDev2 Succesfully downloaded!"
          print "\nPatching MaNGOS..."
          os.system('cd  '+work_dir+'/server;git apply src/bindings/ScriptDev2/patches/MaNGOS-*-ScriptDev2.patch')
       else:
          print "\nScriptDev2 Failed to download!"
          print "\nContinue compile or Quit?"
          move_on=Quest(0)
          if move_on=='yes':
             pass
          else:
             exit()
    else:
       pass
    if q_mangchat=='yes' or q_mangchat=='y':
       print "\nFetching MangChat..."
       fetch_mangchat(work_dir,git_mangchat)
       if os.path.exists(work_dir+'/server/src/game/mangchat'):
          print "\nMangchat Succesfully downloaded!"
       else:
          print "\nMangchat Failed to download!"
          print "\nContinue compile or Quit?"
          move_on=Quest(0)
          if move_on=='yes':
             pass
          else:
             exit()
    else:
       pass
    print os.system('cd '+work_dir+'/server;mkdir '+work_dir+'/server/objdir;cd '+work_dir+'/server/objdir;cmake .. -DPREFIX='+str(install_dir)+';make -j'+str(cores)+';make install')
    if os.path.exists(install_dir):
       print "\nMaNGOS Succesfully installed!"
       Fetch_Database(install_dir,git_database)
       MaNGOS_Database(host,user,password,work_dir,install_dir,'ScriptDev2')
       print "\nCopying/renaming MaNGOS *.conf files, place: "+install_dir+"/etc\n"
       os.system('cd '+install_dir+'/etc/;cp mangosd.conf.dist mangosd.conf;cp realmd.conf.dist realmd.conf;cp scriptdev2.conf.dist scriptdev2.conf;rm *.dist')
       print os.system('ls -la '+install_dir+'/etc/')
       print "\nInstall ready to go!"
       Complete()
       exit()

def fetch_git(work_dir,link):
    for line in os.popen('cd '+work_dir+ ';git clone '+link+'').readlines():
           print line

def fetch_scriptdev2(work_dir,link,version):
    if version=='tbc':
       folder='scripts'
    elif version=='classic':
       folder='ScriptDevZero'
    elif version=='cata':
       folder='ScriptDev2'
    elif version=='wotlk':
       folder='ScriptDev2'
    print "\nCloning into "+work_dir+"/src/bindings/"+folder+"\n"
    for line in os.popen('cd '+work_dir+ '/server;git clone '+link+' src/bindings/'+folder).readlines():
           print line

def fetch_mangchat(work_dir,link):
    print os.system("cd "+work_dir+"/server;git add .;git commit -a -m 'Commiting current work before fetching mangchat.'")
    print os.system('cd '+work_dir+'/server;git pull '+link)

def fetch_svn(link):
    pass

def folder(dir):
    if os.path.exists(dir):
       return 'true'
    else:
       return 'false'

def del_folder(dir):
    if os.path.exists(dir):
       print "\nTheres already a folder by that name, you want me to delete it? yes/no ("+dir+")"
       del_current=Quest('Select: ')
       if del_current=='yes':
          os.system('rm -rf '+dir)
       else:
          print "\nPlease Delete or move your current files in path: "+dir
          print os.system('ls -la '+dir)
          exit()  

def Fetch_Database(install_dir,link):
       print "\nFetching MaNGOS Default database... ("+link+")"
       os.system('mkdir '+install_dir+'/database;cd '+install_dir+'/database')
       for line in os.popen('cd '+install_dir+'/database/;git clone '+link):
           if os.path.exists(install_dir+'/database/database'):
              print "\nDone fecthing default database."

def MaNGOS_Database(host,user,password,work_dir,install_dir,version):
    print "\nPreparing Databases..."
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' < '+work_dir+'/server/sql/create_mysql.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' characters < '+work_dir+'/server/sql/characters.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' mangos < '+work_dir+'/server/sql/mangos.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' realmd < '+work_dir+'/server/sql/realmd.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' < '+work_dir+'/server/src/bindings/'+version+'/sql/scriptdev2_create_database.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' scriptdev2 < '+work_dir+'/server/src/bindings/'+version+'/sql/scriptdev2_create_structure_mysql.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' scriptdev2 < '+work_dir+'/server/src/bindings/'+version+'/sql/scriptdev2_script_full.sql')
    print "\nCreateing full alpha database.."
    os.system('cd '+install_dir+'/database/database;sh make_full_db.sh')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' mangos < '+install_dir+'/database/database/full_db.sql')
    realm_name=Quest(0)
    ip_addr=Quest(0)
    db = MySQLdb.connect(host,user,password,'realmd')
    cursor = db.cursor()
    cursor.execute("UPDATE realmlist SET name = '"+realm_name+"' WHERE id = 1")
    cursor.execute("UPDATE realmlist SET address = '"+ip_addr+"' WHERE id = 1")
    result = cursor.fetchall()
    print "\nDatabase setup done."

def Quest(question):
    if question==0:
       question='Select: '
    else:
       question=question
    answer=raw_input(question)
    return answer

def Log(msg):
    timeStamp=strftime("%Y-%m-%d %H:%M:%S ", localtime())
    f = open(log,'a')
    f.write('Time: ['+str(now)+'] - MSG: '+msg+'\n')
    f.close()

def restart_script():
    Menu()

def welcome():
    greet="\n Welcome to my install script, yet another lazy mans work ;)\n This has been tested and works whit the latest rev of MaNGOS and Ubuntu 12.04\n so fare its setup for latest client: 4.3.4 \n Please dont blame me if anything goes wrong its just a help i will try to keep it updated but i still lifes irl to ;) \n anyways sit back grab a beer and relaxe and let it work!\n Enjoy! ;)"
    return greet

def Complete():
    end="""
        Script is now done installing.
        Databases setup and ready to go. (NOTE. this only apply to Cataclysm/TBC/Classic)
        Please go edit MaNGOS .conf files and open your database editor and edit realmlist.
        Enjoy!
        """

def Menu():
    try:
        print welcome()
        print "\n Syntax: Cataclysm / Wotlk / TBC / Classic / quit\n"
        selection=raw_input('Please enter your choise: ')
    except:
        print "Script ended! \n"
        exit()

    if selection=='cataclysm' or selection=='Cataclysm':
       Install_dep()
       MaNGOS_Cataclysm()
    elif selection=='wotlk' or selection=='Wotlk':
       Install_dep()
       MaNGOS_Wotlk()
    elif selection=='tbc' or selection=='TBC':
       Install_dep()
       MaNGOS_Tbc()
    elif selection=='classic' or selection=='Classic':
       Install_dep()
       MaNGOS_Classic()
    elif selection=='quit':
       exit()
    else:
       print "I wasnt able to read your input, Please try again."
       restart_script()

Menu()

