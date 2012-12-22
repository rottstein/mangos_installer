#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 

import os
import MySQLdb
from time import localtime, strftime

def check_Database(self,what_db):
    db = MySQLdb.connect(self.q_host,self.q_user,self.q_pass)
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES LIKE '"+str(what_db)+"'")
    checks = cursor.fetchall()
    if not checks:
       print self.colored("\nCreating: Database["+str(what_db)+"]",'green')
    else:
       self.backupDB(self,what_db)

def backupDB(self,what_db):
    date=strftime("%Y_%m_%d ", localtime())
    print self.colored("\nDumping Current Database["+what_db+"]",'green')
    os.system('cd '+self.backup_dir+';mysqldump -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+str(what_db)+' > '+str(what_db)+'_backup.sql')
    os.system('cd '+self.backup_dir+';mv '+what_db+'_backup.sql '+what_db+'_'+date+'')
    db = MySQLdb.connect(self.q_host,self.q_user,self.q_pass)
    cursor = db.cursor()
    cursor.execute('DROP database `'+str(what_db)+'`') 

def updateRealm(self):
    self.msg('\nUpdating Current Realm Database','green')
    db = MySQLdb.connect(self.q_host,self.q_user,self.q_pass,self.q_realm)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM `realmlist` WHERE `id` = '+str(self.q_realmid)+'')
    result = cursor.fetchall()
    if not result:
       cursor.execute("INSERT INTO `realmlist` VALUES ("+str(self.q_realmid)+",'"+str(self.q_realmname)+"','"+str(self.q_realmip)+"',"+str(self.q_realmport)+",1,0,1,0,0,'')")
    else:
       self.msg('\nRealm: '+str(self.q_realmid)+' - Name: '+str(self.q_realmname)+' - IP: '+str(self.q_realmip)+' - Port: '+str(self.q_realmport)+'','green')
       self.msg('\nPlease enter a new realm ID since '+str(self.q_realmid)+' is already used!','red')
       q_newID=self.Quest('ID: ')
       q_newName=self.Quest('Name: ')
       q_newPort=self.Quest('Port: ')
       q_newIP=self.Quest('IP: ')
       cursor.execute("INSERT INTO `realmlist` VALUES ("+str(q_newID)+",'"+str(q_newName)+"','"+str(q_newIP)+"',"+str(q_newPort)+",1,0,1,0,0,'')")
    self.msg('\nRealm Database setup done.','green')

def setupRealm(self):
    if version=='tbc':
       vers='mangos-tbc'
    elif version=='classic':
       vers='mangos-classic'
    elif version=='cataclysm':
       vers='server'
    elif version=='wotlk':
       vers='mangos-wotlk'
    self.msg('\nCreating New Realmd Database..','green')
    self.check_Database(self,self.q_realm)
    db = MySQLdb.connect(self.q_host,self.q_user,self.q_pass)
    cursor = db.cursor()
    cursor.execute('CREATE DATABASE `'+self.q_realm+'` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci')
    cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, LOCK TABLES ON `"+self.q_realm+"`.* TO 'mangos'@'localhost'")
    os.system('mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_realm+' < '+self.work_dir+'/'+vers+'/sql/realmd.sql')
    cursor.execute("UPDATE "+self.q_realm+".realmlist SET name = '"+str(self.realmname)+"' WHERE id = 1")
    cursor.execute("UPDATE "+self.q_realm+".realmlist SET port = '"+str(self.realmport)+"' WHERE id = 1")
    cursor.execute("UPDATE "+self.q_realm+".realmlist SET address = '"+str(self.realmip)+"' WHERE id = 1")
    self.msg('\nRealm Database setup done.','green')

def setupChar(self):
    if self.version=='tbc':
       vers='mangos-tbc'
    elif self.version=='classic':
       vers='mangos-classic'
    elif self.version=='cataclysm':
       vers='server'
    elif self.version=='wotlk':
       vers='mangos-wotlk'
    self.msg('\nCreating New Characters Database..','green')
    self.check_Database(self,self.q_char)
    db = MySQLdb.connect(self.q_host,self.q_user,self.q_pass)
    cursor = db.cursor()
    cursor.execute('CREATE DATABASE `'+self.q_char+'` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci')
    cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, LOCK TABLES ON `"+self.q_char+"`.* TO 'mangos'@'localhost'")
    os.system('mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_char+' < '+self.work_dir+'/'+vers+'/sql/characters.sql')
    self.msg('\nCharacters Database setup done.','green')

def setupScriptDev2(self):
    self.msg('\nCreating New ScriptDev2 Database..','green')
    if self.version=='tbc':
       vers='mangos-tbc'
       folder='scripts'
    elif self.version=='classic':
       vers='mangos-classic'
       folder='ScriptDevZero'
    elif self.version=='cataclysm':
       vers='server'
       folder='ScriptDev2'
    elif self.version=='wotlk':
       vers='mangos-wotlk'
       folder='ScriptDev2'
    self.check_Database(self,self.q_script)
    db = MySQLdb.connect(self.q_host,self.q_user,self.q_pass)
    cursor = db.cursor()
    cursor.execute('CREATE DATABASE `'+self.q_script+'` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci')
    cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, LOCK TABLES ON `"+self.q_script+"`.* TO 'mangos'@'localhost'")
    os.system('mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_script+' < '+self.work_dir+'/'+vers+'/src/bindings/ScriptDev2/sql/scriptdev2_create_structure_mysql.sql')
    os.system('mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_script+' < '+self.work_dir+'/'+vers+'/src/bindings/ScriptDev2/sql/scriptdev2_script_full.sql')
    self.msg('\nScriptDev2 Database setup done.','green')

def setupYTDB(self,version):
    if self.version=='cataclysm':
       vers='server'
    elif self.version=='wotlk':
       vers='Wotlk'
       folder='mangos-wotlk'
    elif self.version=='tbc':
       vers='mangos-tbc'
    elif self.version=='classic':
       vers='mangos-classic'
    self.msg('\nPreparing MySQL-Server.','green')
    db = MySQLdb.connect(self.q_host,self.q_user,self.q_pass)
    cursor = db.cursor()
    cursor.execute("SELECT user FROM mysql.user WHERE user='mangos'")
    result = cursor.fetchall()
    if not result:
       cursor.execute("CREATE USER 'mangos'@'localhost' IDENTIFIED BY 'mangos'")
    else:
       print self.colored("MySQL User: mangos@localhost already exists!",'red')
    self.check_Database(self,self.q_world)
    cursor.execute('CREATE DATABASE `'+self.q_world+'` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci')
    cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, LOCK TABLES ON `"+self.q_world+"`.* TO 'mangos'@'localhost'")  
    print self.colored("\nPreparing Databases...",'green')
    os.system('mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_world+' < '+self.work_dir+'/'+folder+'/sql/mangos.sql')
    print self.colored("\nCreateing full database..",'green')
    os.system('cd '+self.install_dir+'/database/'+vers+'/R63;7za e *.7z')
    os.system('cd '+self.install_dir+'/database/'+vers+'/R63;mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_world+' < YTDB_0.14.6_R630_MaNGOS_R12214_SD2_R2737_ACID_R310_RuDB_R56.sql') 
    print self.colored("\nWorld Database setup done.",'green')
    
 
def MaNGOS_Database(self):
    if self.version=='cataclysm':
       vers='server'
    elif self.version=='wotlk':
       vers='mangos-wotlk'
    elif self.version=='tbc':
       vers='mangos-tbc'
    elif self.version=='classic':
       vers='mangos-classic'
    self.msg('\nPreparing MySQL-Server.','green')
    db = MySQLdb.connect(self.q_host,self.q_user,self.q_pass)
    cursor = db.cursor()
    cursor.execute("SELECT user FROM mysql.user WHERE user='mangos'")
    result = cursor.fetchall()
    if not result:
       cursor.execute("CREATE USER 'mangos'@'localhost' IDENTIFIED BY 'mangos'")
    else:
       print self.colored("MySQL User: mangos@localhost already exists!",'red')
    self.check_Database(self,self.q_world)
    cursor.execute('CREATE DATABASE `'+self.q_world+'` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci')
    cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, LOCK TABLES ON `"+self.q_world+"`.* TO 'mangos'@'localhost'")  
    print self.colored("\nPreparing Databases...",'green')
    os.system('mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_world+' < '+self.work_dir+'/'+vers+'/sql/mangos.sql')
    print self.colored("\nCreateing full database..",'green')
    os.system('cd '+self.install_dir+'/database/database;sh make_full_db.sh')
    os.system('mysql -h '+self.q_host+' -u '+self.q_user+' -p'+self.q_pass+' '+self.q_world+' < '+self.install_dir+'/database/database/full_db.sql')
    print self.colored("\nWorld Database setup done.",'green')
