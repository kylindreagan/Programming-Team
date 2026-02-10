#include <stdio.h>
#include <stdlib.h>

typedef long long ll;

/* ---------- Fenwick Tree (BIT) ---------- */
typedef struct {
    int n;
    ll *bit;  // 1-indexed
} Fenwick;

static Fenwick fw_new(int n) {
    Fenwick f;
    f.n = n;
    // calloc gives a 0-initialized blcok
    f.bit = (ll*)calloc((size_t)n + 1, sizeof(ll));
    if (!f.bit) exit(1);
    return f;
}

// inline functions are faster; they are converted from
// functions to inline code
static inline void fw_add(Fenwick *f, int idx0, ll delta) {
    int i = idx0 + 1;
    int n = f->n;
    ll *bit = f->bit;
    while (i <= n) {
        bit[i] += delta;
        i += i & -i;
    }
}

/* sum of a[0:idx) (idx is a length, 0..n) */
static inline ll fw_sum_prefix_excl(const Fenwick *f, int idx) {
    if (idx <= 0) return 0;
    int i = (idx >= f->n) ? f->n : idx;  // [0:idx) => i = idx
    ll s = 0;
    const ll *bit = f->bit;
    while (i > 0) {
        s += bit[i];
        i -= i & -i;
    }
    return s;
}

int main(void) {
    int T;
    scanf("%d", &T);

    while (T--) {
        int m, r;
        scanf("%d %d", &m, &r);

        int size = m + r;
        Fenwick fw = fw_new(size);

        int *pos = malloc((m + 1) * sizeof(int));

        /* Initial placement */
        for (int i = 1; i <= m; i++) {
            pos[i] = r + i - 1;
            fw_add(&fw, pos[i], 1);
        }

        int top = r - 1;  // next free top slot

        for (int i = 0; i < r; i++) {
            int a;
            scanf("%d", &a);

            ll above = fw_sum_prefix_excl(&fw, pos[a]);
            printf("%lld ", above);

            fw_add(&fw, pos[a], -1);

            pos[a] = top;
            fw_add(&fw, pos[a], 1);
            top--;
        }

        printf("\n");

        free(pos);
        free(fw.bit);
    }

    return 0;
}