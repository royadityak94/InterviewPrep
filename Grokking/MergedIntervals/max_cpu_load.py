from heapq import heappop, heappush

#def compute_

class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

def find_max_cpu_load(jobs):
    # Time Complexity: O(NLogN), Space Complexity: O(N)
    jobs.sort(key=lambda task: task.start)
    cpu_tasks = []
    max_load = float('-inf')

    for idx in range(len(jobs)):
        task = jobs[idx]
        while cpu_tasks and cpu_tasks[0][0] <= task.start:
            heappop(cpu_tasks)
        heappush(cpu_tasks, (task.end, task.cpu_load))
        max_load = max(max_load, sum(map(lambda x: x[1], cpu_tasks)))

    return max_load

def main():
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
