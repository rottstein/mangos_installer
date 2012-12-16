def welcome():
    greet="\n Welcome to my install script, yet another lazy mans work ;)\n This has been tested and works whit the latest rev of MaNGOS and Ubuntu 12.04\n Please dont blame me if anything goes wrong its just a help i will try to keep it updated but i still lifes irl to ;) \n anyways sit back grab a beer and relaxe and let it work!\n Enjoy! ;)"
    return greet

def Complete(version):
    end="""
        Script is now done installing. you are now ready to run your server! ("""+version+""")
        Set your client realmlist to: """+self.realmip+"""
        Login:
              username: administrator
              password: administrator

        Database:
              location: http://"""+self.realmip+"""/phpmyadmin
              username: mangos
              password: mangos
        
        Server:
              location: """+self.install_dir+"""
              conf_dir: """+self.install_dir+"""/etc

        RealmInfo:
              name: """+self.realmname+"""
              port: """+self.realmport+"""
              ip: """+self.realmip+"""
        """
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
