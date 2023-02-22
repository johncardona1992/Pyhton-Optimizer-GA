import numbers


class Schedule:
    __slots__ = ('_scheduleID', '_schedule_covering')

    def __init__(self, scheduleID, schedule_covering):
        # Non empty contraint for scheduleID
        if scheduleID is None or len(str(scheduleID).strip()) == 0:
            raise ValueError('scheduleID cannot be empty.')

        # initialization
        self._scheduleID = scheduleID

        # list type contraint for schedule_covering
        if not isinstance(schedule_covering, list):
            raise ValueError('schedule_covering must be a list')
        # Non empty contraint for schedule_covering list
        if schedule_covering is None or len(schedule_covering) == 0:
            raise ValueError('schedule_covering cannot be empty.')
        # initilization
        self._schedule_covering = schedule_covering

    # getters

    @property
    def scheduleID(self):
        return self._scheduleID

    @property
    def schedule_covering(self):
        return self._schedule_covering

    # Object representation
    def __repr__(self):
        return (f"scheduleID='{self._scheduleID}', "
                f"schedule_covering={self._schedule_covering})")
