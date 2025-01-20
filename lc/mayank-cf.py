import sys
import os
from io import BytesIO, IOBase
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

def BFS(s, adj):
    level = [(s, 0)]
    frontier = [s]
    next1 = []
    cur_level = 1
    seen = {s}
    while frontier:
        ele = frontier.pop()
        level.append((ele, cur_level))
        seen.add(ele)
        for v in adj[ele]:
            if v not in seen:
                next1.append(v)
        if not frontier:
            frontier = next1
            next1 = []
            cur_level += 1
    return level

t = int(input())
for _ in range(t):
    n = int(input())
    adj_list = [[] for i in range(n+1)]
    for i in range(n-1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    children = {}
    level = BFS(1, adj_list)
    level.sort(key = lambda x:x[1], reverse=True)
    seen = set()
    for tup in level:
        node = tup[0]
        kids = 0
        for v in adj_list[node]:
            if v in seen:
                kids += children[v]
        children[node] = max(1, kids)
        seen.add(node)
    q = int(input())
    for i in range(q):
        x, y = map(int, input().split())
        ans = children[x]*children[y]
        print(ans)
