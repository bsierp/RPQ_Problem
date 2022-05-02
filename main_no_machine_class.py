from classes.Task import Task
import timeit
import tracemalloc
import matplotlib.pyplot as plt
from operator import attrgetter


def func():
    task_array = []
    fig, gnt = plt.subplots()  # initialize a plot
    task_to_plot = []
    q_to_plot = []
    # filename = input("Choose a file: ")
    filename = "test"
    f = open(filename, 'r')
    task_num = int(f.readline())
    i = 0
    for line in f:  # wczytanie danych do tablicy
        i += 1
        r_p = [int(s) for s in line.split() if s.isdigit()]
        task_array.append(Task(i, r_p[0], r_p[1], r_p[2]))
    f.close()
    gnt.set_ylim(0, (task_num + 1) * 10)
    # gnt.set_xlim(0, max(task_array, key=attrgetter('q')).q + max(task_array, key=attrgetter('r')).r + 2)
    gnt.set_xlabel('Chwila czasowa')
    gnt.set_ylabel('Nr zadania')
    yticks = []
    for n in range(0, task_num):
        yticks.append(n*10+10)
    gnt.set_yticks(yticks)
    # yticks_unsort = []
    # for task in task_array:
    #     yticks_unsort.append(str(task.i))
    # gnt.set_yticklabels(yticks_unsort)
    # gnt.grid(True)
    # for task in task_array:
    #     task_to_plot.append((task.r, task.p))
    #     q_to_plot.append((task.r + task.p, task.q))
    #     gnt.broken_barh([task_to_plot[-1]], (task.i*10-4, 8), facecolors='tab:orange')
    #     gnt.broken_barh([q_to_plot[-1]], (task.i*10-4, 8), facecolors='tab:blue')
    # plt.show()
    yticks_sort = []
    tasl_sorted = []
    start = timeit.default_timer()
    optimal_task = min(task_array)
    current_time = optimal_task.r + optimal_task.p
    yticks_sort.append(str(optimal_task.i))
    task_to_plot.append((current_time - optimal_task.p, optimal_task.p))
    q_to_plot.append((current_time, optimal_task.q))
    c_max = current_time + optimal_task.q
    for j in range(len(task_array)):  # przeciążenie operatora == wymaga użycia pop() zamiast remove()
        if task_array[j] is optimal_task:
            task_array.pop(j)
            break
    for i in range(task_num-1):
        if task_array:
            current_time = max(current_time, min(task_array).r)  # korekta aktualnej chwili w razie przerwy w zadaniach
        max_q = -1
        for task in reversed(task_array):  # wyznaczenie następnego zadania z dostępnych, o największym q
            if task.r <= current_time and task.q > max_q:
                optimal_task = task
                max_q = optimal_task.q
        for j in range(len(task_array)):
            if task_array[j] is optimal_task:
                yticks_sort.append(str(task_array[j].i))
                task_to_plot.append((current_time, task_array[j].p))
                q_to_plot.append((current_time + task_array[j].p, task_array[j].q))
                task_array.pop(j)
                break
        current_time += optimal_task.p  # dostosowanie aktualnej chwili
        c_max = max(c_max, current_time+optimal_task.q)  # wyliczenie c_max
    end = timeit.default_timer()
    gnt.set_xlim(0, c_max+2)
    gnt.set_yticklabels(yticks_sort)
    gnt.grid(True)
    j = 0
    for task_i in range(task_num):
        gnt.broken_barh([task_to_plot[j]], ((j+1)*10-4, 8), facecolors='tab:orange')
        gnt.broken_barh([q_to_plot[j]], ((j+1) * 10 - 4, 8), facecolors='tab:blue')
        j += 1
    plt.text(2, (task_num + 1) * 10 + 1, f'$C_{{max}}$ = {c_max}', fontsize=12)
    plt.show()
    print(c_max)
    print(str(end - start).replace('.', ','))
    print(task_to_plot)
    print(q_to_plot)


if __name__ == "__main__":
    tracemalloc.start()
    func()
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()
