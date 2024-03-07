from model import Creature

_creatures: list[Creature] = [
    Creature(
        name="yeti",
        country="CN",
        area="Himalayas",
        description="A large, hairy, ape-like creature.",
        aka="Abominable Snowman",
    ),
    Creature(
        name="sasquatch",
        country="US",
        area="*",
        description="A large, hairy, ape-like creature.",
        aka="Bigfoot",
    ),
]


def get_creatures() -> list[Creature]:
    return _creatures
