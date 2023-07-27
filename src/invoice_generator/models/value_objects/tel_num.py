from src.invoice_generator.interfaces.value_objects import ValueObject


class TelephoneNumber(ValueObject):
    """
    TelephoneNumber value object

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

    def __init__(self, value: str, prefix: str = "+48"):
        """
        TelephoneNumber constructor
        :param prefix: telephone number prefix
        """
        self._value = value
        self._value = self.normalize()
        self._prefix = prefix

        if not self.validator():
            raise ValueError("Invalid telephone number")

        if not self.prefix_validator():
            raise ValueError("Invalid telephone number prefix")

    def __eq__(self, other: object) -> bool:
        """
        Check if two telephone number are the same
        """
        if not isinstance(other, TelephoneNumber):
            return False
        return self.get_telephone_number() == other.get_telephone_number()

    def __ne__(self, other: object) -> bool:
        """
        Check if two telephone number are not the same
        """
        return not self.__eq__(other)

    def __str__(self) -> str:
        """
        TelephoneNumber string representation
        """
        return self._prefix + self._value

    def validator(self) -> bool:
        """
        TelephoneNumber validator
        """
        if len(self._value) != 9:
            return False
        try:
            int(self._value)
        except ValueError:
            return False
        return True

    def prefix_validator(self) -> bool:
        """
        TelephoneNumber prefix validator
        """
        if (len(self._value) != 3 or self._value[0] != "+") or (len(self._value) != 4 or self._value[0] != "+"):
            return False
        return True

    def normalize(self) -> str:
        """
        TelephoneNumber normalizer
        """
        return self._value.replace(" ", "").replace("-", "")

    def get_telephone_number(self) -> str:
        """
        Get telephone number
        """
        return self._prefix + self._value

    @property
    def value(self) -> str:
        """
        TelephoneNumber value getter
        """
        return self._value

    @property
    def prefix(self) -> str:
        """
        TelephoneNumber prefix getter
        """
        return self._prefix

    @value.setter
    def value(self, value: str):
        """
        TelephoneNumber value setter
        """
        self._value = value
        self._value = self.normalize()
        if not self.validator():
            raise ValueError("Invalid telephone number")

    @prefix.setter
    def prefix(self, prefix: str):
        """
        TelephoneNumber prefix setter
        """
        self._prefix = prefix
        if not self.prefix_validator():
            raise ValueError("Invalid telephone number prefix")
