from enum import Enum


class Obligation(Enum):
    AGREE = 36
    DISAGREE = 37


class DistributionType(Enum):
    INTERNAL = 31
    EXTERNAL = 30


class ComponentModified(Enum):
    YES = 28
    NO = 29


class Hosting(Enum):
    YES = 22
    NO = 23


class HostControl(Enum):
    ABB = 21
    THIRD_PARTY = 20
    NONE = 38


class ComponentInteraction(Enum):
    DYNAMICALLY = 27
    STATICALLY = 24
    STAND_ALONE = 25
    OTHERS = 26


class ComponentInteractionRules(Enum):
    DYNAMICALLY_LINKED = 0
    STATICALLY_LINKED = 1
    # To check if it is saved as STAND_ALONE or STAND-ALONE on blackduck (the project I analyzed never had this field before)
    STAND_ALONE = 2
    OTHERS = 3
