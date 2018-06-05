from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

class Menu(object):

    def __init__(self):
        pass

    commands = {}

    @classmethod
    def add_command(cls, name, klass):
        if not name:
            raise CommandException('Command must have a name!')
        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))
        cls.commands[name] = klass

    def get_all_commands(self):
        return self.commands

    def execute(cls, name, *args, **kwargs):
        if name not in cls.commands:
            raise CommandException(
            'Command with name "{}" not found'.format(name)
            )

        ex = cls.commands.get(name)
        ex(*args, **kwargs).execute(*args, **kwargs)


class CommandException(Exception):
    pass


class SupaMenu(Command):
    def execute(self):
        print('SupaMenu')

class Add_task(Command):
    def execute(self):
        print('add_Task')

class Done_task(Command):
    def execute(self, i):
        b = i + 1
        print(b)

menu = Menu()

menu.add_command('supamenu', SupaMenu)
#print(menu.commands)
menu.add_command('add_task', Add_task)
#print(menu.commands)
menu.add_command('done_task', Done_task)
#print(menu.commands)

menu.execute('add_task')
menu.execute('supamenu')
menu.execute('done_task', 1)

#print(len(menu.commands))

limit = len(menu.commands)
#print('limiiii ', limit)

#print('p', menu.__next__())
#print('a', menu.__next__())
#print('c', menu.__next__())

"""
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
"""
