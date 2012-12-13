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
       backupDB(self.backup_dir,what_db,host,user,password)


def backupDB(self.backup_dir,what_db,host,user,password):
    print "\nDumping Current Database["+what_db+"]"
    os.system('cd '+self.backup_dir+';mysqldump -h '+host+' -u '+user+' -p'+password+' '+str(what_db)+' > '+str(what_db)+'_backup.sql')
    db = MySQLdb.connect(host,user,password)
    cursor = db.cursor()
    cursor.execute('DROP database `'+str(what_db)+'`')   

def MaNGOS_Database(self,host,user,password,install_dir,version):  
        for database in defaultDB:
            check_Database(host,user,password,install_dir,database)
        print "\nPreparing Databases..."
        os.system('mysql -h '+host+' -u '+user+' -p'+password+' < '+work_dir+'/server/sql/create_mysql.sql')
        os.system('mysql -h '+host+' -u '+user+' -p'+password+' characters < '+work_dir+'/server/sql/characters.sql')
        os.system('mysql -h '+host+' -u '+user+' -p'+password+' mangos < '+work_dir+'/server/sql/mangos.sql')
        os.system('mysql -h '+host+' -u '+user+' -p'+password+' realmd < '+work_dir+'/server/sql/realmd.sql')
        if version=='tbc':
          folder='scripts'
        elif version=='classic':
          folder='ScriptDevZero'
        elif version=='cata':
          folder='ScriptDev2'
        elif version=='wotlk':
          folder='ScriptDev2'
        os.system('mysql -h '+host+' -u '+user+' -p'+password+' < '+work_dir+'/server/src/bindings/'+folder+'/sql/scriptdev2_create_database.sql')
        os.system('mysql -h '+host+' -u '+user+' -p'+password+' scriptdev2 < '+work_dir+'/server/src/bindings/'+folder+'/sql/scriptdev2_create_structure_mysql.sql')
        os.system('mysql -h '+host+' -u '+user+' -p'+password+' scriptdev2 < '+work_dir+'/server/src/bindings/'+folder+'/sql/scriptdev2_script_full.sql')
        print "\nCreateing full database.."
        os.system('cd '+install_dir+'/database/database;sh make_full_db.sh')
        os.system('mysql -h '+host+' -u '+user+' -p'+password+' mangos < '+install_dir+'/database/database/full_db.sql')
        if version=='tbc':
          # Minor fix for TBC this is only temperary!
          db = MySQLdb.connect(host,user,password,'mangos')
          cursor = db.cursor()
          cursor.execute('ALTER TABLE db_version CHANGE COLUMN required_12195_02_mangos_mangos_string required_s1718_12113_01_mangos_spell_template bit')
        print "\nDatabase setup done."
