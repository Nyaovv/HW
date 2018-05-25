


from abc import ABCMeta, abstractmethod
import os
import pickle
import json

class ParamHandler(metaclass=ABCMeta):

    def __init__(self, source):
        self.source = source
        self.params = {}


    def add_param(self, key, value):
        self.params[key] = value


    def get_all_params(self):
        return self.params


    @abstractmethod
    def read(self):
        pass


    @abstractmethod
    def write(self):
        pass


    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerExcpetion(
            'Type "{}" not found!'.format(ext)
            )
        return klass(source, *args, **kwargs)


    types = {}


    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerExcpetion('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerExcpetion(
            'Class "{}" is not ParamHandler!'.format(klass)
            )
        cls.types[name] = klass

"""
    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerExcpetion(
            'Type "{}" not found!'.format(ext)
            )
        return klass(source, *args, **kwargs)
"""


class JsonParamHandler(ParamHandler):


    def read(self):
        with open(self.source) as f:
            for line in f:
                self.params = json.load(f)

    def write(self):
        with open(self.source) as f:
            json.dump(self.params, f)


class ParamHandlerExcpetion(Exception):
    pass


class PickleParamHandler(ParamHandler):
    def read(self):
        with open(self.source, 'rb') as f:
            self.params = pickle.load(f)


    def write(self):
        with open(self.source, 'wb') as f:
            pickle.dump(self.params, f)

ParamHandler.add_type('pickle', PickleParamHandler)
ParamHandler.add_type('json', JsonParamHandler)
config = ParamHandler.get_instance('./params.json')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write()
config = ParamHandler.get_instance('./params.pickle')
config.read() # читаем данные из текстового файла
