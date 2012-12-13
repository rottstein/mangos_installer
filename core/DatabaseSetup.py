#!/usr/bin/env python                                        
# -*- coding: cp1252 -*- 

import os
import MySQLdb

def check_Database(host,user,password,what_db):
    db = MySQLdb.connect(host,user,password)
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES LIKE '"+str(what_db)+"'")
    checks = cursor.fetchall()
    if not checks:
       print "\nCreating: Database["+str(what_db)+"]"
    else:
       backupDB(self,what_db,host,user,password)


def backupDB(self,what_db,host,user,password):
    print "\nDumping Current Database["+what_db+"]"
    os.system('cd '+self.backup_dir+';mysqldump -h '+host+' -u '+user+' -p'+password+' '+str(what_db)+' > '+str(what_db)+'_backup.sql')
    db = MySQLdb.connect(host,user,password)
    cursor = db.cursor()
    cursor.execute('DROP database `'+str(what_db)+'`')   

def MaNGOS_Database(self,host,user,password,install_dir,version,dbs):
    self.msg('\nPreparing MySQL-Server.')
    db = MySQLdb.connect(q_host,q_user,q_pass)
    cursor = db.cursor()
    cursor.execute("SELECT user FROM mysql.user WHERE user='mangos'")
    result = cursor.fetchall()
    if not result:
       cursor.execute("CREATE USER 'mangos'@'localhost' IDENTIFIED BY 'mangos'")
    else:
       print "MySQL User: mangos@localhost already exists!"
    for database in dbs:
        self.check_Database(q_host,q_user,q_pass,database)
        cursor.execute('CREATE DATABASE `'+database+'` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci')
        cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, LOCK TABLES ON `"+database+"`.* TO 'mangos'@'localhost'")  
    print "\nPreparing Databases..."
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' characters < '+self.work_dir+'/server/sql/characters.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' mangos < '+self.work_dir+'/server/sql/mangos.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' realmd < '+self.work_dir+'/server/sql/realmd.sql')
    if version=='tbc':
       folder='scripts'
    elif version=='classic':
       folder='ScriptDevZero'
    elif version=='cata':
       folder='ScriptDev2'
    elif version=='wotlk':
       folder='ScriptDev2'
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' scriptdev2 < '+self.work_dir+'/server/src/bindings/'+folder+'/sql/scriptdev2_create_structure_mysql.sql')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' scriptdev2 < '+self.work_dir+'/server/src/bindings/'+folder+'/sql/scriptdev2_script_full.sql')
    print "\nCreateing full database.."
    os.system('cd '+install_dir+'/database/database;sh make_full_db.sh')
    os.system('mysql -h '+host+' -u '+user+' -p'+password+' mangos < '+install_dir+'/database/database/full_db.sql')
    print "\nDatabase setup done."
