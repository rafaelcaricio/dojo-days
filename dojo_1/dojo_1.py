import unittest


def count_nesting(content):
    if not content:
        return 0
    return 1 + count_nesting(content.replace('()', ''))


class DojoTest (unittest.TestCase):
    def test_no_level(self):
        level = count_nesting("")
        self.assertEqual(level, 0)

    def test_one_level(self):
        levels = count_nesting("()")
        self.assertEqual(levels, 1)

    def test_one_level_v2(self):
        levels = count_nesting("()()")
        self.assertEqual(levels, 1)

    def test_two_levels(self):
        levels = count_nesting("(())")
        self.assertEqual(levels, 2)

    def test_one_level_v3(self):
        levels = count_nesting("()()()")
        self.assertEqual(levels, 1)

    def test_final_test(self):
        content = "(((((((((((((()))((((()))(()))))))))(((()))(((((())))(())))))))(()))((())(())))((((((())))((((())))))((((((((()))((((((((((((((((((((((((((((((())))))))))))((())))(((()))))(((((((()))((())(((())((())(((((((())(()))((()))))(())))(()))))))))(())))((((((((()))))(())))))))(((((((()))))))))(((()))))(((())(((()))(((())(())))))))(((((()))))(())))((())(())))((((()))))))))(())))))(((((((())(())))((())))(((((((())(((((((())))))(((((()))(((())((()))))))(())))(()))))((()))))(())))))(()))))))))))))(((((())((((()))(((((((()))(((((((())))))((((((((((()))))))((((((((()))(()))((())(())))))((())(((())(())))))))(((()))(())))(((()))(())))(((((())((())))((((())((()))))((((((()))((()))))(()))((((((((((((((()))(()))(())))((())))((())))(((())(((((()))(((())((((())))(())))(())))(()))((((())((((())((((())))))))))))))))((())))(((()))((((((((((((())((((())))(())))))(()))))))(((((((((()))((((((())))(())))))(()))((()))))(()))((((()))((())((((()))))))(()))))))))))(()))))))(((())))))))(((()))))))))(((())(((((((((())))(((()))(((())))))(((())(((())((((())))))(((((((((((((((((((())(((())))))(((((())))(()))(())))(((((((((((((()))(()))((((())))((((())(((())((((())))(())))((((()))))))(()))(())))))(((((((((()))(((((())(()))(((()))((()))))))))))(()))(()))))))((((((())(()))(((()))((())((((((((((())))(())))((())))((((((()))(()))(())))(()))))((())(((((())(())))))))((((())(((((()))))(())))(()))(()))))))(((())))))))))(()))(())))(())))(()))(()))((((())))))))((()))))(()))(((((((((((((((((((((()))((())((((())(())))))))))))))(())))((((())(((()))))(())))))((())))(((((())(())))((())(())))))))((((())((((())(((())))))(())))(())))))((())((())))))(((()))((())(((((((()))(()))((()))))((())))))))((((())))((())))))))))(())))))))))))))((())))))((((())((())))(((((((()))(((())(((())((((())((((()))(()))(()))))))(((((((()))((((())))))))((())))(()))))((((())))))))((()))))(())))((((((()))))(((()))))((((())(())))(((()))((()))))))"
        levels = count_nesting(content)
        self.assertEqual(levels, 56)

if __name__ == '__main__':
    unittest.main()
