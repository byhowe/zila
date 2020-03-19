#!/usr/bin/env python3

from typing import List


class Validator:
    def __init__(self):
        pass

    def validate(self, field: str = None):
        pass


def validate(field: str,
             validators: List[Validator]) -> List[Validator]:
    failed: List[Validator] = []
    for validator in validators:
        if not validator.validate(field):
            failed.append(validator)
    return failed
