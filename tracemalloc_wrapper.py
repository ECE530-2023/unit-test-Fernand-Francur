import tracemalloc

snapshots = []

def snapshot_wrap():
    snapshots.append(tracemalloc.take_snapshot())

def check_stats(num):
    stats = snapshots[0].statistics('filename')
    print("\n<<< top " + str(num) + " stats >>>")
    for i in stats[:5]:
        print(i)

def compare_wrap(num):
    for snap in snapshots[1:]:
        stats = snap.compare_to(snapshots[0], 'lineno')
        print("\n<<< top " + str(num) + " stats >>>")
        for i in stats[:num]:
            print(i)

def clear_snapshots():
    snapshots = []
