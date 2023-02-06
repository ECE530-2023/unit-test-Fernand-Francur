import os
import subprocess
import tracemalloc
import tracemalloc_wrapper

CHECK = 5
DATA_DIS = 8

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for myfile in files:
    if myfile.endswith(".py") and myfile[0] == 'm':
        print("Linting " + myfile)
        subprocess.run(["autopep8", "--in-place", "-a", "-a", myfile])
        subprocess.run(["flake8", myfile])


print("Running Unit Tests: ")
tracemalloc.start()
for myfile in files:
    if myfile.endswith("tester.py") and myfile[0] == 'm':
        print("\n<<< Testing and tracemallocing " + myfile + " >>>")
        for i in range(5):            
            subprocess.run(["pytest", myfile])
            tracemalloc_wrapper.snapshot_wrap()
        tracemalloc_wrapper.check_stats(CHECK)
        tracemalloc_wrapper.compare_wrap(DATA_DIS)
        tracemalloc_wrapper.clear_snapshots()

        
