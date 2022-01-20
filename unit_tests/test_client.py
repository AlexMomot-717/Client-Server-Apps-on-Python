"""Unit-тесты клиента"""

import os
import sys
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presence, process_answer


class TestClass(unittest.TestCase):
    """
    класс тестов
    """

    def test_def_presence(self):
        """ тест корректного запроса """
        test = create_presence()
        test[TIME] = 1.1  # время необходимо задать принудительно
        # противном случае он тест никогда не будет пройден

        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """ тест корректного разбора ответа 200 """
        self.assertEqual(process_answer({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """ тест корректного разбора ответа 400 """
        self.assertEqual(process_answer({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """ тест исключения без поля RESPONSE """
        self.assertRaises(ValueError, process_answer, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
