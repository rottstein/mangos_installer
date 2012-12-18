#!/usr/env python
# -*- coding: cp1252 -*- 

def loadPreDefines(self):
    self.install_dir='/home/bs/mangos/tbc'
    self.q_data_dir='/mnt/Data'
    self.q_sd2='yes'
    self.q_mc='yes'
    self.q_ahbot='yes'
    self.q_acid='yes'
    self.q_host='localhost'
    self.q_user='root'
    self.q_pass='bjo10ern21'
    self.q_currentrealm='yes'
    self.q_world='mangos_t_world'
    self.q_realm='mangos_realmd'
    self.q_char='mangos_t_characters'
    self.q_script='mangos_t_scriptdev2'
    self.q_realmid=3
    self.q_realmname='tbc'
    self.q_realmport=8087
    self.q_realmip='192.168.1.12'
    self.q_cores=4
    self.del_folder(self.install_dir)
    self.del_folder(self.work_dir)
