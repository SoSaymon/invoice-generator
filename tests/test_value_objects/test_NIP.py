import sys
import pytest

sys.path.append(".")

from src.invoice_generator.models.value_objects.NIP import NIP


@pytest.mark.value_objects
class TestNIP:
    @pytest.mark.parametrize(
        "nip, expected",
        [
            ("611-020-28-60", "6110202860"),
            ("6110202860", "6110202860"),
        ]
    )
    def test_normalize(self, nip, expected):
        assert NIP(nip).value == expected

    @pytest.mark.parametrize(
        "nip1, nip2, expected",
        [
            ("6110202860", "6110202860", True),
            ("611-020-28-60", "611-020-28-60", True),
            ("6110202860", "611-020-28-60", True),
            ("6110202860", "5272267889", False),
            ("6110202860", "527-226-78-89", False),
            ("611-020-28-60", "527-226-78-89", False),
            ("611-020-28-60", "5272267889", False),
        ]
    )
    def test_eq(self, nip1, nip2, expected):
        assert (NIP(nip1) == NIP(nip2)) == expected

    @pytest.mark.parametrize(
        "nip1, nip2, expected",
        [
            ("6110202860", "6110202860", False),
            ("611-020-28-60", "611-020-28-60", False),
            ("6110202860", "611-020-28-60", False),
            ("6110202860", "5272267889", True),
            ("6110202860", "527-226-78-89", True),
            ("611-020-28-60", "527-226-78-89", True),
            ("611-020-28-60", "5272267889", True),
        ]
    )
    def test_ne(self, nip1, nip2, expected):
        assert (NIP(nip1) != NIP(nip2)) == expected

    @pytest.mark.parametrize(
        "nip, expected",
        [
            ("6110202860", "6110202860"),
            ("611-020-28-60", "6110202860"),
        ]
    )
    def test_str(self, nip, expected):
        assert str(NIP(nip)) == expected

    @pytest.mark.parametrize(
        "nip",
        [
            "6110202869",
            "123 456 78 90",
            "ada-456-78-90",
        ]
    )
    def test_init_raises(self, nip):
        with pytest.raises(ValueError):
            NIP(nip)
