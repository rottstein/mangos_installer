#!/usr/bin/env python                                        
# -*- coding: cp1252 -*-                                     

import sys                                                   
sys.path.append('core/')                                     
from Main import installer                                    
progname=sys.argv[0].replace('.py','')   

work_dir='/tmp/mangos'
backup_dir='backup/'
log_file='install.log'

cmd_install='sudo apt-get install'                    

install=installer(work_dir,backup_dir,log_file,cmd_install)
install.main()
