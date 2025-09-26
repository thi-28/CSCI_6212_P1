import time
import gc
import math
import matplotlib.pyplot as plt


def compute_sum(n: int) -> int:
    """Build arrays a, b, c per spec and compute the nested-loop Sum."""
    a = [2 ** i for i in range(1, n + 1)]
    b = [2 * i for i in range(1, n + 1)]
    c = [n * i for i in range(1, n + 1)]

    total = 0
    for i in range(1, n):
        for j in range(i, n):
            # Note: for j*j >= n, the k-loop is empty; early continue saves time.
            if j * j >= n:
                continue
            for k in range(j * j, n):
                total += a[i] * b[j] * c[k]
    return total


def run_experiment(n_values):
    """Run compute_sum for each n, measure time, and return lists (ns, times, sums)."""
    ns = []
    times = []
    sums = []
    for n in n_values:
        gc.collect()
        start_ns = time.perf_counter_ns()
        s = compute_sum(n)
        elapsed = (time.perf_counter_ns() - start_ns) / 1_000_000_000.0
        ns.append(n)
        times.append(elapsed)
        sums.append(s)
        print(f"n={n:>5}  time={elapsed:.6f}s  Sum={s}")
    return ns, times, sums


if __name__ == "__main__":
    # Choose n values that finish quickly but show growth. Adjust as needed.
    n_values = [20, 300, 650, 1000, 2500, 4900, 8000, 12500, 17500, 23900, 30000]

    ns, times, sums = run_experiment(n_values)

    # Plot time vs n (linear scale)
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(ns, times, marker='o')
    plt.xlabel('n')
    plt.ylabel('time (s)')
    plt.title('Time vs n (linear)')
    plt.grid(True)

    # Plot time vs n (log-log) for straight-line comparison if power-law
    plt.subplot(1, 2, 2)
    plt.plot(ns, times, marker='o')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('n (log)')
    plt.ylabel('time (s, log)')
    plt.title('Time vs n (log-log)')
    plt.grid(True, which='both')

    plt.tight_layout()
    plt.show()
