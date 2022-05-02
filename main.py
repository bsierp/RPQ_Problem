from classes.Task import Task
from classes.Machine import Machine
import timeit
import tracemalloc
# import matplotlib.pyplot as plt


def func():
    task_array = []
    # fig, gnt = plt.subplots()  # initialize a plot
    # filename = input("Choose a file: ")
    filename = "test"
    f = open(filename, 'r')
    f.readline()
    # task_num = int(f.readline())

    i = 0
    for line in f:
        i += 1
        r_p = [int(s) for s in line.split() if s.isdigit()]
        task_array.append(Task(i, r_p[0], r_p[1], r_p[2]))
    f.close()
    m = Machine(task_array)
    start = timeit.default_timer()
    m.calculate()
    end = timeit.default_timer()
    print(m.c_max)
    print((end - start))
    # task_sorted = sorted(task_array)
    # heap_by_q = []
    # heap_by_r = []
    # for task in task_array:
    #     heapq.heappush(heap_by_q, (task.q, task.i))
    # c_max = 0
    # task_to_plot = []

    # for task in task_sorted:
    #     print(task.i, " ")
    #     task_sorted = sorted(task_array)
    #     # task_to_plot.append((max(c_max, task.r), task.p)) (sorted)
    #     c_max = max(max(c_max, task.r) + task.p + task.q, c_max)
    # end = timeit.default_timer()
    # print(c_max)
    # print((end - start))
    # gnt.set_ylim(0, (task_num + 1) * 10)
    # gnt.set_xlim(0, c_max)
    # gnt.set_xlabel('Chwila czasowa')
    # gnt.set_ylabel('Nr zadania')
    # yticks = []
    # for n in range(0, task_num):
    #     yticks.append(n*10+10)
    # gnt.set_yticks(yticks)
    #####################################################
    # Unsorted plotting                                 #
    #####################################################
    # yticks_unsort = []
    # for task in task_array:
    #     yticks_unsort.append(str(task.i))
    # gnt.set_yticklabels(yticks_unsort)
    # gnt.grid(True)
    # for task in task_array:
    #     task_to_plot.append((task.r, task.p))
    #     gnt.broken_barh([task_to_plot[-1]], (task.i*10-4, 8), facecolors=('tab:orange'))
    # plt.show()
    #####################################################
    # Sorted plotting                                 #
    #####################################################
    # yticks_sort = []
    # for task in task_sorted:
    #     yticks_sort.append(str(task.i))
    # gnt.set_yticklabels(yticks_sort)
    # gnt.grid(True)
    # j = 0
    # for task in task_sorted:
    #     gnt.broken_barh([task_to_plot[j]], ((j+1)*10-4, 8), facecolors=('tab:orange'))
    #     j += 1
    # plt.show()


if __name__ == '__main__':
    tracemalloc.start()
    func()
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()
