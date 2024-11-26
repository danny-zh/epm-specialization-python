class MyDictionary:
    """A class that mimics dictionary behavior"""
    def __init__(self):
        self.data = {}

    def newentry(self, key, value):
        """
        Adds a new entry to the dictionary.
        :param key: The key of the entry (str).
        :param value: The value of the entry (str).
        :return: None
        """
        self.data[key] = value

    def look(self, key):
        """
        Retrieves the value for a given key.
        :param key: The key to look up (str).
        :return: The value if the key exists, or an error message (str).
        """
        return self.data.get(key, f"Can't find entry for {key}")


if __name__ == "__main__":
    d = MyDictionary()
    d.newentry("key1", "value1")
    d.newentry("key2", "value2")
    print(d.look("key1"))
    print(d.look("key3"))