import unittest

from Account.Account1 import *
from Account.exceptions.InvalidAmountException import InvalidAmountException


class MyTestCase(unittest.TestCase):

    def test_newly_created_account_has_zero_balance(self):
        account = Account("abike", "1234", 0)
        self.assertEqual(0, account.check_balance("1234"))

    def testAccountPinThrowsException_whenInvalidPinIsInputWhenCreatingAccount(self):
        account = Account("abike", "1234", 0)
        with self.assertRaises(InvalidPinException):
            account.check_balance("12ergshr")

    def testDepositNegativeAmount_ThrowsException(self):
        account = Account("abike", "1234", 0)
        with self.assertRaises(InvalidAmountException):
            account.deposit(-5000)
            account.check_balance("1234")


if __name__ == '__main__':
    unittest.main()
