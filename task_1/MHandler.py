from MAsessor import Asessor

class Handler:

    def __init__(self):
        """Список всех асессоров"""
        self.Asessors = []

    def HandleAsessor(self, userID):
        """Возвращает объект асессора по UserID, либо создает в случае отсуствия такового"""
        a = self.GetAsessorByID(userID)

        if (a == None):
            self.Asessors.append(Asessor(userID))
            return self.Asessors[-1]
        else:
            return a

    def GetAsessorByID(self, id):
        """Ищет объект асессора в общем списке"""
        for a in self.Asessors:
            if (a.UserID == id):
                return a
        return None

    @property
    def Count(self):
        """Возвращает количество асессоров"""
        return len(self.Asessors)

    def PrintTheWorst(self):
        """Выводит информацию об асессорах, которые справились хуже всех"""

        self.Asessors.sort(key=lambda x: x.CoeffCorrect)

        n = 50 if (self.Count > 50) else self.Count

        print('[{}] худших асессоров:'.format(n))

        print('\t[uID][Коэффициент верных оценок]')
        for i in range(n):
            print('\t{}'.format(self.Asessors[i]))