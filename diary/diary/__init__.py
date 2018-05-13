import sys
import datetime

from diary import storage

get_connection = lambda: storage.connect('diary.sqlite')


def action_add_task():
    """Добавить задачу"""
    task = input('\nВведите название задачи: ')
    description = input('\nВведите описание задачи: ')
    dt_day = int(input('\nВведите число: '))
    dt_month = int(input('\nВведите месяц: '))
    dt_year = int(input('\nВведите год: '))
    dt_hour = int(input('\nВведите час: '))
    dtl = datetime.datetime(dt_year, dt_month, dt_day, dt_hour)
    with get_connection() as conn:
        storage.add_task(conn, task, description, dtl)


def action_edit_task():
    id = int(input('\nВведите номер задачи: '))
    task = input('\nВведите название задачи: ')
    description = input('\nВведите описание задачи: ')
    with get_connection() as conn:
        storage.edit_task(conn, task, description, id)


def action_done_task():
    id = int(input('\nВведите номер задачи: '))
    with get_connection() as conn:
        storage.done_task(conn, id)


def action_undone_task():
    id = int(input('\nВведите номер задачи: '))
    with get_connection() as conn:
        storage.undone_task(conn, id)


def action_show_tasks():
    """Вывести все задачи"""
    with get_connection() as conn:
        tasks = storage.find_all(conn)

    template = '{task[0]} - {task[1]} - {task[2]} - {task[3]} - {task[4]}'

    for task in tasks:
        print(template.format(task=task))



def action_show_menu():
    """Показать меню"""
    print('''
1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
m. Показать меню
q. Выход
''')


def action_exit():
    """Выйти"""
    sys.exit(0)


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    actions = {
        '1': action_show_tasks,
        '2': action_add_task,
        '3': action_edit_task,
        '4': action_done_task,
        '5': action_undone_task,
        'm': action_show_menu,
        'q': action_exit
    }

    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команда')
