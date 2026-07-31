from config import STORAGE
from storage.JSONStorage import JsonStorage


class StorageManager:

    @staticmethod
    def get_storage():

        storages = {
            "json": JsonStorage(),
            # "sqlite": SQLiteStorage(),
        }

        if STORAGE in storages:
            print(storages[STORAGE])
            return storages[STORAGE]

        raise ValueError(f"Unsupported storage: {STORAGE}")
        