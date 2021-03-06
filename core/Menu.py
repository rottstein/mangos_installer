#!/usr/env python

def info(self):
    self.msg('\nPreparing '+self.version+'..','green')
    self.msg('Choose where to install server?','green')
    self.install_dir=self.Quest(self.colored('Path: ','yellow'))
    self.del_folder(self.install_dir)
    self.del_folder(self.work_dir)
    self.msg('\nPath to Data folder? (This is the path to your DBC, Maps & Vmaps.)','green')
    self.q_data_dir=self.Quest(self.colored('Path: ','yellow'))
    self.msg('\nInstalling into: '+self.install_dir,'green')
    self.msg('\nCompile whit ScriptDev2?','green')
    self.q_sd2=self.Quest(0)
    if self.version=='cataclysm':
       self.msg('\nCompile whit MangChat 1.7.9?','green')
       self.q_mc=self.Quest(0)
    self.msg('\nActivate AuctionHouseBot?','green')
    self.q_ahbot=self.Quest(0)
    self.msg('\nActivate ACID?','green')
    self.q_acid=self.Quest(0)
    self.msg('\nDatabase information.','yellow')
    self.q_host=self.Quest(self.colored('Host: ','green'))
    self.q_user=self.Quest(self.colored('User: ','green'))
    self.q_pass=self.Quest(self.colored('Pass: ','green'))
    self.msg('\nRealm Information.','green')
    self.q_realmid=self.Quest(self.colored('ID: ','yellow'))
    self.q_realmname=self.Quest(self.colored('Name: ','yellow'))
    self.q_realmport=self.Quest(self.colored('Port: ','yellow'))
    self.q_realmip=self.Quest(self.colored('IP: ','yellow'))
    self.msg('\nSelect name of your world database?','green')
    self.q_world=self.Quest(self.colored('Name: ','yellow'))
    self.msg('\nUse current realm?','green')
    self.q_currentrealm=self.Quest(0)
    if self.q_currentrealm=='yes':
       self.msg('\nPlease type the name of your current realmd db.','green')
       self.q_realm=self.Quest(self.colored('Name: ','yellow'))
    elif self.q_currentrealm=='no':
       self.msg('\nSelect name of your realm database?','green')   
       self.q_realm=self.Quest(self.colored('Name: ','yellow'))
    self.msg('\nSelect name of your characters database?','green')
    self.q_char=self.Quest(self.colored('Name: ','yellow'))
    self.msg('\nSelect name of your scriptdev2 database?','green')
    self.q_script=self.Quest(self.colored('Name: ','yellow'))
    self.msg('\nCreate a new account?','green')
    self.q_acc=self.Quest(0)
    if self.q_acc=='yes':
       self.msg('\nType New Account info.','green')
       self.q_newAcc=self.Quest(self.colored('Username: ','yellow'))
       self.q_newAccPass=self.Quest(self.colored('Password: ','yellow'))
       self.q_newAccGM=self.Quest(self.colored('GMLevel: ','yellow'))
    else:
       self.q_newAcc='admin'
       self.q_newAccPass='admin'
       self.q_newAccGM=0
    self.msg('\nSelect number of cores? (CPU) - Currently not working, the command make -j4 doesnt seems to change anything.','red')
    self.q_cores=self.Quest(self.colored('Cores: ','yellow'))
    self.msg('\nStart MaNGOS when install is done?','green')
    self.q_loadServers=self.Quest(0)
