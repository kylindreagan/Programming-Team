#include <iostream>
#include <vector>
#include <cstdint>
#include <cstring>
#include <unistd.h>

class FastIO {
private:
    static constexpr int BUFFER_SIZE = 1 << 16;
    char in_buffer[BUFFER_SIZE];
    char out_buffer[BUFFER_SIZE];
    char* in_ptr;
    char* in_end;
    char* out_ptr;
    int in_fd;
    
    void refill() {
        size_t len = read(in_fd, in_buffer, BUFFER_SIZE);
        in_ptr = in_buffer;
        in_end = in_buffer + len;
    }
    
    char getchar() {
        if (in_ptr >= in_end) refill();
        return *in_ptr++;
    }
    
public:
    FastIO() : in_ptr(in_buffer), in_end(in_buffer), out_ptr(out_buffer), in_fd(STDIN_FILENO) {
        memset(in_buffer, 0, BUFFER_SIZE);
        memset(out_buffer, 0, BUFFER_SIZE);
    }
    
    ~FastIO() {
        flush();
    }
    
    int read_int() {
        char c;
        while ((c = getchar()) <= ' ') {}
        int val = 0;
        bool neg = false;
        
        if (c == '-') {
            neg = true;
            c = getchar();
        }
        
        do {
            val = val * 10 + (c - '0');
        } while ((c = getchar()) >= '0' && c <= '9');
        
        return neg ? -val : val;
    }
    
    char read_char() {
        char c;
        while ((c = getchar()) <= ' ') {}
        return c;
    }
    
    void write_int(int32_t x) {
        if (x < 0) {
            *out_ptr++ = '-';
            x = -x;
        }
        
        char buffer[12];
        char* ptr = buffer + 11;
        *ptr = '\0';
        
        do {
            *--ptr = '0' + (x % 10);
            x /= 10;
        } while (x);
        
        size_t len = buffer + 11 - ptr;
        if (out_ptr - out_buffer + len > BUFFER_SIZE - 32) {
            flush();
        }
        
        memcpy(out_ptr, ptr, len);
        out_ptr += len;
        *out_ptr++ = '\n';
    }
    
    void flush() {
        if (out_ptr > out_buffer) {
            write(STDOUT_FILENO, out_buffer, out_ptr - out_buffer);
            out_ptr = out_buffer;
        }
    }
};

class UltraUFDS {
private:
    std::vector<int32_t> parent;
    std::vector<int32_t> next;
    std::vector<int32_t> head;
    std::vector<int32_t> tail;
    
public:
    UltraUFDS(int32_t N) : parent(N), next(N), head(N), tail(N) {
        #pragma omp parallel for if(N > 10000)
        for (int32_t i = 0; i < N; ++i) {
            parent[i] = i;
            head[i] = i;
            tail[i] = i;
            next[i] = (i + 1 < N) ? i + 1 : -1;
        }
    }
    
    // Force inline for critical path
    __attribute__((always_inline)) 
    int32_t find_set(int32_t i) noexcept {
        // Path splitting
        while (parent[i] != i) {
            int32_t p = parent[i];
            parent[i] = parent[p];
            i = p;
        }
        return i;
    }
    
    __attribute__((always_inline))
    void union_sets(int32_t i, int32_t j) noexcept {
        if (__builtin_expect(i == j, 0)) return;
        
        int32_t x = find_set(i);
        int32_t y = find_set(j);
        if (__builtin_expect(x == y, 0)) return;
        
        parent[y] = x;
        
        int32_t tx = tail[x];
        int32_t hy = head[y];
        
        if (__builtin_expect(tx >= 0 && hy >= 0, 1)) {
            next[tx] = hy;
            tail[x] = tail[y];
        }
        
        head[y] = -1;
        tail[y] = -1;
    }
    
    std::vector<int32_t> balkanize(int32_t x) {
        int32_t root = find_set(x);
        int32_t h = head[root];
        
        if (__builtin_expect(head[root] == root && tail[root] == root, 0)) {
            if (x == root) {
                std::vector<int32_t> result;
                result.reserve(1);
                result.push_back(x);
                return result;
            }
            return {};
        }
        
        // Pre-allocate with estimated size
        int32_t t = tail[root];
        int32_t size_estimate = t - h + 1;
        std::vector<int32_t> members;
        members.reserve(size_estimate > 0 ? size_estimate : 32);
        
        int32_t curr = h;
        while (true) {
            members.push_back(curr);
            if (curr == t) break;
            curr = next[curr];
        }
        
        const int32_t n = static_cast<int32_t>(parent.size());
        for (int32_t u : members) {
            parent[u] = u;
            head[u] = u;
            tail[u] = u;
            next[u] = (u + 1 < n) ? u + 1 : -1;
        }
        
        return members;
    }
};

int main() {
    FastIO io;
    
    int32_t n = io.read_int();
    int32_t q = io.read_int();
    
    UltraUFDS ufds(n);
    
    for (int32_t i = 0; i < q; ++i) {
        char cmd = io.read_char();
        
        if (cmd == 'a') {
            int32_t x = io.read_int() - 1;
            int32_t y = io.read_int() - 1;
            ufds.union_sets(x, y);
        }
        else if (cmd == 'b') {
            int32_t x = io.read_int() - 1;
            ufds.balkanize(x);
        }
        else { 
            // cmd == 'c'
            int32_t x = io.read_int() - 1;
            io.write_int(ufds.find_set(x) + 1);
        }
    }
    
    return 0;
}