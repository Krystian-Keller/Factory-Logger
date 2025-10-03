import pytest
from logger_pkg.singleton import Singleton


def test_same_instance_identity():
    class A(metaclass=Singleton):
        pass

    a1 = A()
    a2 = A()
    assert a1 is a2


def test_state_persists_and_init_called_once():
    class B(metaclass=Singleton):
        def __init__(self):
            # conta quantas vezes __init__ foi executado
            if not hasattr(self, "_inits"):
                self._inits = 0
            self._inits += 1

    b1 = B()
    b2 = B()
    assert b1 is b2
    # __init__ só roda na primeira criação
    assert b1._inits == 1


def test_distinct_singletons_per_class():
    class C(metaclass=Singleton):
        pass

    class D(metaclass=Singleton):
        pass

    c1, c2 = C(), C()
    d1, d2 = D(), D()
    assert c1 is c2
    assert d1 is d2
    assert c1 is not d1  # cada classe tem sua única instância


def test_subclass_has_own_singleton_instance():
    class Base(metaclass=Singleton):
        pass

    class Sub(Base):
        pass

    base1, base2 = Base(), Base()
    sub1, sub2 = Sub(), Sub()
    assert base1 is base2
    assert sub1 is sub2
    assert base1 is not sub1  # subclasses possuem instância própria


def test_first_constructor_args_win_and_are_retained():
    class E(metaclass=Singleton):
        def __init__(self, value=0):
            # apenas a primeira chamada define o valor
            if not hasattr(self, "value"):
                self.value = value

    e1 = E(10)
    e2 = E(999)
    assert e1 is e2
    assert e1.value == 10  # o primeiro valor “vence”


def test_reset_instance_allows_new_args_and_new_identity():
    class F(metaclass=Singleton):
        def __init__(self, name):
            # persistir apenas na primeira criação
            if not hasattr(self, "name"):
                self.name = name

    f1 = F("first")
    # identity antes do reset
    first_id = id(f1)
    assert f1.name == "first"

    # resetar a instância singleton da classe F
    F._reset_instance()

    f2 = F("second")  # nova criação deve aceitar novos args
    second_id = id(f2)

    assert f2.name == "second"
    assert first_id != second_id
    assert f1 is not f2
