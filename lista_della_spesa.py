from datetime import datetime
from collections import namedtuple

ListItem = namedtuple("ListItem", ["value", "user", "time_added"])
ReplacedListItem = namedtuple("ReplacedListItem", ["value", "user", "time_added", "original"])

class ListaDellaSpesa:
    def __init__(self, user=None):
        self.user = user
        self._list = {}
    def add(self, item, user=None, time_added=None):
        self._list[item] = ListItem(item,
                                    user or self.user,
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
    def replace(self, old, new, user=None, time_added=None):
        self._list[new] = ReplacedListItem(new,
                                    user or self.user,
                                    time_added or datetime.now(),
                                    ListItem(*self._list[old][:3]))
        del self._list[old]
