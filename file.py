import os, json

class File:
    def __init__(self, path):
        self.path = path
        self.content = []
    def read(self):
        if os.path.exists(self.path) == False:
            self.content = [""]
        else:
            with open(self.path, 'r') as file:
                for line in file:
                    self.content.append(line.strip())
                file.close()
    def save(self):
        with open(self.path, 'w') as file:
            file.writelines(self.content)
            file.close()
class JsonFile(File):
    def __init__(self, path):
        super().__init__(path)
        self.content_single = ""
        self.content_json = []
    def restruct(self):
        self.content_single = ""
        for i in self.content:
            self.content_single += i
    def read(self):
        File.read(self)
        if self.content == [""] or self.content == []:
            self.content_json = []
        else:
            self.restruct()
            try:
                self.content_json = json.loads(self.content_single)
            except json.decoder.JSONDecodeError:
                self.content_json = []
    def save(self):
        self.content = [json.dumps(self.content_json)]
        File.save(self)
