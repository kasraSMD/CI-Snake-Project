from collections import deque
from Algorithm import Algorithm


class BFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)
        self.explored_set = None

    def run_algorithm(self, snake):
        self.frontier = deque([])
        self.path = []
        self.explored_set = []

        init, final = self.get_initstate_and_goalstate(snake)


        self.frontier.append(init)


        while 0<len(self.frontier):


            c = self.frontier.popleft()

            self.explored_set.append(c)


            n = self.get_neighbors(c)



            for i in n:

                if   self.inside_body(snake, i) or self.outside_boundary(i):


                    self.explored_set.append(i)


                    continue

                if i not in self.frontier and i not in self.explored_set :

                    self.explored_set.append(i)
                    i.parent = c
                    self.frontier.append(i)


                    if i.equal(final):
                        return self.get_path(i)


        return None
