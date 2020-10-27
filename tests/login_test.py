import unittest
from app.models import Users


class UserTest(unittest.TestCase):

    def setUp(self):
        self.new_users =Users('michie','michie57','abc@gmail.com')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_users))


if __name__ == '__main__':
    unittest.main()