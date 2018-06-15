import unittest

import app

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(app.add(10, 5), 15)
        self.assertEqual(app.add(-2, 2), 1)
