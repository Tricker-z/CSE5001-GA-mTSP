import re
import sys
import scipy.stats as stats

from pathlib import Path

folder_path = Path('res/pr226')

def parse_dist(fpath):
    global_dist_pattern  = re.compile(r'^Global minimum distance: (?P<dist>\d+.\d+)$')
    running_time_pattern = re.compile(r'^Running time: (?P<time>\d+.\d+)s$')
    
    res_dist = list()
    res_time = list()
    
    fp = open(fpath, 'r')
    for line in fp.read().splitlines():
        match_dist = global_dist_pattern.match(line)
        match_time = running_time_pattern.match(line)
        
        if not match_dist is None:
            res_dist.append(float(match_dist.groupdict()['dist']))  
        
        if not match_time is None:
            res_time.append(float(match_time.groupdict()['time']))
        
    fp.close()
    return res_dist, res_time
    
def main():
    baseline_path = folder_path.joinpath('baseline.log')
    vns_ga_path   = folder_path.joinpath('vns-ga.log')
    ipga_path     = folder_path.joinpath('ipga.log')
    
    baseline_res, baseline_time = parse_dist(baseline_path)
    vns_ga_res, vns_ga_time = parse_dist(vns_ga_path)
    ipga_res, ipga_time = parse_dist(ipga_path)
    
    print(f'Baseline average dist: {sum(baseline_res) / len(baseline_res)}')
    print(f'Vns-GA average dist: {sum(vns_ga_res) / len(vns_ga_res)}')
    print(f'IPGA average dist: {sum(ipga_res) / len(ipga_res)}')
    
    print(f'Baseline average time: {sum(baseline_time) / len(baseline_time)}')
    print(f'Vns-GA average time: {sum(vns_ga_time) / len(vns_ga_time)}')
    print(f'IPGA average time: {sum(ipga_time) / len(ipga_time)}')
    
    # Wilcoxon rank sum test
    p_vns_ga = stats.ranksums(baseline_res, vns_ga_res, alternative='two-sided')
    print(f'Wilcoxon result of Vns-GA: {p_vns_ga}')

    p_ipga = stats.ranksums(baseline_res, ipga_res, alternative='two-sided')
    print(f'Wilcoxon result of IPGA: {p_ipga}')
    
    
    return 0


if __name__ == '__main__':
    sys.exit(main())