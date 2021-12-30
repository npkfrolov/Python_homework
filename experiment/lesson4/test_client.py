import unittest

from lesson3.client import pres, send_mes, receiving, parse


class TestPresence(unittest.TestCase):
    def testInstance(self):
        msg = pres()
        self.assertIsInstance(msg, dict)

    def testMsg(self):
        result = pres()
        self.assertIn('user', result)


class TestParse(unittest.TestCase):
    def test_ok_response(self):
        result = parse({'response': 200})
        self.assertEqual(result, '200: OK')

    def test_err_response(self):
        result = parse({'response': 400})
        self.assertEqual(result, '400 : Error')


if __name__ == "__main__":
    unittest.main()
