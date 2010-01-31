# This code is licensed under the New BSD License
# 2009, Alexander Artemenko <svetlyak.40wt@gmail.com>
# For other contacts, visit http://aartemenko.com



def _wrap(value):
    """Wraps value in a new AttributedDict or AttributedList."""
    if isinstance(value, dict):
        return AttributedDict(value)
    elif isinstance(value, list):
        return AttributedList(value)
    return value


class AttributedDict(object):
    def __init__(self, d):
        self._data = d


    def __getattr__(self, name):
        return _wrap(self._data[name])


    def __setattr__(self, name, value):
        if name == '_data':
            self.__dict__[name] = value
        else:
            self._data[name] = value


    def __delattr__(self, name):
        self._data.__delitem__(name)


    def __getitem__(self, name): return self.__getattr__(name)
    def __setitem__(self, name, value): self.__setattr__(name, value)


    def __eq__(self, d):
        if isinstance(d, AttributedDict):
            return self._data == d._data
        else:
            return self._data == d


    def __ne__(self, d):
        return not self.__eq__(d)

    def __iter__(self):
        return self._data.__iter__()

    def iteritems(self):
        for key, value in self._data.iteritems():
            yield (key, _wrap(value))

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return "<'AttributedDict' %s>" % self._data


class AttributedList(object):
    def __init__(self, l):
        self._data = l


    def __getitem__(self, index):
        return _wrap(self._data[index])


    def __eq__(self, l):
        if isinstance(l, AttributedList):
            return self._data == l._data
        else:
            return self._data == l


    def __ne__(self, l):
        return not self.__eq__(l)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return "<'AttributedList' %s>" % self._data
