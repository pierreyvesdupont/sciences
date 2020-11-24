from math import *
import random

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

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

        if len(args) == 1:
            self.init_generation_implicite(args[0])
        elif len(args) == 2:
            self.init_generation_recursive(args[0], args[1])
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
            self.u_zero = u_a.value - (u_a.index) * raison
        elif type == Suite.TYPE_GEOMETRICAL:
            power = float(1) / float(u_b.index - u_a.index)
            raison=(float(u_b.value) / float(u_a.value))**(power)
            print("power:[{}] raison:[{}] u_a.index:[{}] u_a.value:[{}]".format(power, raison, u_a.index, u_a.value))
            self.expression_un = "{} * {}{}{}".format(Suite.U_N, ("", "(")[raison < 0], raison, ("", ")")[raison < 0])
            self.u_zero = float(u_a.value) / (raison**(u_a.index))

    def init_generation_implicite(self, expression):
        self.expression_un = None
        self.expression_n = None
        self.u_zero = None
        self.first_value = None

        print("génération implicite")
        self.expression_n = expression
        self.n_zero = None
        if self.isArithmetical():
            self.u_zero = self.term(0)
            self.expression_un = "{} + {}".format(Suite.U_N, self.term(1) - self.u_zero)
        elif self.isGeometrical():
            self.u_zero = self.term(0)
            self.expression_un = "{} * {}".format(Suite.U_N, self.term(1) / self.u_zero)

    def init_generation_recursive(self, expression, first_value):
        self.expression_un = None
        self.expression_n = None
        self.u_zero = None
        self.first_value = None

        print("génération récursive")
        self.expression_un = expression
        self.u_zero = first_value

    def expression (self):
        return (self.expression_un, self.expression_n)[self.expression_un == None]

    def isExpressionRecursive(self, expression):
        return Suite.U_N in expression

    def term(self, term_index):
#        print("term term_index:[{}]".format(term_index))
        if self.expression_un == None:
            result = eval(self.expression_n, Suite.GLOBALS, {Suite.N: term_index})
        else:
            result = self.u_zero
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

def draw_suite(suite):
    x = np.arange(0, 2,0.01)
    fig, ax = plt.subplots()

    data = [0] * 10
    for index in range(10):
        data[index] = suite.term(index)
    ax.plot(data)

    ax.set(xlabel='abscisses', ylabel='ordonnées',
        title='Suite')
    ax.grid()

    plt.show()

def study_suite(suite):
    isArithemical = suite.isArithmetical()
    if isArithemical:
        print("{} is arithmetic.".format(suite.expression()))
    else:
        isGeometrical = suite.isGeometrical()
        if isGeometrical:
            print("{} is geometic.".format(suite.expression()))
        else:
            print("{} is neither arithemic nor geometic.".format(suite.expression()))

    for index in range(8):
        print("u{} = {}".format(index, suite.term(index)))

    draw_suite(suite)

#study_suite(Suite(Suite.TYPE_ARITHMETICAL, SuiteTerm(3, 6), SuiteTerm(5, -2)))
#study_suite(Suite(Suite.TYPE_GEOMETRICAL, SuiteTerm(3, 6), SuiteTerm(5, 2)))
study_suite(Suite("2*n + 1"))
#study_suite(Suite("u_n + 1", 9))
#study_suite(Suite("u_n * 2", 1))
#study_suite(Suite("4 * 5**n"))

#study_suite(Suite("(u_n + 2)**2 * 0.6", 1))
#study_suite(Suite("(n + 2)**2 * 0.6"))
#study_suite(Suite("(-n+2)**3 * 0.6"))
#study_suite(Suite("(-n+2)**3 +1"))
