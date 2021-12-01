class Foo:
    def __init__(self) -> None:
        self.x_value: int = 0

    @property
    def x(self):
        return self.x_value

    @x.setter
    def x(self, value: int):
        if value >= 0:
            value_str = str(value)
            if len(value_str) == 1:
                self.x_value = int(value)
            elif len(value_str) > 1:
                self.x_value = int(value_str[-2:])
        else:
            self.x_value = -1