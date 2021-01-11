import atexit
import os
import json


def load(location, auto_save):
    return PicoDB(location, auto_save)


class PicoDB:
    key_string_error = TypeError('Key/name must be a string!')
    namespace_error = RuntimeError('Namespace does not exist')

    def __init__(self, location: str, auto_save: bool):
        self.db = {}
        self._auto_save = auto_save
        self.location = location

        self.load()

        atexit.register(self._autosave)

    def load(self):
        if os.path.exists(self.location):
            try:
                self.db = json.load(open(self.location, 'rt'))
            except ValueError:
                if os.stat(self.location).st_size == 0:  # Error raised because file is empty
                    self.db = {}
                else:
                    raise

    def _autosave(self):
        if self._auto_save:
            self.save()

    def save(self):
        json.dump(self.db, open(self.location, 'wt'))

    def set_ns(self, namespace):
        """
        Create namespace if not exists
        """
        if not isinstance(namespace, str):
            raise self.key_string_error

        if namespace not in self.db:
            self.db[namespace] = {}
            self._autosave()
            return True

    def delete_ns(self, namespace):
        """
        Delete namespace
        """
        if not isinstance(namespace, str):
            raise self.key_string_error

        if namespace in self.db:
            del self.db[namespace]
            self._autosave()
            return True

    def getall_ns(self):
        """
        Get all namespaces
        """
        return self.db.keys()

    def set(self, namespace, key, value):
        """
        Create/Update key in namespace
        """
        if not isinstance(namespace, str):
            raise self.key_string_error

        if not isinstance(key, str):
            raise self.key_string_error

        if namespace not in self.db:
            raise self.namespace_error

        self.db[namespace][key] = value
        self._autosave()
        return True

    def get(self, namespace, key):
        """
        Get the value of a key
        """
        if not isinstance(namespace, str):
            raise self.key_string_error

        if not isinstance(key, str):
            raise self.key_string_error

        if namespace not in self.db:
            raise self.namespace_error

        return self.db[namespace].get(key, None)

    def getall(self, namespace):
        """
        Get all keys from namespace
        """
        if not isinstance(namespace, str):
            raise self.key_string_error

        if namespace not in self.db:
            raise self.namespace_error

        return self.db[namespace].keys()

    def delete(self, namespace, key):
        """
        Delete key from namespace
        """
        if not isinstance(namespace, str):
            raise self.key_string_error

        if not isinstance(key, str):
            raise self.key_string_error

        if namespace not in self.db:
            raise self.namespace_error

        if key not in self.db[namespace]:
            return False

        del self.db[namespace][key]
        self._autosave()
        return True
