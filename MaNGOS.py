#!/usr/bin/env python

import os, re, MySQLdb
from time import localtime, strftime

#############################################
# MaNGOS Install Config -                   #
#############################################

# Cataclysm
git_mangos='git://github.com/mangos/server.git'
git_scriptdev2='git://github.com/scriptdev2/scriptdev2-cata.git'
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
git_scriptdev2_classic='git://github.com/scriptdev2/scriptdev2-classic.git'
git_database_classic='git://github.com/mangos-zero/database.git'
svn_acid_classic='https://sd2-acid.svn.sourceforge.net/svnroot/sd2-acid/trunk/classic/'
git_php_read_classic='git://github.com/mangos-zero/php-dbc.git'

# Custom Databases
svn_ytdb='http://subversion.assembla.com/svn/ytdbase/'
svn_udb='https://unifieddb.svn.sourceforge.net/svnroot/unifieddb'

# Custom Repo
git_mangchat='git://github.com/gimli/server.git'
git_custom_scriptdev2='git://github.com/gimli/scriptdev2.git'

# Paths
work_dir='/tmp/mangos'
log='install.log'

###################################################

def MaNGOS_Install(custom,scriptdev2,version):
    print "\nPreparing MaNGOS "+version+".. "
    print "\nWhere to install "+version+"? syntax: /path/to/install"
    install_dir=Quest(0)
    del_folder(install_dir)
    print "\nInstalling into: "+install_dir
    del_folder(work_dir)
    print "\nInstall ScriptDev2?"
    q_scriptdev2=Quest(0)
    if version=='Cataclysm':
       print "\nInstall MangChat?"
       q_mangchat=Quest(0)
    else:
       q_mangchat='no'
    print "\nCpu info - nr. of cpu's?"
    cores=int(Quest(0))
    print "\nkick back and relaxe, and enjoy!"
    os.system('mkdir '+work_dir)
    print "\nFecthing MaNGOS "+version+"..."
    if version=='Cataclysm':
       fetch_git(work_dir,git_mangos)
    elif version=='Wotlk':
       fetch_git(work_dir,git_mangos_wotlk)
    elif version=='TBC':
       fetch_git(work_dir,git_mangos_tbc)
    elif version=='Classic':
       fetch_git(work_dir,git_mangos_classic)
    if q_scriptdev2=='yes' or q_scriptdev2=='y':
       print "\nFetching ScriptDev2 ("+version+")..."
       if version=='Cataclysm':
          fetch_scriptdev2(work_dir,git_scriptdev2,'cata')
       elif version=='Wotlk':
          fetch_scriptdev2(work_dir,git_scriptdev2_wotlk,'wotlk')
       elif version=='TBC':
          fetch_scriptdev2(work_dir,git_scriptdev2_tbc,'tbc')
       elif version=='Classic':
          fetch_scriptdev2(work_dir,git_scriptdev2_classic,'classic')
       else:
          print "Error: Version didnt get parsed right - Version: "+version
          exit()
       print "\nScriptDev2 Succesfully downloaded!"
       print "\nPatching MaNGOS..."
       if os.path.exists(work_dir+'/server/src/bindings/ScriptDev2') and version=='Cataclysm' or version=='Wotlk':
          os.system('cd  '+work_dir+'/server;git apply src/bindings/ScriptDev2/patches/MaNGOS-*-ScriptDev2.patch')
          print "\nFetch Custom repo containing: LevelNPC, ProfessionNPC, TeleNPC2, Summon Item Scripts"
          custom=Quest(0)
          if version=='Cataclysm' and custom=='yes' or custom=='yes':
             os.system('cd '+work_dir+'/server/src/bindings/ScriptDev2/;git pull git@isengard.dk:scriptdev2.git')
          else:
             pass
       elif os.path.exists(work_dir+'/server/src/bindings/scripts') and version=='TBC':
          os.system('cd  '+work_dir+'/server;git apply src/bindings/scripts/patches/MaNGOS-*-ScriptDev2.patch')
       elif os.path.exists(work_dir+'/server/src/bindings/ScriptDevZero') and version=='Classic':
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
       Fetch_Database(install_dir,git_database,version)
       print "\nDo you want me to setup your databases?"
       do_db=Quest(0)
       if do_db=='yes' or do_db=='y':
          print "\nDatabase info."
          host=Quest('Host: ')
          user=Quest('User: ')
          password=Quest('Pass: ')
          if version=='Cataclysm':
             MaNGOS_Database(host,user,password,work_dir,install_dir,'cata')
          elif version=='Wotlk':
             MaNGOS_Database(host,user,password,work_dir,install_dir,'wotlk')
          elif version=='TBC':
             MaNGOS_Database(host,user,password,work_dir,install_dir,'tbc')
          elif version=='Classic':
             MaNGOS_Database(host,user,password,work_dir,install_dir,'classic')
          else:
             print "Error: Version didnt get parsed right - Version: "+version
             exit()
       print "\nPlease enter your realm name?"
       realm_name=Quest(0)
       print "\nPlease enter your realm ip?"
       ip_addr=Quest(0)
       db = MySQLdb.connect(host,user,password,'realmd')
       cursor = db.cursor()
       cursor.execute("UPDATE realmlist SET name = '"+str(realm_name)+"' WHERE id = 1")
       cursor.execute("UPDATE realmlist SET address = '"+str(ip_addr)+"' WHERE id = 1")
       result = cursor.fetchall()
       if version=='TBC':
          print "\nFetching ACID "+version
          fetch_svn(install_dir,svn_acid_tbc,version)
          print "\nRunning ACID sql's.."
          os.system('mysql -h '+host+' -u '+user+' -p'+password+' mangos < '+install_dir+'/database/tbc/2.0.7/2.0.7_acid.sql')
          os.system('mysql -h '+host+' -u '+user+' -p'+password+' mangos < '+work_dir+'/server/src/bindings/ScriptDev2/sql/mangos_scriptname_full.sql')
       else:
          pass
       print "\nCopying/renaming MaNGOS *.conf files, place: "+install_dir+"/etc\n"
       os.system('cd '+str(install_dir)+'/etc/;cp mangosd.conf.dist mangosd.conf;cp realmd.conf.dist realmd.conf;cp scriptdev2.conf.dist scriptdev2.conf;rm -rf *.dist')
       print "\nActivate AuctionHouseBot?"
       ahbot=Quest(0)
       if ahbot=='yes' or ahbot=='Yes':
          os.system('cd '+work_dir+'/server/src/game/AuctionHouseBot/; cp ahbot.conf.dist.in '+install_dir+'/etc/ahbot.conf')
       print os.system('ls -la '+str(install_dir)+'/etc/')
       print "\nFire up the server?"
       start_server=Quest(0)
       if start_server=='yes' or start_server=='Yes':
          os.system('sudo apt-get install screen')
          os.system('cd '+str(install_dir)+'/bin/;screen -A -m -d -S mangosworld ./mangosd;screen -A -m -d -S mangosrealm ./realmd')
          os.system('touch start_world.sh')
          os.system('touch start_realm.sh')
          os.system('echo screen -A -m -d -S mangosworld ./mangosd >> start_world.sh')
          os.system('echo screen -A -m -d -S mangosrealm ./realmd >> start_realm.sh') 
          print os.system('ps ax | grep SCREEN')
       Complete(version,str(install_dir),realm_name,ip_addr)
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
    print "\nCloning into "+work_dir+"/server/src/bindings/"+folder+"\n"
    for line in os.popen('cd '+work_dir+ '/server;git clone '+link+' src/bindings/'+folder).readlines():
           print line

