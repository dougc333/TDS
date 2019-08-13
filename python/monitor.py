from collections import Counter
import linecache
import os
import tracemalloc
from time import sleep


def count_prefixes():
    sleep(2)  # Start up time.
    counts = Counter()
    fname = '/usr/share/dict/american-english'
    with open(fname) as words:
        words = list(words)
        for word in words:
            prefix = word[:3]
            counts[prefix] += 1
            sleep(0.0001)
    most_common = counts.most_common(3)
    sleep(3)  # Shut down time.
    return most_common


def main():
    tracemalloc.start()

    most_common = count_prefixes()
    print('Top prefixes:', most_common)

    snapshot = tracemalloc.take_snapshot()
    display_top(snapshot)


def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


main()

