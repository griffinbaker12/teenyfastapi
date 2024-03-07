from pydantic import BaseModel


class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str


thing = Creature(
    name="Bigfoot",
    country="USA",
    area="Pacific Northwest",
    description="A large, hairy, ape-like creature that walks on two legs.",
    aka="Sasquatch",
)
