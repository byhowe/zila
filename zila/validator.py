#!/usr/bin/env python3

from typing import List


class Validator:
    def __init__(self, *args, **kwargs):
        pass

    def validate(self, field: str = None):
        pass


def validate(field: str = None, validators: List[Validator] = []) -> List[Validator]:
    failed: List[Validator] = []
    for validator in validators:
        if not validator.validate(field):
            failed.append(Validator)
    return failed
