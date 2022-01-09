class File:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return f"<File '{self.name}'>"
    
    def __repr__(self):
        return str(self)


class Directory:
    def __init__(self, name: str, *content):
        self.name = name
        self.content = content
    
    def __str__(self):
        return f"<Dir '{self.name}'>"
    
    def __repr__(self):
        return str(self)
    
    def get_content(self) -> list:
        return self.content
    
    def get_dirs(self) -> list:
        dirs = []
        for content in self.content:
            if type(content) == Directory:
                dirs.append(content)
        return dirs

    def get_files(self) -> list:
        files = []
        for content in self.content:
            if type(content) == File:
                files.append(content)
        return files


def walk(dir: Directory, path='.') -> str:
    dirs = dir.get_dirs()
    files = dir.get_files()
    s = path
    # Basic case
    if len(files) > 0 and len(dirs) < 1: # files, no dirs
        s += '\n\t'
        for file in files:
            s += str(file) + '  '
        s += '\n'
    elif len(files) < 1 and len(dirs) < 1: # no files, no dirs
        s += '\n\t<Empty dir>'
    # Recursive case
    elif len(files) > 0 and len(dirs) > 0: # files, dirs
        s += '\n\t'
        for file in files:
            s += str(file) + '  '
        for d in dirs:
            s += '\n' + walk(d, f'{path}/{d.name}')
        s += '\n'
    elif len(files) < 1 and len(dirs) > 0: # no files, dirs
        for d in dirs:
            s += '\n' + walk(d, f'{path}/{d.name}')
        s += '\n'
    return s


# Demonstration
if __name__ == '__main__':
    test_dir = Directory('Main',
        Directory('Child1',
            Directory('C1_1',
                File('c1_1_test1.txt'), File('c1_1_test2.txt')
            ),
            Directory('C1_2',
                File('c1_2_test1.txt'), File('c1_2_test2.txt')
            ),
            Directory('C1_Empty'),
            File('c1_test.txt')
        ),
        Directory('Child2',
            Directory('C2_1',
                File('c2_1_test1.txt'), File('c2_1_test2.txt')
            ),
            Directory('C2_2',
                File('c2_2_test1.txt'), File('c2_2_test2.txt')
            ),
            Directory('C2_Empty'),
            File('c2_test.txt')
        )
    )
    print(walk(test_dir))
