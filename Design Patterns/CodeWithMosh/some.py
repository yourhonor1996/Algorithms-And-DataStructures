import dataclasses


@dataclasses.dataclass(repr=True, init= True)
class SomeClass:
    x: int
    y: float


inst = SomeClass(2, 3.4)
print(inst)
