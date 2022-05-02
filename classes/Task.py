

class Task:

    def __init__(self, i, r, p, q):
        self.i = i  # nr zadania
        self.r = r  # chwila, w której dostarczono zadanie
        self.p = p  # czas trwania zadania
        self.q = q  # czas dostarczenia

    def __eq__(self, other):
        return self.r == other.r

    def __lt__(self, other):
        if self == other:
            return self.q > other.q
        else:
            return self.r < other.r
