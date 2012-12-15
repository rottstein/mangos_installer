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
    self.msg('\nPreparing Cataclysm..','green')
    self.msg('Choose where to install server?','green')
    install_dir=self.Quest(self.colored('Path: ','yellow'))
    self.del_folder(install_dir)
    self.del_folder(self.work_dir)
    self.msg('\nPath to Data folder? (This is the path to your DBC, Maps & Vmaps.)','green')
    q_data_dir=self.Quest(self.colored('Path: ','yellow'))
    self.msg('\nInstalling into: '+install_dir,'green')
    self.msg('\nCompile whit ScriptDev2?','green')
    q_sd2=self.Quest(0)
    self.msg('\nCompile whit MangChat 1.7.9?','green')
    q_mc=self.Quest(0)
    self.msg('\nActivate AuctionHouseBot?','green')
    q_ahbot=self.Quest(0)
    self.msg('\nDatabase information.','yellow')
    q_host=self.Quest(self.colored('Host: ','green'))
    q_user=self.Quest(self.colored('User: ','green'))
    q_pass=self.Quest(self.colored('Pass: ','green'))
    self.msg('\nSelect name of your world database?','green')
    q_world=self.Quest(self.colored('Name: ','yellow'))
    self.msg('\nSelect name of your realm database?','green')
    q_realm=self.Quest(self.colored('Name: ','yellow'))
    self.msg('\nSelect name of your characters database?','green')
    q_char=self.Quest(self.colored('Name: ','yellow'))
    self.msg('\nSelect name of your scriptdev2 database?','green')
    q_script=self.Quest(self.colored('Name: ','yellow'))
    self.msg('\nSetup ACID?','green')
    q_acid=self.Quest(0)
    self.msg('\nRealm Information.','green')
    q_realmname=self.Quest(self.colored('Name: ','yellow'))
    q_realmport=self.Quest(self.colored('Port: ','yellow'))
    q_realmip=self.Quest(self.colored('IP: ','yellow'))
    self.msg('\nSelect number of cores? (CPU)','green')
    q_cores=self.Quest(self.colored('Cores: ','yellow'))
    dbs=[
         q_world,
         q_realm,
         q_char,
         q_script
        ]
    os.system('clear')
    self.msg("""Collected Information.
    ----------------------
    Database:
       Host: """+self.colored(q_host,'yellow')+"""
       User: """+self.colored(q_user,'yellow')+"""
       Pass: """+self.colored(q_pass,'red')+"""

    Realm:
       Name: """+self.colored(q_realmname,'yellow')+"""
       Port: """+self.colored(q_realmport,'yellow')+"""
       IP: """+self.colored(q_realmip,'yellow')+"""

    Config:
       Path: """+self.colored(install_dir,'yellow')+"""
       Data: """+self.colored(q_data_dir,'yellow')+"""
       ScriptDev2: """+self.colored(q_sd2,'yellow')+"""
       MangChat: """+self.colored(q_mc,'yellow')+"""
       AuctionHouseBot: """+self.colored(q_ahbot,'yellow')+"""
       ACID: """+self.colored(q_acid,'yellow')+"""             
             """,'green')
    self.msg('\nIs this correct?','yellow')
    con=self.Quest(0)
    if con=='yes':
       os.system('clear')
    else:
       exit()
    self.msg('\nWe are now done collecting information and ready todo our magic work, kick back and enjoy','blue')
    self.msg('Go grap a beer or something, this might take awhile depending on your system!','blue')
    self.mkdir(self.work_dir)
    if self.checkFolder(self.backup_dir)==1:
       self.msg('\nBackup folder already exists!','red')
    else:
       self.mkdir(self.backup_dir)
    self.msg('\nDownloading MaNGOS!','green')
    self.fetch_git(self,cataclysm[0])
    if self.checkFolder(self.work_dir+'/server')==1:
       self.msg('MaNGOS Succesfully Downloaded!','green')
    else:
       self.msg('Error: Please check your connection and run script again!','red')  
       exit()
    if q_sd2=='yes':
       self.msg('\nDownloading ScriptDev2!','green')    
       self.fetch_scriptdev2(self,cataclysm[1],'cata')
       if self.checkFolder(self.work_dir+'/server/src/bindings/ScriptDev2')==1:
          self.msg('ScriptDev2 Succesfully Downloaded!','green')
       else:
          self.msg('Error: Please check your connection and run script again!','red')  
          exit()
    else:
         pass
    self.msg('\nPatching SD2.','yellow')
    os.system('cd '+self.work_dir+'/server;git apply src/bindings/ScriptDev2/patches/MaNGOS-*-ScriptDev2.patch')
    if q_mc=='yes':
         self.msg('\nDownloading MangChat 1.7.9!','green')
         self.fetch_mangchat(self,cataclysm[4])
         if self.checkFolder(self.work_dir+'/server/src/game/mangchat')==1:
            self.msg('\nMangChat 1.7.9 Succesfully downloaded!','green')
         else:
            self.msg('\nError: Please check your connection and run script again!','red')
            exit()
    else:
         pass
    os.system('cd '+self.work_dir+'/server;mkdir '+self.work_dir+'/server/objdir;cd '+self.work_dir+'/server/objdir;cmake .. -DPREFIX='+str(install_dir)+';make -j'+str(q_cores)+';make install')
    if self.checkFolder(install_dir+'/bin')==1:
       self.msg('\n'+self.colored('MaNGOS Succesfully installed into','green')+' '+install_dir,'yellow')
       if q_ahbot=='yes':
          os.system('cd '+self.work_dir+'/server/src/game/AuctionHouseBot/; cp ahbot.conf.dist.in '+install_dir+'/etc/ahbot.conf')
       if q_mc='yes':
          os.system('cd '+str(install_dir)+'/etc/;cp mangchat.conf.dist mangchat.conf')
       os.system('cd '+str(install_dir)+'/etc/;cp mangosd.conf.dist mangosd.conf;cp realmd.conf.dist realmd.conf;cp scriptdev2.conf.dist scriptdev2.conf;rm -rf *.dist')
       print os.system('ls -la '+str(install_dir)+'/etc/')
    else:
       self.msg('\nError: MaNGOS Failed to compile, Please check '+self.log_file,'red')
       exit()
    os.system('clear')
    self.msg('\nDownloading Databases.','green')
    self.fetch_database(self,install_dir,cataclysm[3],'cata')
    self.msg('\nSetting up Databases.','green')
    self.MaNGOS_Database(self,q_host,q_user,q_pass,install_dir,'cata',dbs,q_realmname,q_realmport,q_realmip) 
    self.msg('\nSetting up ACID.','green')
    self.fetch_custom_git(self,install_dir+'/database/',cataclysm[2])
    os.system('cd '+install_dir+'/database/acid/;mysql -h '+q_host+' -u '+q_user+' -p'+q_pass+' '+dbs[0]+' < acid_wotlk.sql')
    os.system('mysql -h '+q_host+' -u '+q_user+' -p'+q_pass+' mangos < '+self.work_dir+'/server/src/bindings/ScriptDev2/sql/mangos_scriptname_full.sql')
    self.msg('\nSetting Config files.','green')
    self.msg('\nSetting DataDir = "." to DataDir = '+q_data_dir,'green')
    self.replaceAll(install_dir+'/etc/mangosd.conf','"."','"'+str(q_data_dir)+'"')
    self.msg('\nSetting WorldServerPort = 8085 to WorldServerPort = '+q_realmport,'green')
    self.replaceAll(install_dir+'/etc/mangosd.conf','8085',''+str(q_realmport)+'')
    self.msg('\nSetting LoginDatabaseInfo = realmd to LoginDatabaseInfo = '+dbs[1]+' (realmd.conf)','green')
    self.replaceAll(install_dir+'/etc/realmd.conf','127.0.0.1;3306;mangos;mangos;realmd','127.0.0.1;3306;mangos;mangos;'+dbs[1]+'')
    self.msg('\nSetting LoginDatabaseInfo = realmd to LoginDatabaseInfo = '+dbs[1],'green')  
    self.replaceAll(install_dir+'/etc/mangosd.conf','127.0.0.1;3306;mangos;mangos;realmd','127.0.0.1;3306;mangos;mangos;'+dbs[1]+'')
    self.msg('\nSetting WorldDatabaseInfo = mangos to WorldDatabaseInfo = '+dbs[0],'green')
    self.replaceAll(install_dir+'/etc/mangosd.conf','127.0.0.1;3306;mangos;mangos;mangos','127.0.0.1;3306;mangos;mangos;'+dbs[0]+'')
    self.msg('\nSetting CharactersDatabaseInfo = characters to CharacterDatabaseInfo = '+dbs[2],'green') 
    self.replaceAll(install_dir+'/etc/mangosd.conf','127.0.0.1;3306;mangos;mangos;characters','127.0.0.1;3306;mangos;mangos;'+dbs[2]+'')
    self.msg('\nSetting LoginDatabaseInfo = scriptdev2 to LoginDatabaseInfo = '+dbs[3]+' (scriptdev2.conf)','green') 
    self.replaceAll(install_dir+'/etc/scriptdev2.conf','127.0.0.1;3306;mangos;mangos;scriptdev2','127.0.0.1;3306;mangos;mangos;'+dbs[3]+'')
    # RESERVE for auto start script.
    print self.Complete('Cataclysm',install_dir,q_realmname,q_realmport,q_realmip)
    exit()
    #os.system('clear')

def Wotlk(self):
    pass

def TBC(self):
    pass

def Classic(self):
    pass
