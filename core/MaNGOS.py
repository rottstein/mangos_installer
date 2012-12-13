#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 

import os
import MySQLdb

cataclysm=[
            'git://github.com/mangos/server.git',
            'git://github.com/scriptdev2/scriptdev2-cata.git',
            'git://github.com/scriptdev2/acid.git',
            'git://github.com/mangos/database.git',
            'git://github.com/gimli/server.git mangchat'
          ]

def Cataclysm(self):
    os.system('clear')
    self.msg('\nPreparing Cataclysm..')
    self.msg('Choose where to install server?')
    install_dir=self.Quest('Path: ')
    self.del_folder(install_dir)
    self.del_folder(self.work_dir)
    self.msg('\nInstalling into: '+install_dir)
    self.msg('\nCompile whit ScriptDev2?')
    q_sd2=self.Quest(0)
    self.msg('\nCompile whit MangChat 1.7.9?')
    q_mc=self.Quest(0)
    self.msg('\nActivate AuctionHouseBot?')
    q_ahbot=self.Quest(0)
    self.msg('\nDatabase information.')
    q_host=self.Quest('Host: ')
    q_user=self.Quest('User: ')
    q_pass=self.Quest('Pass: ')
    self.msg('\nSelect name of your world database?')
    q_world=self.Quest('Name: ')
    self.msg('\nSelect name of your realm database?')
    q_realm=self.Quest('Name: ')
    self.msg('\nSelect name of your characters database?')
    q_char=self.Quest('Name: ')
    self.msg('\nSelect name of your scriptdev2 database?')
    q_script=self.Quest('Name: ')
    self.msg('\nSetup ACID?')
    q_acid=self.Quest(0)
    self.msg('\nRealm Information.')
    q_realmname=self.Quest('Name: ')
    q_realmport=self.Quest('Port: ')
    q_realmip=self.Quest('IP: ')
    self.msg('\nSelect number of cores? (CPU)')
    q_cores=self.Quest('Cores: ')
    dbs=[
         q_world,
         q_realm,
         q_char,
         q_script
        ]
    os.system('clear')
    self.msg('\nWe are now done collecting information and ready todo our magic work, kick back and enjoy')
    self.msg('Go grap a beer or something this might take awhile depending on your system!')
    self.mkdir(self.work_dir)
    self.msg('\nDownloading MaNGOS!')
    self.fetch_git(self,cataclysm[0])
    if self.checkFolder(self.work_dir+'/server')==1:
       self.msg('MaNGOS Succesfully Downloaded!')
    else:
       self.msg('Error: Please check your connection and run script again!')  
       exit()
    if q_sd2=='yes':
       self.msg('\nDownloading ScriptDev2!')    
       self.fetch_scriptdev2(self,cataclysm[1],'cata')
       if self.checkFolder(self.work_dir+'/server/src/bindings/ScriptDev2')==1:
          self.msg('ScriptDev2 Succesfully Downloaded!')
       else:
          self.msg('Error: Please check your connection and run script again!')  
          exit()
    else:
         pass
    self.msg('\nPatching SD2.')
    os.system('cd '+self.work_dir+'/server;git apply src/bindings/ScriptDev2/patches/MaNGOS-*-ScriptDev2.patch')
    if q_mc=='yes':
         self.msg('\nDownloading MangChat 1.7.9!')
         self.fetch_mangchat(self,cataclysm[4])
         if self.checkFolder(self.work_dir+'/server/src/game/mangchat')==1:
            self.msg('\nMangChat 1.7.9 Succesfully downloaded!')
         else:
            self.msg('\nError: Please check your connection and run script again!')
            exit()
    else:
         pass
    os.system('cd '+self.work_dir+'/server;mkdir '+self.work_dir+'/server/objdir;cd '+self.work_dir+'/server/objdir;cmake .. -DPREFIX='+str(install_dir)+';make -j'+str(q_cores)+';make install')
    if self.checkFolder(install_dir+'/bin')==1:
       self.msg('\nMaNGOS Succesfully installed into '+install_dir)
    else:
       self.msg('\nError: MaNGOS Failed to compile, Please check '+self.log_file)
       exit()
    self.msg('\nPreparing MySQL-Server.')
    db = MySQLdb.connect(q_host,q_user,q_pass)
    cursor = db.cursor("SELECT user FROM mysql.user WHERE user='mangos'")
    result = cursor.fetchall()
    if not result:
       cursor.execute("CREATE USER 'mangos'@'localhost' IDENTIFIED BY 'mangos'")
    else:
       print "MySQL User: mangos@localhost already exists!"
    for database in dbs:
        self.check_Database(self,q_host,q_user,q_pass,database)
        cursor.execute('CREATE DATABASE `'+database+'` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci')
        cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, LOCK TABLES ON `"+database+"`.* TO 'mangos'@'localhost'")
    #self.msg('\nDownloading Databases.')
    #self.MaNGOS_Database(q_host,q_user,q_pass,self.work_dir,install_dir,'cata')   

def Wotlk(self):
    pass

def TBC(self):
    pass

def Classic(self):
    pass
