"""
This file has all the configs required
"""


cfg = None


class Config(object):

    def __init__(self) -> None:
        self.config = {
            
            'KEY_MAP': {
            'r': 'Rock!!',
            'p': 'Paper!!',
            's': 'Scissors!!'
            },

            'SLEEP_ENABLED': True
        }


    def get(self, key, default=None):
        
        if key in self.config:
            return self.config[key]
        
        elif default:
            return default
        
        else:
            raise AttributeError
    
    def set(self, key, value):

        if key in self.config:
            self.config[key] = value
        
        else:
            raise AttributeError


def get_config():
    
    global cfg

    if cfg is None:
        cfg = Config()
    
    return cfg
