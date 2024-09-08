from components import tokenizeProgram

class TestTokenize:
    def testTokenizeSimple(self):
        str = "x"
        L = ["x"]
        assert tokenizeProgram(str) == L

    def testTokenizeFullExpression(self):
        expression = "(define x 10)"
        L = ["(", "define", "x", "10", ")"]
        assert tokenizeProgram(expression) == L

    def testTokenizeNestedExpression(self):
        expression = "(define x (+ 3 2))"
        L = ["(", "define", "x", "(", "+", "3", "2", ")", ")"]
        assert tokenizeProgram(expression) == L