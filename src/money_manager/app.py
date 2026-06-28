'''Application-wide functions for Money Manager
'''

from typing import Any, Dict
import os
import json

from .ui import UserInterface

class Application:
    '''Main class that handles operation of app
    '''

    def __init__(self):
        self.config: Dict[str, Any] = {}

        self._load_config()
        return
    
    def _load_config(self):
        '''Load configuration from file
        '''
        
        f_dir = os.path.expanduser('~/.money_manager')
        if not os.path.exists(f_dir):
            os.makedirs(f_dir)

        f_name = 'config.json'
        f_path = os.path.join(f_dir, f_name)
        if not os.path.exists(f_path):
            self._create_config()

        return
    
    def _create_config(self):
        '''Create default configuration file
        '''
        
        return

    def run(self):
        return

    def user_interface(self):
        ui = UserInterface(self)
        return
