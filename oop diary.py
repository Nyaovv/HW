from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

class Menu(metaclass=ABCMeta):

    def __init__(self):
        self.commands = {}
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.lis = tuple(self.commands.items())
        if self.counter < len(self.commands):
            num = self.counter
            self.counter += 1
            return self.lis[num]
        else:
            raise StopIteration('No more elements')


    def add_command(self, name, klass):
        if not name:
            raise CommandException('Command must have a name!')
        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))
        self.commands[name] = klass


    def execute(self, name, *args, **kwargs):
        if name not in self.commands:
            raise CommandException(
            'Command with name "{}" not found'.format(name)
            )

        klass = self.commands.get(name)
        return klass(*args, **kwargs).execute()


class CommandException(Exception):
    pass


class SupaMenu(Command):
    def execute(self):
        pass

class Add_task(Command):
    def execute(self):
        pass

class Done_task(Command):
    def execute(self):
        pass
        #print('Done_task ', b)

#menu = Menu()


#menu.add_command('supamenu', SupaMenu)
#print(menu.commands)
#menu.add_command('add_task', Add_task)
#print(menu.commands)
#menu.add_command('done_task', Done_task)
#print(menu.commands)

#print('len ', len(menu.commands))



#print(menu.__next__())
#print(menu.__next__())
#print(menu.__next__())
#print(menu.__next__())


#menu.execute('add_task')
#menu.execute('supamenu')
#menu.execute('done_task', 1)

#print(len(menu.commands))
