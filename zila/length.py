from .validator import Validator


class Length(Validator):
    def __init__(self, min_length: int = -1, max_length: int = -1):
        assert (
            min_length != -1 or max_length != -1
        ), "At least one of `min_length` or `max_length` must be specified."
        assert max_length == -1 or min_length <= max, "`min` cannot be more than `max`."
        self.min_length = min
        self.max_length = max

    def validate(self, field: str = None) -> bool:
        length = field and len(field) or 0
        return not (
            length < self.min_length or self.max_length != -1 and length > self.max
        )
