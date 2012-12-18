#!/usr/env python

def loadPreDefines(self):
    self.install_dir='' # Where to install MaNGOS /path/to/install
    self.q_data_dir=''  # Data folder for MaNGOS DBC/MAPS/VMAPS
    self.q_sd2=''       # Compile whit SD2
    self.q_mc=''        # Compile whit MangChat -> Only for 4.3.4 master repo.
    self.q_ahbot=''     # Activate AHBOT
    self.q_acid=''      # Fetch and setup ACID
    self.q_host=''      # DB host
    self.q_user=''      # DB user
    self.q_pass=''      # DB password
    self.q_currentrealm='' # use current realm or install new realm db. yes/no
    self.q_world=''        # World DB name
    self.q_realm=''        # Realm DB name
    self.q_char=''         # Characters DB name
    self.q_script=''       # ScriptDev2 DB name
    self.q_realmid=1       # Realm id (new realm)
    self.q_realmname=''    # Realm Name (by default MaNGOS)
    self.q_realmport=8085  # Realm Port 
    self.q_realmip=''      # Realm ip
    self.q_cores=4         # CPU using make -j4
