from select import select


class RouletteABC(select):
    @classmethod
    def roulette(cls, population: [], accumulated_relative_fitness: [],rs: []) -> []:
        to_return=[]
        # See individuals that check condition
        for r in rs:
            if r <= accumulated_relative_fitness[0]:
                to_return.append(population[0])
                break

            for i in range(1, len(accumulated_relative_fitness)):
                if accumulated_relative_fitness[i - 1] < r and r <= accumulated_relative_fitness[i]:
                    to_return.append(population[i])
                    break
        return to_return