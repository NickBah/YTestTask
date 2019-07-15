import csv
from MHandler import Handler

def main():
    file_name = "data_task3.csv"

    handler = Handler()

    with open(file_name) as file:
        reader = csv.DictReader(file, delimiter='\t')

        for line in reader:
            asessor = handler.HandleAsessor(line['uid'])
            asessor.JudgementCount += 1

            if (line['jud'] != line['cjud']):
                asessor.MistakesCount += 1

    print('Количество асессоров: {}'.format(handler.Count))

    handler.PrintTheWorst()


main()