from Modules.Schedule import Schedule
from Modules.Agent import Agent
import numbers


class Problem:
    def __init__(self, *, agents, schedules, agentsRequired, cost):
        # list type contraint for agents
        if not isinstance(agents, list):
            raise ValueError('agents must be a list')
        # Non empty contraint for feasible_Schedules list
        if agents is None or len(agents) == 0:
            raise ValueError('agents cannot be empty.')
        # initilization
        self._agents = agents

        # list type contraint for schedules
        if not isinstance(schedules, list):
            raise ValueError('schedules must be a list')
        # Non empty contraint for feasible_Schedules list
        if schedules is None or len(schedules) == 0:
            raise ValueError('schedules cannot be empty.')
        # initilization
        self._schedules = schedules

        # list type contraint for agentsRequired
        if not isinstance(agentsRequired, list):
            raise ValueError('agentsRequired must be a list')
        # Non empty contraint for feasible_agentsRequired list
        if agentsRequired is None or len(agentsRequired) == 0:
            raise ValueError('agentsRequired cannot be empty.')
        # initilization
        self._agentsRequired = agentsRequired

        # Non empty contraint for cost
        if cost is None or len(str(cost).strip()) == 0:
            raise ValueError('cost cannot be empty.')
        # Real contraint for cost
        if not isinstance(cost, numbers.Real):
            raise ValueError('cost must be a real number.')
        # initialization
        self._cost = cost

    # getters

    @property
    def agents(self):
        return self._agents

    @property
    def schedules(self):
        return self._schedules

    @property
    def agentsRequired(self):
        return self._agentsRequired

    @property
    def cost(self):
        return self._cost

    # Object representation
    def __repr__(self):
        return (f"len(agents)='{len(self._agents)}', "
                f"len(schedules)={len(self._schedules)}, "
                f"len(agentsRequired)={len(self._agentsRequired)}, "
                f"cost={self._cost}")
