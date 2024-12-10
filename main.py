from datetime import datetime

from application.db.people import get_empoyees
from application.salary import calculate_salary

if __name__ == '__main__':
    date = datetime.date(datetime.today())

    get_empoyees('Иван Пупкин')
    calculate_salary('Сотрудник', 7, 40)

    print(f'\nТекущая дата: {date}')