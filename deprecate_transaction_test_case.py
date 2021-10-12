# pylint: disable=W0002

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

from astroid.nodes.node_classes import Import, ImportFrom


class TransactionTestCaseChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'deprecate_transaction_test_case'
    priority = -1
    msgs = {
        'W0002': (
            'Usage of TransactionTestCase or APITransactionTestCase.',
            'deprecate-transaction-test-case',
            'TransactionTestCase or APITransactionTestCase should not be used.'
        ),
    }

    def visit_class(self, node):
        if type(node) not in [Import, ImportFrom]:
            return

        if 'TransactionTestCase' in node.names[0][0]:
            self.add_message('deprecate-transaction-test-case', node=node)
