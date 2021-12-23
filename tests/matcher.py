from hamcrest.core.base_matcher import BaseMatcher


class IsLengthGreaterThan5(BaseMatcher):
    def __init__(self, warning):
        self.warning = warning

    def _matches(self, item):
        if len(self.warning) > 5:
            return True
        return False

    def describe_to(self, description):
        description.append_text('Length is not greater than 5')


def custom_matcher(warning):
    return IsLengthGreaterThan5(warning)
