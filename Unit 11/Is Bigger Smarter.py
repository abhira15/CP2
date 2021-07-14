import sys
from itertools import count
def readnum():
    return list(map(int, sys.stdin.readline().split()))
def readcase():
    elephants = []
    num = count(1)
    while True:
        el = readnum()
        if not el:
            break
        weight, iq = el
        elephants.append((weight, iq, next(num)))
    return elephants
def sort_key(elephant):
    weight, iq, num = elephant
    return weight*10000-iq
def find_sequence(elephants):
    seq = sorted(elephants, reverse=True, key=sort_key)
    seq_len = [1 for _ in seq]
    seq_nxt = [n for n, _ in enumerate(seq)]
    for c in range(1, len(seq)):
        current_weight, current_iq, _ = seq[c] 
        for j in range(c-1, -1, -1):
            weight, iq, _ = seq[j]
            if iq >= current_iq:
                continue
            if current_weight == weight:
                if seq_len[j] > seq_len[c]:
                    seq_len[c] = seq_len[j]
                    seq_nxt[c] = seq_nxt[j]
            else:
                if seq_len[j] >= seq_len[c]:
                    seq_len[c] = seq_len[j]+1
                    seq_nxt[c] = j
    _, start = max((s, n) for n,s in enumerate(seq_len))
    longest = [start]
    while seq_nxt[longest[-1]]!=longest[-1]:
        longest.append(seq_nxt[longest[-1]])
    return [seq[e][2] for e in longest]
if __name__ == '__main__':
    elephants = readcase()
    seq = find_sequence(elephants)
    print(len(seq))
    for e in seq:
        print(e)