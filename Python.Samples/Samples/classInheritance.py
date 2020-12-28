class SuperA:
    var_a = 10
    def fun_a(self):
        return 11

    def fun(self):
        return "fun of SuperA"


class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
    def fun(self):
        return "fun of SuperB"

class Sub(SuperA, SuperB):
    def fun_b(self):
        return 22

