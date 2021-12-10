import os
import sys
import subprocess

from argparse import ArgumentParser
from pathlib import Path
from shlex import split


ga2path = {
    'baseline' : 'GA/baseline/main.py',
    'vns-ga'   : 'GA/vns-ga/main.py',
    'ipga'     : 'GA/IPGA/main.py'
}


def parse_args():
    parser = ArgumentParser(description='Running scirpt for Ga')
    parser.add_argument('-n', '--number', type=int, default=30,
                        help='Number of repeat runs')
    parser.add_argument('-a', '--algorithm', type=str, required=True,
                        help='GA from baseline, vns-ga, ipga')
    parser.add_argument('-i', '--input', type=Path, required=True,
                        help='Path of the input for mTSP')
    parser.add_argument('-o', '--output', type=Path, required=True,
                        help='Path of the output log file')
    return parser.parse_args()


def run(cmd, logfile):
    p = subprocess.Popen(cmd, stdout=logfile)
    return p

def main():
    args = parse_args()
    if args.algorithm not in ga2path.keys():
        raise Exception('Algorithm should select from [baseline, vns-ga, ipga')
    ga_path = ga2path[args.algorithm]
    
    log_path = args.output
    if not log_path.exists():
        log_path.parent.mkdir(parents=True, exist_ok=True)
    
    log = open(log_path, 'a+')
    cmd = f'python {ga_path} -i {args.input} -t 300'
    
    for idx in range(args.number):
        run(split(cmd), log)

    log.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())