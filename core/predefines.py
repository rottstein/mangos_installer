#!/usr/env python
# -*- coding: cp1252 -*- 
#
# Simply Edit theese values
# to your needs and save your self
# the time of the guide.

def loadPreDefines(self):
    self.install_dir='/home/bs/mangos/Classic' # Path to install
    self.q_data_dir='/home/bs/mangos/Data'       # Path to Data folder (DBC/MAPS/VMAPS)
    self.q_sd2='yes'                               # Download Scriptdev2
    self.q_mc='yes'                                # Cataclysm: Mangchat 1.7.9
    self.q_ahbot='yes'                             # Activate Ahbot
    self.q_acid='yes'                              # Download ACID
    self.q_host='localhost'                        # Database host
    self.q_user='root'                             # Database user (Default: root)
    self.q_pass='bjo10ern21'                           # Database password
    self.q_currentrealm='no'                       # Use current realm
    self.q_world='mangos'                          # World Database name
    self.q_realm='realmd'                          # Realm Database name
    self.q_char='characters'                       # Characters Database name
    self.q_script='scriptdev2'                     # ScriptDev2 Database name
    self.q_realmid=1                               # Realm ID (only when using multiple realms)
    self.q_realmname='MaNGOS'                      # Realm Name
    self.q_realmport=8085                          # Realm Port
    self.q_realmip='127.0.0.1'                     # Realm Ip
    self.q_acc='yes'
    self.q_newAcc='nickless'                       # New Account
    self.q_newAccPass='bjo10ern21'                     # New Account Password
    self.q_newAccGM=3                              # New Account GMLevel
    self.q_cores=4                                 # CPU cores
    self.q_loadServers='yes'                        # Load Servers
    self.del_folder(self.install_dir)
    self.del_folder(self.work_dir)
