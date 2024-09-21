from components.parse import tokenizeProgram, parse
import pytest as pt

class TestTokenize:
    def testTokenizeSimple(self):
        expression = "x"
        L = ["x"]
        assert tokenizeProgram(expression) == L

    def testTokenizeFullExpression(self):
        expression = "(define x 10)"
        L = ["(", "define", "x", "10", ")"]
        assert tokenizeProgram(expression) == L

    def testTokenizeNestedExpression(self):
        expression = "(define x (+ 3 2))"
        L = ["(", "define", "x", "(", "+", "3", "2", ")", ")"]
        assert tokenizeProgram(expression) == L

    def testTokenizeInvalidExpression(self):
        expression = ") definex ("
        L = [")", "definex", "("]
        assert tokenizeProgram(expression) == L

class TestParse:
    def testParseSimple(self):
        expression = "x"
        L = "x"
        assert parse(expression) == L
    
    def testParseFullExpression(self):
        expression = "(define x 10)"
        L = ["define", "x", 10]
        assert parse(expression) == L
    
    def testParseNestedExpression(self):
        expression = "(define x (+ 3 2))"
        L = ["define", "x", ["+", 3, 2]]
        assert parse(expression) == L
    
    def testTokenizeInvalidExpression(self):
        with pt.raises(Exception) as e_info:
            expression = ") definex ("
            tokenizeProgram(expression)
            assert str(e_info.value) == "Unexpected )"

