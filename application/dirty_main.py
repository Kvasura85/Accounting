from datetime import *

from application.db.people import *
from application.salary import *

if __name__ == '__main__':
    date = datetime.date(datetime.today())

    get_empoyees('Иван Пупкин')
    calculate_salary('Сотрудник', 7, 40)

    print(f'\nТекущая дата: {date}')