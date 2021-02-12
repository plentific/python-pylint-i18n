try:
    from pylint.interfaces import IAstroidChecker
except ImportError:
    from pylint.interfaces import IASTNGChecker as IAstroidChecker

from pylint.checkers import BaseChecker


class DateTimeNowChecker(BaseChecker):

    __implements__ = IAstroidChecker  # pylint: disable=F0220

    name = 'datetime_now'
    msgs = {
        'R0402': ('Do not use datetime.now() %s',
                  'datetime-now',
                  "datetime.now() is not allowed"),
        }

    priority = -1

    def visit_attribute(self, node):
        is_datetime_module_n_class = (node.func.value.attr == 'datetime'
                                      and node.func.value.value.id == 'datetime')

        if is_datetime_module_n_class and node.func.attr in 'now':
            self.add_message('R0402', node=node, args=node.func.value)


def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(DateTimeNowChecker(linter))
