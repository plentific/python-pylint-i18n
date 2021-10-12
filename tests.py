import unittest
import astroid
import pylint.testutils

from deprecate_transaction_test_case import TransactionTestCaseChecker


class MissingGettextTestCase(unittest.TestCase):
    def testT(self):
        pass


class TestTransactionTestCaseChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = TransactionTestCaseChecker

    def test_transaction_test_case_classes(self):
        import_statements = [
            'import rest_framework.test.APITransactionTestCase #@',
            'from rest_framework.test import APITransactionTestCase #@',
            'import django.test.TransactionTestCase #@',
            'from django.test import TransactionTestCase #@',
        ]

        for import_statement in import_statements:
            import_node = astroid.extract_node(import_statement)
            with self.assertAddsMessages(
                    pylint.testutils.Message(
                        msg_id='deprecate-transaction-test-case',
                        node=import_node,
                    ),
            ):
                self.checker.visit_class(import_node)


if __name__ == '__main__':
    unittest.main()
