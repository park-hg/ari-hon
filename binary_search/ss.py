import heapq
n, k = 12, 2
s = '.SSSS.SS.SSS'
state = list(s)
for _ in range(k):

    heap = []
    for i in range(n):
        heapq.heappush(heap, (-state[i:i+3].count('S'), i))
    idx = heapq.heappop(heap)[1]
    state[idx:idx+3] = ['.','.','.']

print(state.count('.'))