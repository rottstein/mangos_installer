#!/usr/env python
# -*- coding: cp1252 -*- 

def loadPreDefines(self):
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
