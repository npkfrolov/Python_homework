import unittest
import sys

from messenger.server import create_parser, response


class TestParser(unittest.TestCase):

    def test_default(self):
        sys.argv[1:] = []
        parser = create_parser()
        namespace = parser.parse_args()
        self.assertEqual('', namespace.address)
        self.assertEqual(7777, namespace.port)

    def test_address(self):
        sys.argv[1:] = ['-a', 'localhost']
        parser = create_parser()
        namespace = parser.parse_args()
        self.assertEqual(namespace.address, 'localhost')

    def test_port(self):
        sys.argv[1:] = ['-p', '7778']
        parser = create_parser()
        namespace = parser.parse_args()
        self.assertEqual(namespace.port, 7778)


class TestResponse(unittest.TestCase):

    def testInstance(self):
        result = response(200, 'msg')
        self.assertIsInstance(result, dict)

    def testMsg(self):
        result = response(200, 'msg')
        self.assertIn('from', result)

    def testJoin(self):
        result = response(200, 'join')
        self.assertIn('room', result)


if __name__ == "__main__":
    unittest.main()
