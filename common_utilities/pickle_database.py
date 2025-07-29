import os
import pickle


class PickleDatabase(dict):
    def __init__(self, storage_file_path: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.storage_file_path = storage_file_path
        self.load()

    def load(self) -> None:
        print(f'Loading database from {self.storage_file_path}')
        if os.path.exists(self.storage_file_path):
            with open(self.storage_file_path, "rb") as storage_file:
                data = pickle.load(storage_file)
                self.update(data)

    def save(self) -> None:
        print(f'Saving database to {self.storage_file_path}')
        with open(self.storage_file_path, "wb") as storage_file:
            # noinspection PyTypeChecker
            pickle.dump(self, storage_file)
