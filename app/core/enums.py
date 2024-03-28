from enum import StrEnum


class Environment(StrEnum):
    PRODUCTION = 'production'
    STAGING = 'staging'
    LOCAL = 'local'
    TEST = 'test'
