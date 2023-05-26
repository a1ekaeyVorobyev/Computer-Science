import unittest

from lexer import LexDisassembly


class TestLexer(unittest.TestCase):
    def testCreateToken(self):
        """тeсты"""
        lex_disassembly = LexDisassembly()

        str_test = 'g = 1+(10+34)*2'
        str_result = lex_disassembly.format_string(str_test)
        str_ideal = 'g = 1 + ( 10 + 34 ) * 2'
        self.assertEqual(str_result, str_ideal)
        token_result = lex_disassembly.get_token(str_result)
        token_ideal = ['=', 'g', ['+', '1', ['*', ['+', '10', '34'], '2']]]
        self.assertEqual(token_result, token_ideal)

    def testCreateListTokens(self):
        lex_disassembly = LexDisassembly()
        str_test = 'a=2\ng = 1+(10+34)*2\na=a+g\n<<a'
        tokens_result = lex_disassembly.create_list_tokens(str_test)
        tokens_ideal = [['=', 'a', '2'], ['=', 'g', ['+', '1', ['*', ['+', '10', '34'], '2']]],
                        ['=', 'a', ['+', 'a', 'g']], ['<<', 'a', '']]
        self.assertEqual(tokens_result, tokens_ideal)

    def test_build_token_parenthesis(self):
        lex_disassembly = LexDisassembly()
        str_test = lex_disassembly.format_string('a=(a+1*(2+b))').split(' ')
        tokens_result = lex_disassembly.build_token_parenthesis(str_test)
        tokens_ideal = ['=', 'a', ['+', 'a', ['*', '1', ['+', '2', 'b']]]]
        self.assertEqual(tokens_result, tokens_ideal)

    def test_build_token_parenthesis_Exception(self):
        lex_disassembly = LexDisassembly()
        str_test = lex_disassembly.format_string('a=((a+1*(2+b))').split(' ')
        with self.assertRaises(Exception) as context:
            lex_disassembly.build_token_parenthesis(str_test)


if __name__ == '__main__':
    unittest.main()
