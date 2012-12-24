def welcome():
    greet="\n Welcome to my install script, yet another lazy mans work ;)\n This has been tested and works whit the latest rev of MaNGOS and Ubuntu 12.04\n Please dont blame me if anything goes wrong its just a help i will try to keep it updated but i still lifes irl to ;) \n anyways sit back grab a beer and relaxe and let it work!\n Enjoy! ;)"
    return greet

def Complete(self,version):
    end="""
    MaNGOS install Done!
    The script is now done working, here all the needed information to connect to your server.
    All this info will be stored in """+self.install_dir+"""/login.info
    Enjoy! :)

    Login:
          """+self.colored('Username: ','yellow')+""""""+self.colored(str(self.q_newAcc),'green')+"""
          """+self.colored('Password: ','yellow')+""""""+self.colored(str(self.q_newAccPass),'green')+"""
          """+self.colored('GMLevel: ','yellow')+""""""+self.colored(str(self.q_newAccGM),'green')+"""

    Database:
          """+self.colored('Host: ','yellow')+""""""+self.colored('http://'+str(self.q_host)+'/phpmyadmin','green')+"""
          """+self.colored('User: ','yellow')+""""""+self.colored(str(self.q_user),'green')+"""
          """+self.colored('Pass: ','yellow')+""""""+self.colored(str(self.q_pass),'green')+"""

    Folders:
          """+self.colored('Install dir: ','yellow')+""""""+self.colored(str(self.install_dir),'green')+"""
          """+self.colored('Config dir: ','yellow')+""""""+self.colored(str(self.install_dir)+'/etc/','green')+"""

    Realm:
          """+self.colored('ID: ','yellow')+""""""+self.colored(str(self.q_realmid),'green')+"""
          """+self.colored('Name: ','yellow')+""""""+self.colored(self.q_realmname,'green')+"""
          """+self.colored('Host: ','yellow')+""""""+self.colored(self.q_realmip,'green')+"""
          """+self.colored('Port: ','yellow')+""""""+self.colored(self.q_realmport,'green')+"""
          """+self.colored('set realmlist: ','yellow')+""""""+self.colored(self.q_host,'green')+"""
        """
    os.system('echo '+end+' >> '+self.install_dir+'/login.info')
    return end

def Correct(self):
 info="""
    Collected Information.
    ----------------------
    Database:
       """+self.colored('Host: '+self.colored(self.q_host,'yellow')+'','green')+"""
       """+self.colored('User: '+self.colored(self.q_user,'yellow')+'','green')+"""
       """+self.colored('Pass: '+self.colored(self.q_pass,'red')+'','green')+"""

    """+self.colored('Realm:','green')+"""
       """+self.colored('Name: '+self.colored(self.q_realmname,'yellow')+'','green')+"""
       """+self.colored('Port: '+self.colored(self.q_realmport,'yellow')+'','green')+"""
       """+self.colored('IP: '+self.colored(self.q_realmip,'yellow')+'','green')+"""

    """+self.colored('Config:','green')+"""
       """+self.colored('Path: '+self.colored(self.install_dir,'yellow')+'','green')+"""
       """+self.colored('Data: '+self.colored(self.q_data_dir,'yellow')+'','green')+"""
       """+self.colored('ScriptDev2: '+self.colored(self.q_sd2,'yellow')+'','green')+"""
       """+self.colored('MangChat: '+self.colored(self.q_mc,'yellow')+'','green')+"""
       """+self.colored('AuctionHouseBot: '+self.colored(self.q_ahbot,'yellow')+'','green')+"""
       """+self.colored('ACID: '+self.colored(self.q_acid,'yellow')+'','green')+"""             
             """
 return info

def Correct_w(self):
 info="""
    Collected Information.
    ----------------------
    Database:
       """+self.colored('Host: '+self.colored(self.q_host,'yellow')+'','green')+"""
       """+self.colored('User: '+self.colored(self.q_user,'yellow')+'','green')+"""
       """+self.colored('Pass: '+self.colored(self.q_pass,'red')+'','green')+"""

    """+self.colored('Realm:','green')+"""
       """+self.colored('Name: '+self.colored(self.q_realmname,'yellow')+'','green')+"""
       """+self.colored('Port: '+self.colored(self.q_realmport,'yellow')+'','green')+"""
       """+self.colored('IP: '+self.colored(self.q_realmip,'yellow')+'','green')+"""

    """+self.colored('Config:','green')+"""
       """+self.colored('Path: '+self.colored(self.install_dir,'yellow')+'','green')+"""
       """+self.colored('Data: '+self.colored(self.q_data_dir,'yellow')+'','green')+"""
       """+self.colored('ScriptDev2: '+self.colored(self.q_sd2,'yellow')+'','green')+"""
       """+self.colored('AuctionHouseBot: '+self.colored(self.q_ahbot,'yellow')+'','green')+"""
       """+self.colored('ACID: '+self.colored(self.q_acid,'yellow')+'','green')+"""             
             """
 return info