def fetch_mangchat(work_dir,link):
    print os.system("cd "+work_dir+"/server;git add .;git commit -a -m 'Commiting current work before fetching mangchat.'")
    print os.system('cd '+work_dir+'/server;git pull '+link)

def fetch_svn(install_dir,link,version):
    os.system('cd '+install_dir+'/database/;svn co '+link+'')

def syntax_error(syntax):
    print "[ERROR] : Syntax error! ("+str(syntax)+")"

def Install_dep(version):
    print ""
    print "Preparing MaNGOS "+version+" setup...\n"
    print "Installing necessary packages to compile and run MaNGOS? yes/no"
    install_dep=raw_input('Selection: ')
    if install_dep=='yes':
       os.system('sudo apt-get install build-essential gcc g++ automake git-core autoconf make patch libmysql++-dev mysql-server libtool libssl-dev grep binutils zlibc libc6 libbz2-dev cmake subversion phpmyadmin screen')
    else:
       pass

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

def Fetch_Database(install_dir,link,version):
       print "\nFetching MaNGOS "+version+" Default database... ("+link+")"
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
    if version=='tbc':
       folder='scripts'
    elif version=='classic':
       folder='ScriptDevZero'
    elif version=='cata':
       folder='ScriptDev2'
    elif version=='wotlk':
       folder='ScriptDev2'
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' < '+work_dir+'/server/src/bindings/'+folder+'/sql/scriptdev2_create_database.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' scriptdev2 < '+work_dir+'/server/src/bindings/'+folder+'/sql/scriptdev2_create_structure_mysql.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' scriptdev2 < '+work_dir+'/server/src/bindings/'+folder+'/sql/scriptdev2_script_full.sql')
    print "\nCreateing full database.."
    os.system('cd '+install_dir+'/database/database;sh make_full_db.sh')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' mangos < '+install_dir+'/database/database/full_db.sql')
    print "\nDatabase setup done."

def Quest(question):
    if question==0:
       question='Select: '
    else:
       question=question
    answer=raw_input(question)
    return answer

def restart_script():
    Menu()

def welcome():
    greet="\n Welcome to my install script, yet another lazy mans work ;)\n This has been tested and works whit the latest rev of MaNGOS and Ubuntu 12.04\n Please dont blame me if anything goes wrong its just a help i will try to keep it updated but i still lifes irl to ;) \n anyways sit back grab a beer and relaxe and let it work!\n Enjoy! ;)"
    return greet

def Complete(version,install_dir,realmdname,realmdip):
    end="""
        Script is now done installing. you are now ready to run your server! ("""+version+""")
        Set your client realmlist to: """+realmip+"""
        Login:
              username: administrator
              password: administrator

        Database:
              location: http://localhost/phpmyadmin
              username: mangos
              password: mangos
        
        Server:
              location: """+install_dir+"""
              conf_dir: """+install_dir+"""/etc

        RealmInfo:
              name: """+realmdname+"""
              ip: """+realmdip+"""
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
       Install_dep('Cataclysm')
       MaNGOS_Install('custom','ScriptDev2','Cataclysm')
    elif selection=='wotlk' or selection=='Wotlk':
       Install_dep('Wotlk')
       MaNGOS_Install('custom','ScriptDev2','Wotlk')
    elif selection=='tbc' or selection=='TBC':
       Install_dep('tbc')
       MaNGOS_Install('custom','scripts','TBC')
    elif selection=='classic' or selection=='Classic':
       Install_dep('Classic')
       MaNGOS_Install('custom','ScriptDevZero','Classic')
    elif selection=='quit':
       exit()
    else:
       syntax_error('Cataclysm/Wotlk/TBC/Classic')
       restart_script()

Menu()
