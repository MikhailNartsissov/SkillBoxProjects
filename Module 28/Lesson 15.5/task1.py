class File:
    def __init__(self, c_filename: str, c_mode: str) -> None:
        self.filename = c_filename
        self.mode = c_mode
        self.fileobject = None

    def __enter__(self) -> 'file':
        self.fileobject = open(self.filename, self.mode, encoding='utf-8')
        return self.fileobject

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.fileobject.close()


with File('example.txt', 'w') as file:
    file.write('Всем привет!')
