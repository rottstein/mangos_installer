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

wotlk=[
        'git://github.com/cmangos/mangos-wotlk.git',
        'git://github.com/scriptdev2/scriptdev2.git',
        'git://github.com/scriptdev2/acid.git',
        'http://subversion.assembla.com/svn/ytdbase/',
        '',
      ]

tbc=[
      'git://github.com/cmangos/mangos-tbc.git',
      'git://github.com/scriptdev2/scriptdev2-tbc.git',
      'git://github.com/scriptdev2/acid.git',
      '',
      '',
    ]

classic=[
         'git://github.com/cmangos/mangos-classic.git',
         'git://github.com/scriptdev2/scriptdev2-classic.git',
         'git://github.com/scriptdev2/acid.git',
         '',
         '',
        ]

def Cataclysm(self):
    os.system('clear')
    self.info(self)
    os.system('clear')
    self.msg(self.Correct(self),'green')
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
    if self.q_sd2=='yes':
       self.msg('\nDownloading ScriptDev2!','green')    
       self.fetch_scriptdev2(self,cataclysm[1],'cataclysm')
       if self.checkFolder(self.work_dir+'/server/src/bindings/ScriptDev2')==1:
          self.msg('ScriptDev2 Succesfully Downloaded!','green')
       else:
          self.msg('Error: Please check your connection and run script again!','red')  
          exit()
    else:
         pass
    self.msg('\nPatching SD2.','yellow')
    os.system('cd '+self.work_dir+'/server;git apply src/bindings/ScriptDev2/patches/MaNGOS-*-ScriptDev2.patch')
    if self.q_mc=='yes':
         self.msg('\nDownloading MangChat 1.7.9!','green')
         self.fetch_mangchat(self,cataclysm[4])
         if self.checkFolder(self.work_dir+'/server/src/game/mangchat')==1:
            self.msg('\nMangChat 1.7.9 Succesfully downloaded!','green')
         else:
            self.msg('\nError: Please check your connection and run script again!','red')
            exit()
    else:
         pass
    os.system('cd '+self.work_dir+'/server;mkdir '+self.work_dir+'/server/objdir;cd '+self.work_dir+'/server/objdir;cmake .. -DPREFIX='+str(self.install_dir)+';make -j'+str(self.q_cores)+';make install')
    if self.checkFolder(self.install_dir+'/bin')==1:
       self.msg('\n'+self.colored('MaNGOS Succesfully installed into','green')+' '+self.install_dir,'yellow')
       if self.q_ahbot=='yes':
          os.system('cd '+self.work_dir+'/server/src/game/AuctionHouseBot/; cp ahbot.conf.dist.in '+self.install_dir+'/etc/ahbot.conf')
       if self.q_mc=='yes':
          os.system('cd '+str(self.install_dir)+'/etc/;cp mangchat.conf.dist mangchat.conf')
       os.system('cd '+str(self.install_dir)+'/etc/;cp mangosd.conf.dist mangosd.conf;cp realmd.conf.dist realmd.conf;cp scriptdev2.conf.dist scriptdev2.conf;rm -rf *.dist')
       print os.system('ls -la '+str(self.install_dir)+'/etc/')
    else:
       self.msg('\nError: MaNGOS Failed to compile, Please check '+self.log_file,'red')
       exit()
    os.system('clear')
    self.msg('\nDownloading Databases.','green')
    self.fetch_database(self,cataclysm[3],'cata')
    self.MaNGOS_Database(self)
    self.setupChar(self)
    self.setupScriptDev2(self,'cata')
    if self.q_currentrealm=='yes':
       self.updateRealm(self)
    else:
       self.msg('\nCreating new realm db.','green')
       self.setupRealm(self)
    self.msg('\nSetting up ACID.','green')
    self.fetch_custom_git(self,self.install_dir+'/database/',cataclysm[2])
    os.system('cd '+self.install_dir+'/database/acid/;mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_world+' < acid_wotlk.sql')
    os.system('mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_world+' < '+self.work_dir+'/server/src/bindings/ScriptDev2/sql/mangos_scriptname_full.sql')
    self.msg('\nSetting Config files.','green')
    self.msg('\nSetting DataDir = "." to DataDir = '+self.q_data_dir,'green')
    self.replaceAll(self.install_dir+'/etc/mangosd.conf','"."','"'+str(self.q_data_dir)+'"')
    self.msg('\nSetting WorldServerPort = 8085 to WorldServerPort = '+self.q_realmport,'green')
    self.replaceAll(self.install_dir+'/etc/mangosd.conf','8085',''+str(self.q_realmport)+'')
    self.msg('\nSetting LoginDatabaseInfo = realmd to LoginDatabaseInfo = '+self.q_realm+' (realmd.conf)','green')
    self.replaceAll(self.install_dir+'/etc/realmd.conf','127.0.0.1;3306;mangos;mangos;realmd','127.0.0.1;3306;mangos;mangos;'+self.q_realm+'')
    self.msg('\nSetting LoginDatabaseInfo = realmd to LoginDatabaseInfo = '+self.q_realm,'green')  
    self.replaceAll(self.install_dir+'/etc/mangosd.conf','127.0.0.1;3306;mangos;mangos;realmd','127.0.0.1;3306;mangos;mangos;'+self.q_realm+'')
    self.msg('\nSetting WorldDatabaseInfo = mangos to WorldDatabaseInfo = '+self.q_world,'green')
    self.replaceAll(self.install_dir+'/etc/mangosd.conf','127.0.0.1;3306;mangos;mangos;mangos','127.0.0.1;3306;mangos;mangos;'+self.q_world+'')
    self.msg('\nSetting CharactersDatabaseInfo = characters to CharacterDatabaseInfo = '+self.q_char,'green') 
    self.replaceAll(self.install_dir+'/etc/mangosd.conf','127.0.0.1;3306;mangos;mangos;characters','127.0.0.1;3306;mangos;mangos;'+self.q_char+'')
    self.msg('\nSetting LoginDatabaseInfo = scriptdev2 to LoginDatabaseInfo = '+self.q_script+' (scriptdev2.conf)','green') 
    self.replaceAll(self.install_dir+'/etc/scriptdev2.conf','127.0.0.1;3306;mangos;mangos;scriptdev2','127.0.0.1;3306;mangos;mangos;'+self.q_script+'')
    # RESERVE for auto start script.
    print self.colored(self.Complete('Cataclysm'),'green')
    exit()

def Wotlk(self):
    os.system('clear')
    #self.info(self)
    self.install_dir='/home/bs/mangos/wotlk'
    self.q_data_dir='/mnt/Data'
    self.q_sd2='yes'
    self.q_mc='yes'
    self.q_ahbot='yes'
    self.q_acid='yes'
    self.q_host='localhost'
    self.q_user='root'
    self.q_pass='bjo10ern21'
    self.q_currentrealm='yes'
    self.q_world='mangos_w_world'
    self.q_realm='mangos_realmd'
    self.q_char='mangos_w_characters'
    self.q_script='mangos_w_scriptdev2'
    self.q_realmid=3
    self.q_realmname='test'
    self.q_realmport=8087
    self.q_realmip='192.168.1.12'
    self.q_cores=4
    self.del_folder(self.install_dir)
    self.del_folder(self.work_dir)
    os.system('clear')
    self.msg(self.Correct_w(self),'green')
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
    self.colored(self.fetch_git(self,wotlk[0]),'blue')
    if self.checkFolder(self.work_dir+'/mangos-wotlk')==1:
       self.msg('MaNGOS Succesfully Downloaded!','green')
    else:
       self.msg('Error: Please check your connection and run script again!','red')  
       exit()
    if self.q_sd2=='yes':
       self.msg('\nDownloading ScriptDev2!','green')    
       self.fetch_scriptdev2(self,wotlk[1],'wotlk')
       if self.checkFolder(self.work_dir+'/mangos-wotlk/src/bindings/ScriptDev2')==1:
          self.msg('ScriptDev2 Succesfully Downloaded!','green')
       else:
          self.msg('Error: Please check your connection and run script again!','red')  
          exit()
    else:
         pass
    self.msg('\nPatching SD2.','yellow')
    os.system('cd '+self.work_dir+'/mangos-wotlk;git apply src/bindings/ScriptDev2/patches/MaNGOS-*-ScriptDev2.patch')
    os.system('cd '+self.work_dir+'/mangos-wotlk;mkdir '+self.work_dir+'/mangos-wotlk/objdir;cd '+self.work_dir+'/mangos-wotlk/objdir;cmake .. -DPREFIX='+str(self.install_dir)+';make -j'+str(self.q_cores)+';make install')
    if self.checkFolder(self.install_dir+'/bin')==1:
       self.msg('\n'+self.colored('MaNGOS Succesfully installed into','green')+' '+self.install_dir,'yellow')
       if self.q_ahbot=='yes':
          os.system('cd '+self.work_dir+'/mangos-wotlk/src/game/AuctionHouseBot/; cp ahbot.conf.dist.in '+self.install_dir+'/etc/ahbot.conf')
       os.system('cd '+str(self.install_dir)+'/etc/;cp mangosd.conf.dist mangosd.conf;cp realmd.conf.dist realmd.conf;cp scriptdev2.conf.dist scriptdev2.conf;rm -rf *.dist')
       print os.system('ls -la '+str(self.install_dir)+'/etc/')
    else:
       self.msg('\nError: MaNGOS Failed to compile, Please check '+self.log_file,'red')
       exit()
    os.system('clear')
    self.msg('\nDownloading Databases.','green')
    self.fetch_svn(self,wotlk[3],'ytdb')
    self.setupYTDB(self)
    self.setupChar(self)
    self.setupScriptDev2(self,'wotlk')
    if self.q_currentrealm=='yes':
       self.updateRealm(self)
    else:
       self.msg('\nCreating new realm db.','green')
       self.setupRealm(self)
    self.msg('\nSetting up ACID.','green') 
    self.fetch_custom_git(self,self.install_dir+'/database/',wotlk[2]) 
    os.system('cd '+self.install_dir+'/database/acid/;mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_world+' < acid_wotlk.sql')
    os.system('mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_world+' < '+self.work_dir+'/mangos-wotlk/src/bindings/ScriptDev2/sql/mangos_scriptname_full.sql')
    self.msg('\nSetting Config files.','green')
    self.msg('\nSetting DataDir = "." to DataDir = '+self.q_data_dir,'green')
    self.replaceAll(self.install_dir+'/etc/mangosd.conf','"."','"'+str(self.q_data_dir)+'"')
    self.msg('\nSetting WorldServerPort = 8085 to WorldServerPort = '+self.q_realmport,'green')
    self.replaceAll(self.install_dir+'/etc/mangosd.conf','8085',''+str(self.q_realmport)+'')
    self.msg('\nSetting LoginDatabaseInfo = realmd to LoginDatabaseInfo = '+self.q_realm+' (realmd.conf)','green')
    self.replaceAll(self.install_dir+'/etc/realmd.conf','127.0.0.1;3306;mangos;mangos;realmd','127.0.0.1;3306;mangos;mangos;'+self.q_realm+'')
    self.msg('\nSetting LoginDatabaseInfo = realmd to LoginDatabaseInfo = '+self.q_realm,'green')  
    self.replaceAll(self.install_dir+'/etc/mangosd.conf','127.0.0.1;3306;mangos;mangos;realmd','127.0.0.1;3306;mangos;mangos;'+self.q_realm+'')
    self.msg('\nSetting WorldDatabaseInfo = mangos to WorldDatabaseInfo = '+self.q_world,'green')
    self.replaceAll(self.install_dir+'/etc/mangosd.conf','127.0.0.1;3306;mangos;mangos;mangos','127.0.0.1;3306;mangos;mangos;'+self.q_world+'')
    self.msg('\nSetting CharactersDatabaseInfo = characters to CharacterDatabaseInfo = '+self.q_char,'green') 
    self.replaceAll(self.install_dir+'/etc/mangosd.conf','127.0.0.1;3306;mangos;mangos;characters','127.0.0.1;3306;mangos;mangos;'+self.q_char+'')
    self.msg('\nSetting LoginDatabaseInfo = scriptdev2 to LoginDatabaseInfo = '+self.q_script+' (scriptdev2.conf)','green') 
    self.replaceAll(self.install_dir+'/etc/scriptdev2.conf','127.0.0.1;3306;mangos;mangos;scriptdev2','127.0.0.1;3306;mangos;mangos;'+self.q_script+'')
    # RESERVE for auto start script.
    print self.colored(self.Complete('Wotlk'),'green')
    exit()

def TBC(self):
    pass

def Classic(self):
    pass
