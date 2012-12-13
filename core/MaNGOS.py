#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 

def Cataclysm(self):
    self.msg('Preparing Cataclysm..')
    self.msg('\nChoose where to install server?')
    install_dir=self.Quest('Path: ')
    self.del_folder(install_dir)
    self.del_folder(self.work_dir)
    self.msg('\nInstalling into: '+install_dir)
    self.msg('\nCompile whit ScriptDev2?')
    q_sd2=self.Quest(0)
    self.msg('\nCompile whit MangChat 1.7.9?')
    q_mc=self.Quest(0)
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
    q_realmip=self.Quest('IP: ')
    q_realmport=self.Quest('Port: ')
    self.msg('\nSelect number of cores? (CPU)')
    q_cores=self.Quest('Cores: ')
    self.msg('\nWe are now done collecting information and ready todo our magic work, kick back and enjoy\nGo grap a beer or something this might take awhile depending on your system!\n')
    
      

def Wotlk(self):
    pass

def TBC(self):
    pass

def Classic(self):
    pass
