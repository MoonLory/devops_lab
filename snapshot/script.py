import argparse
import datetime
import json
import psutil
import time


class Snapshot:
    num = 0

    def __init__(self):
        Snapshot.num += 1
        self.time = str(datetime.datetime.now())
        self.cpu_load = psutil.cpu_percent(interval=1, percpu=True)
        self.memory_usage = psutil.disk_usage("/")
        self.vm_usage = psutil.virtual_memory()
        self.io_info = psutil.disk_io_counters()
        self.network_info = psutil.net_io_counters()

    def __str__(self):
        return 'SNAPSHOT %d: %s: %s, %s, %s, %s, %s' % \
               (self.num, self.time, self.cpu_load, self.memory_usage,
                self.vm_usage, self.io_info, self.network_info)


class Printer:
    def write_txt(self: str, name: str):
        f = open(name, "a")
        print(self, file=f)
        f.close()

    def write_json(self: str, name: str):
        f = open(name, "a")
        print(self, file=f)
        f.close()

    def write(self: str, output: str):
        if self == "txt":
            Printer.write_txt(output, "logs.txt")
        if self == "json":
            Printer.write_json(json.dumps(output), "logs.json")


def begin():
    parser = argparse.ArgumentParser(description='Interval and format')
    parser.add_argument("-i", "--interval", type=int,
                        help='interval of snapshots, default 5 min', default=5)
    parser.add_argument("-f", "--fileformat", type=str, help="output format")

    args = parser.parse_args()
    interval = args.interval
    fileformat = args.fileformat

    while True:
        snap = Snapshot()
        Printer.write(fileformat, str(snap))
        time.sleep(interval * 60)
