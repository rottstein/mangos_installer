def welcome():
    greet="\n Welcome to my install script, yet another lazy mans work ;)\n This has been tested and works whit the latest rev of MaNGOS and Ubuntu 12.04\n Please dont blame me if anything goes wrong its just a help i will try to keep it updated but i still lifes irl to ;) \n anyways sit back grab a beer and relaxe and let it work!\n Enjoy! ;)"
    return greet

def Complete(version,install_dir,realmdname,realmport,realmdip):
    end="""
        Script is now done installing. you are now ready to run your server! ("""+version+""")
        Set your client realmlist to: """+realmdip+"""
        Login:
              username: administrator
              password: administrator

        Database:
              location: http://"""+realmip+"""/phpmyadmin
              username: mangos
              password: mangos
        
        Server:
              location: """+install_dir+"""
              conf_dir: """+install_dir+"""/etc

        RealmInfo:
              name: """+realmdname+"""
              port: """+realmport+"""
              ip: """+realmdip+"""
        """
    return end
