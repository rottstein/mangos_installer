#!/usr/bin/env python                                        
# -*- coding: cp1252 -*-                                     

import sys                                                   
sys.path.append('core/')                                     
from Main import installer                                    
progname=sys.argv[0].replace('.py','')   

work_dir='/tmp/mangos'
backup_dir='backup/'
log_file='install.log'                    

install=installer(work_dir,backup_dir,log_file)
install.main()
