from datetime import datetime
from collections import namedtuple

ListItem = namedtuple("ListItem", ["value", "creator", "time_added"])
ReplacedListItem = namedtuple("ReplacedListItem", ["value", "creator", "time_added", "original"])

class ListaDellaSpesa:
    def __init__(self, creator=None):
        self.creator = creator
        self._list = {}
    def add(self, item, creator=None, time_added=None):
        self._list[item] = ListItem(item,
                                    creator or self.creator,
                                    time_added or datetime.now())
    def remove(self, item):
        del self._list[item]
    def get(self):
        return sorted(self._list)
    def info(self, item):
        return self._list[item]
    def complete(self, text):
        for item in self._list:
            if item.lower().startswith(text.lower()):
                yield item
    def replace(self, old, new, creator=None, time_added=None):
        self._list[new] = ReplacedListItem(new,
                                    creator or self.creator,
                                    time_added or datetime.now(),
                                    ListItem(*self._list[old][:3]))
        del self._list[old]
