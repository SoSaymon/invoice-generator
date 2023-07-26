from abc import ABC, abstractmethod


class ValueObject(ABC):
    """
    ValueObject interface

    Params:
    -------
    value: object

    Methods:
    --------
    __init__(self, value: object)
    __eq__(self, other: object) -> bool
    __ne__(self, other: object) -> bool
    __str__(self) -> str
    validator(self) -> bool
    """
    @abstractmethod
    def __init__(self, value: object):
        """
        ValueObject constructor
        """
        self._value = value

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Check if two ValueObjects are the same
        """
        raise NotImplementedError

    @abstractmethod
    def __ne__(self, other: object) -> bool:
        """
        Check if two ValueObjects are not the same
        """
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        """
        ValueObject string representation
        """
        raise NotImplementedError

    @abstractmethod
    def validator(self) -> bool:
        """
        ValueObject validator
        """
        raise NotImplementedError

    @property
    def value(self) -> object:
        """
        ValueObject value getter
        """
        return self._value

    @value.setter
    def value(self, value: object) -> None:
        """
        ValueObject value setter
        """
        self._value = value
