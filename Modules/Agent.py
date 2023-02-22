import numbers


class Agent:
    def __init__(self, agentID, feasible_Schedules, Scheduleindices):
        # Non empty contraint for Agent ID
        if agentID is None or len(str(agentID).strip()) == 0:
            raise ValueError('Agent ID cannot be empty.')
        # Integer contraint for Agent ID
        if not isinstance(agentID, numbers.Integral):
            raise ValueError('Agent ID must be an integer.')
        # initialization
        self._agentID = agentID

        # list type contraint for feasible_Schedules
        if not isinstance(feasible_Schedules, list):
            raise ValueError('feasible_Schedules must be a list')
        # Non empty contraint for feasible_Schedules list
        if feasible_Schedules is None or len(feasible_Schedules) == 0:
            raise ValueError('feasible_Schedules cannot be empty.')
        # initilization
        self._feasible_Schedules = feasible_Schedules

        # list type contraint for Scheduleindices
        if not isinstance(Scheduleindices, list):
            raise ValueError('Scheduleindices must be a list')
        # Non empty contraint for Scheduleindices list
        if Scheduleindices is None or len(Scheduleindices) == 0:
            raise ValueError('Scheduleindices cannot be empty.')
        # initilization
        self._Scheduleindices = Scheduleindices

    # getters
    @property
    def agentID(self):
        return self._agentID

    @property
    def feasible_Schedules(self):
        return self._feasible_Schedules

    @property
    def Scheduleindices(self):
        return self._Scheduleindices

    # Object representation
    def __repr__(self):
        return (f"agentID='{self._agentID}', "
                f"feasible_Schedules={self._feasible_Schedules}, "
                f"Scheduleindices={self._Scheduleindices})")
