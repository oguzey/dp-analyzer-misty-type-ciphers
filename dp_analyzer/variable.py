from enum import Enum


class TypeVariable(Enum):
    INPUT = 0
    OUTPUT = 1
    UNKNOWN = 2

    def __str__(self):
        return self._name_.capitalize()


class Variable(object):
    # __k__ - coefficient for calculation hash of Variable
    __k__ = 1000000
    __id__ = {
        TypeVariable.INPUT: 1,
        TypeVariable.OUTPUT: 1,
        TypeVariable.UNKNOWN: 1
    }
    instances = {
        TypeVariable.INPUT: [],
        TypeVariable.OUTPUT: [],
        TypeVariable.UNKNOWN: []
    }

    def __init__(self, type_var):
        super(Variable, self).__init__()
        Variable.instances[type_var].append(self)
        self.__id = Variable.__id__[type_var]
        Variable.__id__[type_var] += 1
        self.__type = type_var
        self.__is_zero = False

    def __eq__(self, other):
        return self.__type == other.__type and self.__id == other.__id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if self.__type != other.__type:
            raise Exception("Compare two different types of Variables")
        return self.__id > other.__id

    def __str__(self):
        return "{} var: {} ".format(str(self.__type), self.__id)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return Variable.__k__ * int(self.__type.value) + self.__id

    def set_to_zero(self):
        self.__is_zero = True

    def is_zero(self):
        return self.__is_zero

    def is_unknown(self):
        return self.__type == TypeVariable.UNKNOWN

    def is_input(self):
        return self.__type == TypeVariable.INPUT

    def is_output(self):
        return self.__type == TypeVariable.OUTPUT

    def is_as_type(self, type_var):
        return self.__type == type_var

    def reset(self):
        self.__is_zero = False

    def get_id(self):
        return self.__id
