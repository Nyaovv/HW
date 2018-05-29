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

Validator.add_type('email', EMailValidator)
validator = Validator.get_instance('email')
print(validator)
input()
