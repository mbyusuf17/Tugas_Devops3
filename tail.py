import sys
import time

class Tail():
    def __init__(self,file_name,callback=sys.stdout.write):
        self.file_name = file_name
        self.callback = callback
    def follow(self,n=10):
        try:
            with open(self.file_name) as f:
                self._file = f
                self.showLastLine(n)
                self._file.seek(0,2)
                while True:
                    line = self._file.readline()
                    if line:
                        self.callback(line)
        except Exception,e:
            print 'Failed to open the file. See if the file does not exist or if there is a problem with permissions'
            print e
    def showLastLine(self, n):
        last_lines = self._file.readlines()[-10:]
        for line in last_lines:
            self.callback(line)