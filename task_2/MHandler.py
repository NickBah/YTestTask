from MAsessor import Asessor

class Handler:

    def __init__(self):
        """Список всех асессоров"""
        self.Asessors = []

    def HandleAsessor(self, login):
        """Возвращает объект асессора по Login, либо создает в случае отсуствия такового"""
        a = self.GetAsessorByID(login)

        if (a == None):
            self.Asessors.append(Asessor(login))
            return self.Asessors[-1]
        else:
            return a

    def GetAsessorByID(self, login):
        """Ищет объект асессора в общем списке"""
        for a in self.Asessors:
            if (a.Login == login):
                return a
        return None

    @property
    def Count(self):
        """Возвращает количество асессоров"""
        return len(self.Asessors)

