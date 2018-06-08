class Question:

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def _is_numeric_(value):
        return isinstance(value, int) or isinstance(value, float)

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        if _is_numeric_(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        # This is just a helper method to print
        # the question in a readable format.
        condition = "=="
        if _is_numeric_(value):
            condition = ">="
        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value))
