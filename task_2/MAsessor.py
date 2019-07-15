from MTask import Task

class Asessor:

    def __init__(self,login):
        """Идентификатор судьи"""
        self.Login = login

        """Задачи судьи"""
        self.Tasks = []

        """Начало работы"""
        self.StartTS = None

        """Окончание работы"""
        self.FinishTS = None

    def AssignTask(self,task_id, microtasks, assigned_ts, closed_ts):
        """Назначить судью на задачу"""
        self.Tasks.append(Task(task_id,microtasks, assigned_ts, closed_ts))

        if (self.StartTS == None or self.StartTS > self.Tasks[-1].AssignedTS):
            self.StartTS = self.Tasks[-1].AssignedTS

        if (self.FinishTS == None or self.FinishTS < self.Tasks[-1].СlosedTS):
            self.FinishTS = self.Tasks[-1].СlosedTS

    def GetReport(self):
        """Подготовить результаты работы судьи - начало работы, конец и кол-во решенных задач"""
        return '[{}] [{}]\t[{}]\t[{}]\t[{:.6}]'.format(self.Login,self.StartTS, self.FinishTS, self.TasksCount, self.GetSalaryCoeff())

    def GetSalaryCoeff(self):
        """На основании времени работы и решенных задач (в том числе, подзадач) вычислить коэфф. зарплаты за задачу"""
        ts = self.FinishTS - self.StartTS

        if (self.TasksCount == 0):
            return 0

        return (self.TasksCount / ts.total_seconds()) * 30

    @property
    def TasksCount(self):
        """Фактическое кол-во задач у судьи"""
        sum = 0
        for t in self.Tasks:
            sum += t.MicrotasksCount
        return sum