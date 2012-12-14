#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 

import os
import MySQLdb

def check_Database(self,host,user,password,what_db):
    db = MySQLdb.connect(host,user,password)
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES LIKE '"+str(what_db)+"'")
    checks = cursor.fetchall()
    if not checks:
       print self.colored("\nCreating: Database["+str(what_db)+"]",'green')
    else:
       self.backupDB(self,what_db,host,user,password)

def backupDB(self,what_db,host,user,password):
    print self.colored("\nDumping Current Database["+what_db+"]",'green')
    os.system('cd '+self.backup_dir+';mysqldump -h '+host+' -u '+user+' -p'+password+' '+str(what_db)+' > '+str(what_db)+'_backup.sql')
    db = MySQLdb.connect(host,user,password)
    cursor = db.cursor()
    cursor.execute('DROP database `'+str(what_db)+'`')   

def MaNGOS_Database(self,host,user,password,install_dir,version,dbs,realmname,realmport,realmip):
    self.msg('\nPreparing MySQL-Server.','green')
    db = MySQLdb.connect(host,user,password)
    cursor = db.cursor()
    cursor.execute("SELECT user FROM mysql.user WHERE user='mangos'")
    result = cursor.fetchall()
    if not result:
       cursor.execute("CREATE USER 'mangos'@'localhost' IDENTIFIED BY 'mangos'")
    else:
       print self.colored("MySQL User: mangos@localhost already exists!",'red')
    for database in dbs:
        self.check_Database(self,host,user,password,database)
        cursor.execute('CREATE DATABASE `'+database+'` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci')
        cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, LOCK TABLES ON `"+database+"`.* TO 'mangos'@'localhost'")  
    print self.colored("\nPreparing Databases...",'green')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' '+dbs[2]+' < '+self.work_dir+'/server/sql/characters.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' '+dbs[0]+' < '+self.work_dir+'/server/sql/mangos.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' '+dbs[1]+' < '+self.work_dir+'/server/sql/realmd.sql')
    if version=='tbc':
       folder='scripts'
    elif version=='classic':
       folder='ScriptDevZero'
    elif version=='cata':
       folder='ScriptDev2'
    elif version=='wotlk':
       folder='ScriptDev2'
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' '+dbs[3]+' < '+self.work_dir+'/server/src/bindings/'+folder+'/sql/scriptdev2_create_structure_mysql.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' '+dbs[3]+' < '+self.work_dir+'/server/src/bindings/'+folder+'/sql/scriptdev2_script_full.sql')
    print self.colored("\nCreateing full database..",'green')
    os.system('cd '+install_dir+'/database/database;sh make_full_db.sh')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' '+dbs[0]+' < '+install_dir+'/database/database/full_db.sql')
    db = MySQLdb.connect(host,user,password,'realmd')
    cursor = db.cursor()
    cursor.execute("UPDATE realmlist SET name = '"+str(realmname)+"' WHERE id = 1")
    cursor.execute("UPDATE realmlist SET port = '"+str(realmport)+"' WHERE id = 1")
    cursor.execute("UPDATE realmlist SET address = '"+str(realmip)+"' WHERE id = 1")
    print self.colored("\nDatabase setup done.",'green')
