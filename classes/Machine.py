from operator import attrgetter


class Machine:

    def __init__(self, tasks):
        self.tasks = tasks  # lista zadań do wykonania
        self.current_time = 0  # aktualna chwila
        self.c_max = 0  # wartość c_max

    def generate_available_tasks(self):
        return [i for i in range(len(self.tasks)) if self.tasks[i].r <= self.current_time]

    def pick_optimal_task(self):
        if self.current_time == 0:
            optimal_task = min(self.tasks)
            self.current_time = optimal_task.r
            self.tasks.remove(optimal_task)
            return optimal_task
        else:
            available_tasks_indexes = self.generate_available_tasks()
            available_tasks = []
            for i in available_tasks_indexes:
                available_tasks.append(self.tasks[i])
            max_q_element = max(available_tasks, key=attrgetter('q'))
            optimal_task = self.tasks[self.tasks.index(max_q_element)]
            self.tasks.pop(self.tasks.index(max_q_element))
            return optimal_task
            # max_q = 0
            # for i in available_tasks_indexes:
            #     max_q = max(max_q, self.tasks[i].q)
            # index = self.tasks.index(max_q)

    def calculate(self):
        for i in range(len(self.tasks)):
            current_task = self.pick_optimal_task()
            self.current_time += current_task.p
            self.c_max = max(self.c_max, self.current_time + current_task.q)
            if self.tasks:
                self.current_time = max(self.current_time, min(self.tasks).r)
