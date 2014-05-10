from datetime import datetime
from collections import namedtuple

ListItem = namedtuple("ListItem", ["creator", "time_added"])

class ListaDellaSpesa:
    def __init__(self, creator=None):
        self.creator = creator
        self._list = {}
    def add(self, item, creator=None, time_added=None):
        self._list[item] = ListItem(creator or self.creator,
                                    time_added or datetime.now())
    def get(self):
        return sorted(self._list)
    def info(self, item):
        return self._list[item]
    def complete(self, text):
        for item in self._list:
            if item.lower().startswith(text.lower()):
                return item