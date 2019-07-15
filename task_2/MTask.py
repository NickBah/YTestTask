from ciso8601 import parse_datetime

class Task:

    def __init__(self, id, microtasks, assigned_ts, closed_ts):
        """Идентификатор задания"""
        self.ID = id

        """Подзадачи"""
        self.MicrotasksCount = float(microtasks)

        """Время назначения задания"""
        self.AssignedTS = parse_datetime(assigned_ts)

        """Время закрытия задания"""
        self.СlosedTS  = parse_datetime(closed_ts)

