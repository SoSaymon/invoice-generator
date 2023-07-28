from pyban.iban import IBAN
from src.invoice_generator.interfaces.value_objects import ValueObject


class BankAccountNumber(ValueObject):
    """
    BankAccountNumber value object

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
        BankAccountNumber constructor
        """
        self._value = value
        self._value = self.normalize()

        if not self.validator():
            raise ValueError("Invalid bank account number")

    def __eq__(self, other: object) -> bool:
        """
        Check if two bank account numbers are the same
        """
        if not isinstance(other, BankAccountNumber):
            return False
        return self._value == other.value

    def __ne__(self, other: object) -> bool:
        """
        Check if two bank account numbers are not the same
        """
        return not self.__eq__(other)

    def __str__(self) -> str:
        """
        BankAccountNumber string representation
        """
        return self._value

    def validator(self) -> bool:
        """
        BankAccountNumber validator
        """
        if not self._value[:2].isalpha():
            self._value = "PL" + self._value

        try:
            IBAN(self._value)
        except ValueError:
            return False
        return True

    def normalize(self) -> str:
        """
        BankAccountNumber normalizer
        """
        return self._value.replace(" ", "").replace("-", "")

    @property
    def value(self) -> str:
        """
        BankAccountNumber value getter
        """
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        """
        BankAccountNumber value setter
        """
        self._value = value
        self._value = self.normalize()

        if not self.validator():
            raise ValueError("Invalid bank account number")
