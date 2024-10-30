import os
import typer

from sconfig.constat import APP_NAME

filename = os.path.join(typer.get_app_dir(APP_NAME),"config.json")

class Watcher:
    def __init__(self):
        self._cache_stamp = -1
        self.filename = filename
        
    
    def has_modified(self) -> bool:
        stamp = os.stat(self.filename).st_mtime
        if abs(stamp - self._cache_stamp) >= 10**-6:
            res = self._cache_stamp != -1
            self._cache_stamp = stamp
            return res
        
        return False