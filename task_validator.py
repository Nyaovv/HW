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
                'Validator with name "{}" not found'.format(name)
            )
        return klass(name)

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ValidatorException('Validator must have a name!')

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
        if '@' in value:
            return True
        return False

#class Aa(object):
#    pass

class DateTimeValidator(Validator):
    def validate(self, value):
        value = value.split(" ")
        d_value = value[0]
        if "-" in d_value:
            d_value = d_value.split("-")
        elif "/" in d_value:
            d_value = d_value.split("/")
        elif "." in d_value:
            d_value = d_value.split(".")

        if int(d_value[0]) in range(1, 999999) and int(d_value[1]) in range(1, 13) and int(d_value[2]) in range(1, 32):
            pass #проверка с какой части начинается год
        elif int(d_value[0]) in range(1, 32) and int(d_value[1]) in range(1, 13) and int(d_value[2]) in range(1, 9999999):
            pass
        else:
            return False
        if len(value) == 2:
            t_value = value[1]
            t_value = t_value.split(":")
            #print('tval', t_value)
            #print(len(t_value))
            if len(t_value) == 2:
                if int(t_value[0]) not in range(24) or int(t_value[1]) not in range(61):
                    #print('p1')
                    return False
            elif len(t_value) == 3:
                if int(t_value[0]) not in range(24) or int(t_value[1]) not in range(61) or int(t_value[2]) not in range(61):
                    #print('p2')
                    return False
        return True


Validator.add_type('email', EMailValidator)
Validator.add_type('datetime', DateTimeValidator)
#validator = Validator.get_instance('email')
#print(validator.validate('info@itmo-it.org'))
#Validator.add_type('datetime', Aa)
