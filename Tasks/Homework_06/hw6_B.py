import sys

class CommonProperties:
    @property
    def size(self):
        return len(self.data)

    @property
    def min_value(self):
        if isinstance(self.data, dict):
            return self._dict_min_value()
        try:
            return min(self.data)
        except ValueError:
            return None

    @property
    def max_value(self):
        if isinstance(self.data, dict):
            return self._dict_max_value()
        try:
            return max(self.data)
        except ValueError:
            return None


class DictProperties(CommonProperties):
    def _dict_min_value(self):
        numeric_values = [v for v in self.data.values() if isinstance(v, (int, float))]
        numeric_keys = [k for k in self.data.keys() if isinstance(k, (int, float))]
        all_nums = numeric_values + numeric_keys
        return min(all_nums) if all_nums else None

    def _dict_max_value(self):
        numeric_values = [v for v in self.data.values() if isinstance(v, (int, float))]
        numeric_keys = [k for k in self.data.keys() if isinstance(k, (int, float))]
        all_nums = numeric_values + numeric_keys
        return max(all_nums) if all_nums else None


class CustomList(CommonProperties):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"My CustomList data {self.data}"


class CustomDict(DictProperties):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"My CustomDict data {self.data}"


exec(sys.stdin.read())
