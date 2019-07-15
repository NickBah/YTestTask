class Asessor:

    def __init__(self,userID):
        """Идентификатор судьи"""
        self.UserID = userID

        """Количество выставленных оценок"""
        self.JudgementCount = 0

        """Количество неверных оценок"""
        self.MistakesCount = 0

    @property
    def CoeffCorrect(self):
        """Коэффициент верных оценок судьи [0,1]"""

        if (self.JudgementCount == 0):
            return 0

        return 1 - (self.MistakesCount / self.JudgementCount)

    def __str__(self):
        return '[{:0>3}][{:.4}]'.format(self.UserID,self.CoeffCorrect)