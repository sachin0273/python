import json
import os

class file:
    def __init__(self):
        pass

    def new(self):
        filename="untitled"
        with open(filename, "x") as f:
            json.dump(self.load(), f, indent=2)
            return f

    def openf(self):
        file_name = input("please enter file name for open")
        with open(file_name, "w")as f:
            f.write(self.load())
        return f

    def close(self):
        r = self.new()
        y = self.openf()
        r.close()
        y.close()

    def save(self):
        t = self.openf()
        t.close()

    def save_as(self):
        name = input("please enter your file name or extension")
        ty=self.openf()
        os.rename = (ty,name)
        ty.close()