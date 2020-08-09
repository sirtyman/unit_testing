class Foo(object):
    def __init__(self):
        self.a_param = None

    @staticmethod
    def foo():
        return "Fail"


class Bar(object):
    @staticmethod
    def bar():
        # Bar depends on Foo instance so that when calling Foo() specific mock instance should be returned
        foo = Foo()
        return foo.foo()
