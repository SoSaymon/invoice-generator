from src.invoice_generator.interfaces.value_objects import ValueObject


class REGON(ValueObject):
    """
    REGON value object

    Attributes:
    -----------
    value: str

    Methods:
    --------
    __init__(self, value: str)
    __eq__(self, other: object) -> bool
    __ne__(self, other: object) -> bool
    __str__(self) -> str
    validator(self) -> bool
    """

    def __init__(self, value: str):
        """
        REGON constructor
        """
        self._value = value
        self._value = self.normalize()

        if not self.validator():
            raise ValueError("Invalid REGON")

    def __eq__(self, other: object) -> bool:
        """
        Check if two REGONs are the same
        """
        if not isinstance(other, REGON):
            return False
        return self._value == other.value

    def __ne__(self, other: object) -> bool:
        """
        Check if two REGONs are not the same
        """
        return not self.__eq__(other)

    def __str__(self) -> str:
        """
        REGON string representation
        """
        return self._value

    def validator(self) -> bool:
        """
        REGON validator
        """
        if len(self._value) not in [9, 14]:
            return False
        try:
            int(self._value)
        except ValueError:
            return False
        weights = [8, 9, 2, 3, 4, 5, 6, 7]
        if len(self._value) == 9:
            weights = [8, 9, 2, 3, 4, 5, 6, 7]
        elif len(self._value) == 14:
            weights = [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]
        control_sum = 0
        for i in range(len(weights)):
            control_sum += int(self._value[i]) * weights[i]
        control_sum %= 11
        if control_sum == 10:
            control_sum = 0
        return control_sum == int(self._value[-1])

    def normalize(self) -> str:
        """
        Normalize REGON
        """
        return self._value.replace("-", "").replace(" ", "")