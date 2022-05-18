class FileReader:

    def __init__(self, file):
        self.file = file
        print(f'Opening file: {self.file}')

    def read_next_line(self):
        print('Reading line...')
        raise IOError()
        return 'File line'

    def close(self):
        print('Closing file.')

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        print("closing file")
