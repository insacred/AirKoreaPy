from xml.etree.ElementTree import Element


class AirCondition:
    def __init__(self, item: Element):
        self._item = item

    def __getattr__(self, item_name: str):
        try:
            found = self._item.find(item_name).text
        except AttributeError:
            raise AttributeError(item_name)
        return found

    def keys(self):
        keys = []
        for e in list(self._item):
            keys.append(e.tag)
        return keys

    def __iter__(self):
        for key in self.keys():
            yield key, getattr(self, key)

    def asdict(self):
        return dict(x for x in self)
