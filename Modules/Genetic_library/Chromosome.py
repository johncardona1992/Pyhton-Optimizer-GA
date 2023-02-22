import numbers


class Chromosome:
    __slots__ = ('_genetic_code', '_objective_function',
                 '_fitness', '_crossover_probability')

    def __init__(self, *, genetic_code, objective_function=100000, fitness=0, crossover_probability=0):
        # list type contraint for genetic_code
        if not isinstance(genetic_code, list):
            raise ValueError('genetic_code must be a list')
        # Non empty contraint for genetic_code list
        if genetic_code is None or len(genetic_code) == 0:
            raise ValueError('genetic_code cannot be empty.')
        # initialization
        self._genetic_code = genetic_code

        # Real type contraint for objective_function
        if not isinstance(objective_function, numbers.Real):
            raise ValueError('objective_function must be a real number')
        # initialization
        self._objective_function = objective_function

        # Real type contraint for fitness
        if not isinstance(fitness, numbers.Real):
            raise ValueError('fitness must be a real number')
        # initialization
        self._fitness = fitness

        # Real type contraint for crossover_probability
        if not isinstance(crossover_probability, numbers.Real):
            raise ValueError('crossover_probability must be a real number')
        # initialization
        self._crossover_probability = crossover_probability

    # getters
    @property
    def genetic_code(self):
        return self._genetic_code

    @property
    def objective_function(self):
        return self._objective_function

    @property
    def fitness(self):
        return self._fitness

    @property
    def crossover_probability(self):
        return self._crossover_probability

    # setters
    @genetic_code.setter
    def genetic_code(self, value):
        # list type contraint for genetic_code
        if not isinstance(value, list):
            raise ValueError('genetic_code must be a list')
        # Non empty contraint for genetic_code list
        if value is None or len(value) == 0:
            raise ValueError('genetic_code cannot be empty.')

    @objective_function.setter
    def objective_function(self, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('objective_function must be a real number')
        # initialization
        self._objective_function = value

    @fitness.setter
    def fitness(self, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('fitness must be a real number')
        # initialization
        self._fitness = value

    @crossover_probability.setter
    def crossover_probability(self, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('crossover_probability must be a real number')
        # initialization
        self._crossover_probability = value

    # Object representation
    def __repr__(self):
        return (f"genetic_code='{self._genetic_code}', "
                f"objective_function={self._objective_function}, "
                f"fitness={self._fitness}, "
                f"crossover_probability={self._crossover_probability})")
