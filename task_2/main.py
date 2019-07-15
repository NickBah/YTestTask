import csv
from MHandler import Handler

def main():
    file_name = 'data_task4_old.txt'

    handler = Handler()

    with open(file_name) as file:
        reader = csv.DictReader(file, delimiter='\t')

        for line in reader:
            asessor = handler.HandleAsessor(line['login'])
            asessor.AssignTask(line['tid'],line['Microtasks'],line['assigned_ts'],line['closed_ts'])

    print('Количество асессоров: {}'.format(handler.Count))

    print('\t[Логин]   [Начало работы]\t\t[Конец работы]\t\t[Решенные задачи]\t[Коэффициент для установления зарплаты]')
    for asessor in handler.Asessors:
        print('\t{}'.format(asessor.GetReport()))
main()