import bhaskara

class test_bhaskara:
    def testa_uma_raiz(self):
        b = bhaskara.bhaskara()
        assert b.calcula_raizes(1, 0, 0) == (1, 0)

    