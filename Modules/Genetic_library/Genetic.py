from multiprocessing.dummy import active_children
import numbers
from random import randrange, uniform
import numpy.random as npr
import math
from Modules.Genetic_library.Chromosome import Chromosome
from Modules.Genetic_library.Gene import Gene


class Genetic:
    """ Genetic Algorithm adapted to solve a Agent Scheduling problem """

    def __init__(self, *, chromosome_length, population_length=10, generations=10, mutation_propability=0):
        self._population = None
        self._highlander = None

        # Integer type contraint for chromosome_length
        if not isinstance(chromosome_length, numbers.Integral):
            raise ValueError('chromosome_length must be an integer number')
        if chromosome_length <= 0:
            raise ValueError('chromosome_length must be greater than 0')
        # initialization
        self._chromosome_length = chromosome_length

        # Integer type contraint for population_length
        if not isinstance(population_length, numbers.Integral):
            raise ValueError('population_length must be a integer number')
        if population_length <= 0:
            raise ValueError('population_length must be greater than 0')
        if not (population_length % 2) == 0:
            raise ValueError('population_length must be an even number')
        # initialization
        self._population_length = population_length

        # Integer type contraint for generations
        if not isinstance(generations, numbers.Integral):
            raise ValueError('generations must be a integer number')
        if generations <= 0:
            raise ValueError('generations must be greater than 0')
        self._generations = generations

        # Real type contraint for mutation_propability
        if not isinstance(mutation_propability, numbers.Real):
            raise ValueError('mutation_propability must be a real number')
        if not (mutation_propability >= 0 and mutation_propability <= 1):
            raise ValueError(
                'mutation_propability must be a positive number and less than 1')
        self._mutation_propability = mutation_propability

    # getters
    @property
    def population(self):
        return self._population

    @property
    def highlander(self):
        return self._highlander

    @property
    def chromosome_length(self):
        return self._chromosome_length

    @property
    def population_length(self):
        return self._population_length

    @property
    def generations(self):
        return self._generations

    @property
    def mutation_propability(self):
        return self._mutation_propability

    # setters
    @population.setter
    def population(self, value):
        # list type contraint for population
        if not isinstance(value, list):
            raise ValueError('population must be a list')
        # Non empty contraint for population list
        if value is None or len(value) == 0:
            raise ValueError('population cannot be empty.')
        self._population = value

    @highlander.setter
    def highlander(self, value):
        # Cromosome type contraint for highlander
        if not isinstance(value, Chromosome):
            raise ValueError('highlander must be a Cromosome')
        # Non empty contraint for population list
        if value is None or len(value.genetic_code) == 0:
            raise ValueError('highlander cannot be empty.')
        self._highlander = value

    @chromosome_length.setter
    def chromosome_length(self, value):
        # Integer type contraint for chromosome_length
        if not isinstance(value, numbers.Integral):
            raise ValueError('chromosome_length must be an integer number')
        if value <= 0:
            raise ValueError('chromosome_length must be greater than 0')
        self._chromosome_length = value

    @population_length.setter
    def population_length(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('population_length must be a integer number')
        if value <= 0:
            raise ValueError('population_length must be greater than 0')
        if not (value % 2) == 0:
            raise ValueError('population_length must be an even number')
        self._population_length = value

    @generations.setter
    def generations(self, value):
        # Integer type contraint for generations
        if not isinstance(value, numbers.Integral):
            raise ValueError('generations must be a integer number')
        if value <= 0:
            raise ValueError('generations must be greater than 0')
        self._generations = value

    @mutation_propability.setter
    def mutation_propability(self, value):
        # Real type contraint for mutation_propability
        if not isinstance(value, numbers.Real):
            raise ValueError('mutation_propability must be a real number')
        if not (value >= 0 and value <= 1):
            raise ValueError(
                'mutation_propability must be greater than 0 and less than 1')
        self._mutation_propability = value

    # Object representation
    def __repr__(self):
        return (f"population='{self._population}', "
                f"highlander={self._highlander}, "
                f"chromosome_length={self._chromosome_length}, "
                f"population_length={self._population_length}, "
                f"generations={self._generations}, "
                f"mutation_propability={self._mutation_propability})")

    # initialize the population of chromosomes
    def initilize_population(self, *, agents):
        # list of chromosomes
        chromo_popu = []
        for _ in range(self.population_length):
            genetic_sample = self.generate_DNA(agents=agents)
            chromo = Chromosome(genetic_code=genetic_sample)
            chromo_popu.append(chromo)
        self.population = chromo_popu

        return None

    def generate_DNA(self, *, agents):
        # list of genes
        code = []
        for a in range(self.chromosome_length):
            rand_int = randrange(len(agents[a].feasible_Schedules))
            sch_id = agents[a].feasible_Schedules[rand_int]
            sch_index = agents[a].Scheduleindices[rand_int]
            gene = Gene(schedule_id=sch_id, schedule_index=sch_index)
            code.append(gene)
        return code

    # calculate the fitness and crossover probability value for each chromosome
    def calculate_fitness(self, *, problem):
        # initilize the best chromosome
        self.highlander = Chromosome(genetic_code=[1])
        # initlize the cumulative fitness
        cumulative_fitness = 0
        for c in range(self.population_length):
            # calculate the objective function for each chromosome
            self.population[c].objective_function = self.calculateF(
                self.population[c].genetic_code, problem)
            # calculate fitness for each chromosome
            self.population[c].fitness = 1 / \
                self.population[c].objective_function
            # update cumulative fitness
            cumulative_fitness += self.population[c].fitness

            # choose the best chromosome
            if self.population[c].objective_function < self.highlander.objective_function:
                self.highlander = self.population[c]

        for c in range(self.population_length):
            # calculate thr crossover probability for each chromosome
            self.population[c].crossover_probability = self.population[c].fitness / \
                cumulative_fitness

    # calculate the objective function for a given chromosome
    def calculateF(self, genetic_code, problem):
        # initilize the objective function
        objective_function = 0
        for period in range(len(problem.agentsRequired)):
            # initlize the unfulfilled demand
            unfulfilled_demand = problem.agentsRequired[period]

            for agent in range(len(problem.agents)):
                # get the index of the schedule
                index = genetic_code[agent].schedule_index
                # get the status of the agent
                active_agent = problem.schedules[index].schedule_covering[period]
                # substract the acitive agent to the unfulfilled_demand
                unfulfilled_demand -= active_agent
                # exit for loop if the unfulfilled demand is 0
                if unfulfilled_demand <= 0:
                    break

            objective_function += unfulfilled_demand*problem.cost

        return objective_function

    # generate the new population by crossover
    def crossover(self):
        # initilize offspring
        offspring = []
        for _ in range(int(self.population_length/2)):
            # select parent 1
            parent1 = self.parent_selection()
            # select parent 2
            parent2 = self.parent_selection()

            # generate first child
            child = self.reproduction(parentID1=parent1, parentID2=parent2)
            offspring.append(child)

            # generate second child
            child = self.reproduction(parentID1=parent2, parentID2=parent1)
            offspring.append(child)

        # replace old population with offspring
        self.population = offspring

    def parent_selection(self):
        selection_probs = [c.crossover_probability for c in self.population]
        return npr.choice(len(self.population), p=selection_probs)

    def reproduction(self, *, parentID1, parentID2):
        # get the crossover point
        cross_point = math.floor(self.population_length/2)
        # initilize parents
        p1 = self.population[parentID1]
        p2 = self.population[parentID2]
        # crossover
        genetic_code_child = p1.genetic_code[:cross_point] + \
            p2.genetic_code[cross_point:]
        # create child
        child = Chromosome(genetic_code=genetic_code_child)
        return child

    def mutation(self, agents):
        for c in range(self.population_length):
            for a in range(self.chromosome_length):
                # generate random
                rnd_number = uniform(0, 1)
                if rnd_number < self.mutation_propability:
                    # mutate gene
                    self.population[c].genetic_code[a] = self.mutate(
                        gen_ID=a, agents=agents)

    def mutate(self, *, gen_ID, agents):
        # generate a new schedule
        rand_int = randrange(len(agents[gen_ID].feasible_Schedules))
        sch_id = agents[gen_ID].feasible_Schedules[rand_int]
        sch_index = agents[gen_ID].Scheduleindices[rand_int]
        gene = Gene(schedule_id=sch_id, schedule_index=sch_index)
        return gene

    def elite(self):
        # select a random child and replace it with the best parent
        child = randrange(self.population_length)
        self.population[child] = self.highlander
