from datetime import datetime, timedelta
from collections import namedtuple

ListItem = namedtuple("ListItem", ["value", "user", "time_added"])
ReplacedListItem = namedtuple("ReplacedListItem", ["value", "user", "time_added", "original"])
PostponedListItem = namedtuple("PostponedListItem", ["value", "user", "time_postponed", "timedelta", "original"])
RecurringListItem = namedtuple("RecurringListItem", ["value", "user", "time_added", "timedelta"])

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
        self._manage_recurring_items()
        def is_active(item):
            return not isinstance(self._list[item], PostponedListItem)
        return sorted([i for i in self._list if is_active(i)])
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
    def _postpone(self, item, timedelta, user, time_postponed):
        self._list[item] =  PostponedListItem(item,
                                    user or self.user,
                                    time_postponed or datetime.now(),
                                    timedelta,
                                    ListItem(*self._list[item][:3]))
    def postpone(self, item, timedelta, user=None, time_postponed=None):
        self._postpone(item, timedelta, user, time_postponed)
    def approaching_postponed(self, current_time=None):
        current_time = current_time or datetime.now()
        for item in self._list:
            list_item = self._list[item]
            if isinstance(list_item, PostponedListItem):
                time_recurring = list_item.time_postponed + list_item.timedelta
                timedelta_before = list_item.timedelta / 4
                if (current_time + timedelta_before) > time_recurring:
                    yield item
    def recurr_postponed(self, item, user=None, current_time=None):
        list_item = self._list[item]
        if not isinstance(list_item, PostponedListItem):
            raise ValueError("Item '{}':{} is not postponed".format(item, type(list_item)))
        self._list[item] = RecurringListItem(item,
                                    user or list_item.user,
                                    current_time or datetime.now(),
                                    timedelta = list_item.timedelta)
    def _manage_recurring_items(self):
        for item in self.approaching_postponed():
            self.recurr_postponed(item)
