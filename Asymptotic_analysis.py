import time
import gc
import math
import matplotlib.pyplot as plt


def compute_sum(n: int) -> int:

    total = 0
    for i in range(1, n):
        for j in range(i, n):
            for k in range(j * j, n):
                total += i * j * k
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
        elapsed_ns = time.perf_counter_ns() - start_ns
        ns.append(n)
        times.append(elapsed_ns)
        sums.append(s)
        print(f"n={n:>5}  time={elapsed_ns:>12}ns  Sum={s}")
    return ns, times, sums


if __name__ == "__main__":
    # Choose n values that finish quickly but show growth. Adjust as needed.
    n_values = [20, 300, 650, 1000, 2500, 4900, 8000, 12500, 17500, 23900, 30000]

    ns, times, sums = run_experiment(n_values)

    # Calculate theoretical values and scaling constant
    # Raw theoretical (units): n^2; Adjusted theoretical (ns): c * n^2
    # c = experimental_time / n^2 for the first data point
    raw_theoretical = [n ** 2 for n in ns]
    scaling_constant = times[0] / raw_theoretical[0]
    theoretical_times = [scaling_constant * t for t in raw_theoretical]
    
    print(f"\nScaling constant (c) for O(n^2): {scaling_constant:.2e}")
    print(f"\nComparison of Experimental vs Theoretical:")
    print(f"{'n':>8} {'Experimental (ns)':>18} {'Theoretical n^2 (units)':>18} {'Adjusted Theoretical (ns)':>18} {'Ratio':>10}")
    print("-" * 90)
    for i, n in enumerate(ns):
        ratio = times[i] / theoretical_times[i] if theoretical_times[i] > 0 else 0
        print(f"{n:>8} {times[i]:>18} {raw_theoretical[i]:>18} {theoretical_times[i]:>18.0f} {ratio:>10.2f}")

    # Log-log scale plot: Experimental vs Theoretical O(n^2)
    plt.figure(figsize=(8, 6))
    
    # Experimental data
    plt.plot(ns, times, 'ro-', linewidth=2, markersize=6, label='Experimental')
    
    # Theoretical O(n^2) reference
    plt.plot(ns, theoretical_times, 'bs--', linewidth=2, markersize=6, label='Theoretical O(n^2)')
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('n (log scale)')
    plt.ylabel('time (ns, log scale)')
    plt.title('Experimental vs Theoretical O(n^2) Analysis')
    plt.grid(True, which='both', alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()
