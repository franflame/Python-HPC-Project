import matplotlib
matplotlib.use("Agg")   

from os.path import join
import numpy as np
import matplotlib.pyplot as plt
from parallel_simulation import run_parallel

LOAD_DIR = "/dtu/projects/02613_2025/data/modified_swiss_dwellings"

# Load building IDs
with open(join(LOAD_DIR, "building_ids.txt")) as f:
    building_ids = f.read().splitlines()

# Use smaller subset for timing 
N = 50
building_ids = building_ids[:N]

workers = [1, 2, 4, 8, 16]
runtimes = []

print(f"Running benchmark with {N} floorplans")

for p in workers:
    print(f"\nRunning with {p} workers")

    t = run_parallel(building_ids, LOAD_DIR, p)

    print(f"Runtime: {t:.2f} seconds")
    runtimes.append(t)

# Compute speedups
T1 = runtimes[0]
speedups = [T1 / t for t in runtimes]

# Save results
np.savetxt(
    "timings.txt",
    np.column_stack((workers, runtimes, speedups)),
    header="workers runtime speedup"
)

# Plotting speedup results
plt.figure()
plt.plot(workers, speedups, marker="o", label="Measured")
plt.plot(workers, workers, linestyle="--", label="Ideal")

plt.xlabel("Number of workers")
plt.ylabel("Speedup")
plt.title("Parallel Speedup")
plt.grid()
plt.legend()

plt.savefig("speedup.png")

print("\nResults saved:")
print("- timings.txt")
print("- speedup.png")
