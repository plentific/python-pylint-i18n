from pylint.interfaces import IAstroidChecker
from pylint.checkers import BaseChecker


class DateTimeNowChecker(BaseChecker):

    __implements__ = IAstroidChecker  # pylint: disable=F0220

    DATETIME_NOW = 'datetime-now'
    DATETIME_NOW_MESSAGE = (
        'In %s: datetime.now from datetime is not timezone-aware. '
        'Please use timezone.now from django.utils instead.'
    )
    DATETIME_NOW_HELP = (
        'datetime.now from datetime is not timezone-aware. '
        'timezone.now from django.utils should be used instead.'
    )

    name = 'datetime_now'
    msgs = {
        'R0402': (
            DATETIME_NOW_MESSAGE,
            DATETIME_NOW,
            DATETIME_NOW_HELP,
        ),
    }

    priority = -1

    def visit_attribute(self, node):
        if not hasattr(node, 'attrname') or node.attrname != 'now':
            return

        # Covered cases: datetime.now, datetime.datetime.now
        is_datetime = hasattr(node.expr, 'name') and node.expr.name == 'datetime'
        is_datetime_datetime = hasattr(node.expr, 'attrname') and node.expr.attrname == 'datetime'

        if is_datetime or is_datetime_datetime:
            source_string = (node.parent or node).as_string()
            self.add_message('datetime-now', node=node, args=(source_string,))


def register(linter):
    linter.register_checker(DateTimeNowChecker(linter))

