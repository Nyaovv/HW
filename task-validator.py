from abc import ABCMeta, abstractmethod

class Validator(metaclass=ABCMeta):

    def __init__(self, source):
        pass

    @abstractmethod
    def validate(self, value):
        pass

    types = {}

    @classmethod
    def get_instance(cls, name):
        klass = cls.types.get(name)
        if klass is None:
            raise ValidatorException(
            'Klass "{}" not found!'.format(klass)
            )
        return klass(name)

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ValidatorException('Type must have a name!')
        if not issubclass(klass, Validator):
            raise ValidatorException(
            'Class "{}" is not Validator!'.format(klass)
            )
        cls.types[name] = klass

class ValidatorException(Exception):
    pass

class EMailValidator(Validator):
    def validate(self, value):
        value = str(value)
        if '@' not in value:
            return False
        return True

class DateTimeValidator(Validator):
    def data_checker(self, d_value):
        if "-" in d_value:
            d_value = d_value.split("-")
        elif "/" in d_value:
            d_value = d_value.split("/")
        elif "." in d_value:
            d_value = d_value.split(".")

        if int(d_value[0]) in range(1, 9999) and int(d_value[1]) in range(1, 13) and int(d_value[2]) in range(1, 32): #проверка с какой части начинается год
            return True
        if int(d_value[0]) in range(1, 32) and int(d_value[1]) in range(1, 13) and int(d_value[2]) in range(1, 9999):
            return True
        return False

    def time_checker(self, t_value):
        t_value = t_value.split(":")
        if len(t_value) == 2:
            if int(t_value[0]) in range(24) and int(t_value[1]) in range(61):
                return True
        elif len(t_value) == 3:
            if int(t_value[0]) in range(24) and int(t_value[1]) in range(61) and int(t_value[2]) in range(61):
                return True
        return False

    def validate(self, value):
        value = value.split(" ")
        if len(value) == 1:
            if self.data_checker(value[0]):
                return True
        if len(value) == 2:
            if self.data_checker(value[0]) and self.time_checker(value[1]):
                #print('t2')
                return True
        return True
