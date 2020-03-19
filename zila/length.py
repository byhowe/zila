from .validator import Validator


class Length(Validator):
    def __init__(self, min_length: int = -1, max_length: int = -1):
        super().__init__()
        assert (
                min_length != -1 or max_length != -1
        ), "At least one of `min_length` or `max_length` must be specified."
        assert (
                max_length == -1 or min_length <= max_length
        ), "`min_length` cannot be more than `max_length`."
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, field: str = None) -> bool:
        length = field and len(field) or 0
        return not (
                length < self.min_length or
                self.max_length != -1 and length > self.max_length
        )
