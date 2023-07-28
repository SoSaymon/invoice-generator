import sys
import pytest

sys.path.append(".")

from src.invoice_generator.models.value_objects.bank_acc_num import BankAccountNumber


@pytest.mark.value_objects
class TestBankAccountNumber:
    @pytest.mark.parametrize(
        "bank_acc_num, expected",
        [
            ("PL02249000050000460083168772", "PL02249000050000460083168772"),
            ("02249000050000460083168772", "PL02249000050000460083168772"),
        ]
    )
    def test_normalize(self, bank_acc_num, expected) -> None:
        assert BankAccountNumber(bank_acc_num).value == expected

    @pytest.mark.parametrize(
        "bank_acc_num1, bank_acc_num2, expected",
        [
            ("PL02249000050000460083168772", "PL02249000050000460083168772", True),
            ("02249000050000460083168772", "02249000050000460083168772", True),
            ("PL02249000050000460083168772", "02249000050000460083168772", True),
            ("PL02249000050000460083168772", "PL21101000550202416000070000", False),
            ("02249000050000460083168772", "21101000550202416000070000", False),
            ("PL02249000050000460083168772", "21101000550202416000070000", False),
            ("PL02249000050000460083168772", "PL21101000550202416000070000", False),
        ]
    )
    def test_eq(self, bank_acc_num1, bank_acc_num2, expected) -> None:
        assert (BankAccountNumber(bank_acc_num1) == BankAccountNumber(bank_acc_num2)) == expected

    @pytest.mark.parametrize(
        "bank_acc_num1, bank_acc_num2, expected",
        [
            ("PL02249000050000460083168772", "PL02249000050000460083168772", False),
            ("02249000050000460083168772", "02249000050000460083168772", False),
            ("PL02249000050000460083168772", "02249000050000460083168772", False),
            ("PL02249000050000460083168772", "PL21101000550202416000070000", True),
            ("02249000050000460083168772", "21101000550202416000070000", True),
            ("PL02249000050000460083168772", "21101000550202416000070000", True),
            ("PL02249000050000460083168772", "PL21101000550202416000070000", True),
        ]
    )
    def test_ne(self, bank_acc_num1, bank_acc_num2, expected) -> None:
        assert (BankAccountNumber(bank_acc_num1) != BankAccountNumber(bank_acc_num2)) == expected

    @pytest.mark.parametrize(
        "bank_acc_num, expected",
        [
            ("PL02249000050000460083168772", "PL02249000050000460083168772"),
            ("02249000050000460083168772", "PL02249000050000460083168772"),
        ]
    )
    def test_str(self, bank_acc_num, expected) -> None:
        assert str(BankAccountNumber(bank_acc_num)) == expected

    @pytest.mark.parametrize(
        "bank_acc_num",
        [
            "PL0224900005000460083168772",
            "0224900005000046083168772",
            "PL0224900005000046008316872",
            "0224900005000046008316872",
            "PL022490000500004600831687721",
            "022490000500004600831687721",
        ]
    )
    def test_raise_value_error(self, bank_acc_num) -> None:
        with pytest.raises(ValueError):
            BankAccountNumber(bank_acc_num)