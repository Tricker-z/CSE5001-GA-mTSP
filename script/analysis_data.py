import re
import sys
import scipy.stats as stats

from pathlib import Path

folder_path = Path('res/pr226')

def parse_dist(fpath):
    global_dist_pattern = re.compile(r'^Global minimum distance: (?P<dist>\d+.\d+)$')
    res = list()
    fp = open(fpath, 'r')
    for line in fp.read().splitlines():
        matcher = global_dist_pattern.match(line)
        if matcher is None:
            continue
        dist = float(matcher.groupdict()['dist'])
        res.append(dist)
    fp.close()
    return res
    
def main():
    baseline_path = folder_path.joinpath('baseline.log')
    vns_ga_path   = folder_path.joinpath('vns-ga.log')
    
    baseline_res = parse_dist(baseline_path)
    vns_ga_res = parse_dist(vns_ga_path)
    
    print(f'Baseline average: {sum(baseline_res) / len(baseline_res)}')
    print(f'Vns-GA average: {sum(vns_ga_res) / len(vns_ga_res)}')
    
    # Wilcoxon rank sum test
    res = stats.wilcoxon(baseline_res, vns_ga_res, 
                         alternative='two-sided')
    print(f'Wilcoxon result: {res}')
    
    return 0


if __name__ == '__main__':
    sys.exit(main())