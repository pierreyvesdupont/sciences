from math import *
import random

def all_equal(iterator):
    return len(set(iterator)) <= 1

class SuiteTerm:

    def __init__(self, index, value):
        self.index = index
        self.value = value

class Suite:
    U_N = "u_n"
    N = "n"
    GLOBALS = {'sqrt': sqrt, 'pow': pow}
    TYPE_ARITHMETICAL = 0
    TYPE_GEOMETRICAL = 1

    def __init__(self, *args, **kwargs):
        self.expression_un = None
        self.expression_n = None
        self.u_zero = None
        self.first_value = None

        if len(args) == 2:
            self.init_with_expression(args[0], args[1])
        elif len(args) == 3:
            self.init_with_terms(args[0], args[1], args[2])

    def init_with_terms(self, type, u_x, u_y):
        self.expression_un = None
        self.expression_n = None
        self.u_zero = None
        self.first_value = None

        u_a = u_x
        u_b = u_y
        if u_x.index > u_y.index:
            u_a = u_y
            u_b = u_x

        if type == Suite.TYPE_ARITHMETICAL:
            raison=(u_b.value - u_a.value) / (u_b.index - u_a.index)
            self.expression_un = "{} + {}{}{}".format(Suite.U_N, ("", "(")[raison < 0], raison, ("", ")")[raison < 0])
            self.u_zero = u_a.value - (u_a.index + 1) * raison
        elif type == Suite.TYPE_GEOMETRICAL:
            power = float(1) / float(u_b.index - u_a.index)
            raison=(float(u_b.value) / float(u_a.value))**(power)
            print("power:[{}] raison:[{}] u_a.index:[{}] u_a.value:[{}]".format(power, raison, u_a.index, u_a.value))
            self.expression_un = "{} * {}{}{}".format(Suite.U_N, ("", "(")[raison < 0], raison, ("", ")")[raison < 0])
            self.u_zero = float(u_a.value) / (raison**(u_a.index+1))

    def init_with_expression(self, expression, first_value):
        self.expression_un = None
        self.expression_n = None
        self.u_zero = None
        self.first_value = None

        if self.isExpressionRecursive(expression):
            # génération récursive
            print("génération récursive")
            self.expression_un = expression
            self.u_zero = first_value
        else:
            print("génération implicite")
            self.expression_n = expression
            self.n_zero = first_value
            if self.isArithmetical():
                self.u_zero = self.term(0)
                self.expression_un = "{} + {}".format(Suite.U_N, self.term(1) - self.u_zero)
            elif self.isGeometrical():
                self.u_zero = self.term(0)
                self.expression_un = "{} * {}".format(Suite.U_N, self.term(1) / self.u_zero)

    def expression (self):
        return (self.expression_un, self.expression_n)[self.expression_un == None]

    def isExpressionRecursive(self, expression):
        return Suite.U_N in expression

    def term(self, term_index):
#        print("term term_index:[{}]".format(term_index))
        if self.expression_un == None:
            result = eval(self.expression_n, Suite.GLOBALS, {Suite.N: term_index})
        else:
            result = eval(self.expression_un, Suite.GLOBALS, {Suite.U_N: self.u_zero})
            if term_index > 0:
                result = eval(self.expression_un, Suite.GLOBALS, {Suite.U_N: self.term(term_index - 1)})

#        print("term = {}".format(term_index, result))
        return result

    def isArithmetical(self):
        nb_of_items=2
        results = [None] * nb_of_items
        for index in range(nb_of_items):
            term_index = index # random.randint(0, 10)
            u_n = self.term(term_index)
            u_n_plus_1 = self.term(term_index + 1)
            results[index] = u_n_plus_1 - u_n

        return all_equal(results)

    def isGeometrical(self):
        nb_of_items=2
        results = [None] * nb_of_items
        for index in range(nb_of_items):
            term_index = index # random.randint(0, 10)
            u_n = self.term(term_index)
            u_n_plus_1 = self.term(term_index + 1)
            results[index] = u_n_plus_1 / u_n

        return all_equal(results)

def study_suite(suite):
    isArithemical = suite.isArithmetical()
    if isArithemical:
        print("{} is arithmetic.".format(suite.expression()))
    else:
        isGeometrical = suite.isGeometrical()
        if isGeometrical:
            print("{} is geometic.".format(suite.expression()))

    for index in range(8):
        print("u{} = {}".format(index, suite.term(index)))

#study_suite(Suite(Suite.TYPE_ARITHMETICAL, SuiteTerm(3, 6), SuiteTerm(5, -2)))
study_suite(Suite(Suite.TYPE_GEOMETRICAL, SuiteTerm(3, 6), SuiteTerm(5, 2)))
#study_suite(Suite("2*n + 1", 1))
#study_suite(Suite("u_n + 1", 9))
#study_suite(Suite("u_n * 0.6", 1))
#study_suite(Suite("4 * 5**n", 1))

#study_suite(Suite("(u_n + 2)**2 * 0.6", 1))
