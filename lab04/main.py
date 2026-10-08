import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    nonEmpty = sum([1 for line in lines if line.strip()])    
    print(len(records))
    print(nonEmpty-len(records))
    if records:
        best = warmest_city(records)
        print("%.1f" % average_by_city(records)[best])


main()
