import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    q = int(next(it))

    parent = list(range(n + 1))
    # enemy[root] = set of roots that have at least one distrust edge to this root
    enemy = [set() for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        enemy[u].add(v)
        enemy[v].add(u)

    def find(x: int) -> int:
        # iterative find with path halving
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    out = []
    for _ in range(q):
        a = int(next(it))
        b = int(next(it))
        ra = find(a)
        rb = find(b)
        # they are guaranteed to be different
        if rb in enemy[ra] or ra in enemy[rb]:
            out.append("REFUSE")
        else:
            out.append("APPROVE")
            # merge the two components
            # small‑to‑large on the enemy sets
            if len(enemy[ra]) < len(enemy[rb]):
                # merge ra into rb
                for c in enemy[ra]:
                    enemy[c].discard(ra)
                    enemy[c].add(rb)
                enemy[rb].update(enemy[ra])
                enemy[ra] = None
                parent[ra] = rb
            else:
                # merge rb into ra
                for c in enemy[rb]:
                    enemy[c].discard(rb)
                    enemy[c].add(ra)
                enemy[ra].update(enemy[rb])
                enemy[rb] = None
                parent[rb] = ra

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()