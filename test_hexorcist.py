import pytest
from io import StringIO
import main
from unittest.mock import patch
from main import to_decimal, from_decimal, main  # adjust filename if needed


# ---------- TESTS FOR to_decimal ----------

def test_to_decimal_binary():
    assert to_decimal("1011", 2) == 11

def test_to_decimal_hex():
    assert to_decimal("1A", 16) == 26

def test_to_decimal_uppercase_handling():
    assert to_decimal("ff", 16) == 255

def test_to_decimal_base36():
    assert to_decimal("Z", 36) == 35

def test_to_decimal_invalid_character():
    with pytest.raises(ValueError):
        to_decimal("2", 2)


# ---------- TESTS FOR from_decimal ----------

def test_from_decimal_binary():
    assert from_decimal(11, 2) == "1011"

def test_from_decimal_hex():
    assert from_decimal(255, 16) == "FF"

def test_from_decimal_zero():
    assert from_decimal(0, 8) == "0"

def test_from_decimal_large_number():
    assert from_decimal(123456789, 36) == "21I3V9"


# ---------- INTEGRATION TEST FOR main() ----------

def test_main_integration(monkeypatch, capsys):
    # Simulate user input: number=1A, original base=16, target base=2
    inputs = iter(["1A", "16", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    output = capsys.readouterr().out
    assert "The number 1A in base 16 is 11010 in base 2." in output
