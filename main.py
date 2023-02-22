import pandas as pd
import numpy as np
from Modules.Schedule import Schedule
from Modules.Agent import Agent
from Modules.Problem import Problem
from Modules.Genetic_library.Genetic import Genetic
import time


def initData():
    # 1. ETL process
    # cost
    data_global = pd.read_csv('../MILP/Global_parameters.csv')
    # Agent data
    data_A = pd.read_csv('../MILP/A.csv')
    # Scheduling covering data
    data_E = pd.read_csv('../MILP/E.csv')
    # Feasible shifts per agent data
    data_L = pd.read_csv('../MILP/L.csv')
    # head count required per period data
    data_P = pd.read_csv('../MILP/P.csv')
    # Schedules indeces data
    data_S = pd.read_csv('../MILP/S.csv')
    data_S['index1'] = data_S.index
    # add the index id to each feasible schedule
    data_L = data_L.merge(data_S[['S_ID', 'index1']], on='S_ID', how='left')

    # instantiate list of Schedules objects
    schedules = [
        (Schedule(row.S_ID, data_E.query("S_ID == @row.S_ID")
                  ['E_value'].values.tolist())) for index, row in data_S.iterrows()
    ]

    # instantiate list of Agents objects
    agents = [
        (Agent(row.A_ID, data_L.query("A_ID == @row.A_ID")
               ['S_ID'].values.tolist(), data_L.query("A_ID == @row.A_ID")
               ['index1'].values.tolist())) for index, row in data_A.iterrows()
    ]

    # instantiate list of Agents required by period of the day.
    agentsRequired = data_P['REQ'].values.tolist()

    # unfulfilled demand cost
    cost = data_global.query("Parameter == 'CostUnder'")[
        'Value'].values.tolist()[0]

    problem = Problem(agents=agents, schedules=schedules,
                      agentsRequired=agentsRequired, cost=cost)
    return problem


def main():
    # initilize the data
    problem = initData()

    # initilize Genetic algorithm
    genetic = Genetic(chromosome_length=len(
        problem.agents), mutation_propability=0.005, population_length=100, generations=1000)

    # initilize population
    genetic.initilize_population(agents=problem.agents)

    # start creating generations
    for i in range(genetic.generations):
        # calculate fitness
        genetic.calculate_fitness(problem=problem)
        # crossover
        genetic.crossover()
        # mutation
        genetic.mutation(agents=problem.agents)
        # elitism
        genetic.elite()
        print(
            f'Generation: {i}, Objective: {genetic.highlander.objective_function}')

    # output results
    data_Output = pd.read_csv('../MILP/A.csv')
    data_Output = data_Output[["A_ID"]]
    final_schedules = [s.schedule_id for s in genetic.highlander.genetic_code]
    data_Output['S_ID'] = final_schedules
    data_Output['x_value'] = [1 for _ in range(genetic.chromosome_length)]
    data_Output.to_csv('../MILP/result.csv', index=False)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f"optimized in {finish -start:0.4f} seconds")
