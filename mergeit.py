import sys


def Nothing(line):
    return len(line.strip()) == 0


with open(sys.argv[1], 'r')as f, open(sys.argv[2], 'r') as g:
    content1 = f.read()
    content2 = g.read()
    x_set = set(content1.split('\n'))
    y_set = set(content2.split('\n'))
    mergeit = set(x_set).union(y_set)
    for i in sorted(mergeit):
        if not Nothing(i):
            print(str(i).replace(' ', ''))

