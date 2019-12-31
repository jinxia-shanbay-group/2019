# ========================================================================
# FileName: stat.py
# Description:
# Author: voldikss
# GitHub: https://github.com/voldikss
# ========================================================================

import sys


def stat(fname):
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    cnt = [0] * (len(lines[0].split('|')) - 3)
    for line in lines[2:]:
        record = line.split('|')[2:-1]
        for i in range(len(record)):
            if '❌' in record[i]:
                cnt[i] += 1

    report = '|'.join([
        "",
        '总计',
        *[str(30-i) for i in cnt],
        '\n'
    ])
    f = open(fname, 'a')
    f.write(report)
    f.write(f"全员红包：{sum(cnt)}")
    f.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Argument error")
        print("Use python stat [filename]")
        exit()
    fname = sys.argv[1]
    stat(fname)

