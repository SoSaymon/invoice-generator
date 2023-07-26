from src.invoice_generator.interfaces.value_objects import ValueObject


class NIP(ValueObject):
    """
    NIP value object

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
        NIP constructor
        """
        self._value = value
        self._value = self.normalize()

        if not self.validator():
            raise ValueError("Invalid NIP")

    def __eq__(self, other: object) -> bool:
        """
        Check if two NIPs are the same
        """
        if not isinstance(other, NIP):
            return False
        return self._value == other.value

    def __ne__(self, other: object) -> bool:
        """
        Check if two NIPs are not the same
        """
        return not self.__eq__(other)

    def __str__(self) -> str:
        """
        NIP string representation
        """
        return self._value

    def validator(self) -> bool:
        """
        NIP validator
        """
        if len(self._value) != 10:
            return False
        try:
            int(self._value)
        except ValueError:
            return False
        weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
        control_sum = sum([int(self._value[i]) * weights[i] for i in range(9)])
        control_digit = control_sum % 11
        if control_digit == 10:
            control_digit = 0
        return control_digit == int(self._value[9])

    def normalize(self) -> str:
        """
        NIP normalization
        """
        return self._value.replace('-', '')
    