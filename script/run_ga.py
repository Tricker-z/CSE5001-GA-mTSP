import sys
import subprocess

from shlex import split

RUN_NUM  = 1
LOG_PATH = "log/mtsp51/baseline.log"


def run(cmd, logfile):
    p = subprocess.Popen(cmd, stdout=logfile)
    return p


def main():
    log = open(LOG_PATH, 'a+')
    cmd = f'python GA/baseline/main.py -i data/mtsp51.txt'
    
    for idx in range(RUN_NUM):
        print(f'Running id: {idx}')
        run(split(cmd), log)

    log.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())