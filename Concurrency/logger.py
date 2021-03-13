import os

class FileLogger:
    def __init__(self,log_name):
        # if not os.path.exists(f"log/{log_name}.txt"):
        self.f = open(f"log/{log_name}.txt", "w", encoding="utf8")

    def make_log_dir(self):
        if not os.path.isdir("log"):
            os.mkdir("log")

    def start_logging(self,log_name):
        self.f.write("기록이 시작됩니다.\n")

    def write(self,start,end):
        from datetime import datetime
        stamp=str(datetime.now())
        log_line=stamp+'\t'+'start:'+f'%.5f'%start+'  '+'end:'+f'%.5f'%end+'\n'
        self.f.write(log_line)

    def finish_logging(self):
        self.f.close()



