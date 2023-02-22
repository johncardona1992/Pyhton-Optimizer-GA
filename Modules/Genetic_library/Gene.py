import numbers


class Gene:
    __slots__ = ('_schedule_id', '_schedule_index')

    def __init__(self, *, schedule_id, schedule_index):
        # Non empty contraint for scheduleID
        if schedule_id is None or len(str(schedule_id).strip()) == 0:
            raise ValueError('schedule_id cannot be empty.')
        # initialization
        self._schedule_id = schedule_id

        # integer type contraint for schedule_index
        if not isinstance(schedule_index, numbers.Integral):
            raise ValueError('schedule_index must be an integer')
        # initialization
        self._schedule_index = schedule_index

    # getters
    @property
    def schedule_id(self):
        return self._schedule_id

    @property
    def schedule_index(self):
        return self._schedule_index

    # setters
    @schedule_id.setter
    def schedule_id(self, value):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError('schedule_id cannot be empty.')
        self._schedule_id = value

    @schedule_index.setter
    def schedule_index(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('schedule_index must be an integer.')
        self._schedule_index = value

    # Object representation
    def __repr__(self):
        return (f"schedule_id='{self._schedule_id}', "
                f"schedule_index={self._schedule_index})")
