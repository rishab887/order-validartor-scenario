import pytest

from src.order_validator import (
    is_valid_order,
    mask_order,
    normalize_order,
)


def test_valid_order():
    assert is_valid_order("ORD-1234") is True


def test_invalid_order():
    assert is_valid_order("ABC-1234") is False


def test_mask_order_invalid():
    with pytest.raises(ValueError):
        mask_order("INVALID")


def test_normalize_order():
    assert normalize_order(" ord-5678 ") == "ORD-5678"


# This test is intentionally disabled.
# DO NOT enable it yet.

def test_mask_order_basic():
    result = mask_order("ORD-1234")
    assert result == "ORD-1***"

def test_invalid_order_non_string():
    assert is_valid_order(1234) is False


def test_mask_order_short_number():
    result = mask_order("ORD-123")
    assert result == "ORD-***"


def test_normalize_order_non_string():
    with pytest.raises(TypeError):
        normalize_order(1234)


def test_normalize_order_adds_prefix():
    result = normalize_order("5678")
    assert result == "ORD-5678"