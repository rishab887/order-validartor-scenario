def is_valid_order(order):
    """Return True if order has a valid ORD- prefix and numeric ID."""
    if not isinstance(order, str):
        return False

    if not order.startswith("ORD-"):
        return False

    number = order[4:]

    return number.isdigit() and len(number) >= 3


def mask_order(order):
    """Mask the numeric portion of a valid order."""

    if not is_valid_order(order):
        raise ValueError("order is not valid")

    prefix = order[:4]
    number = order[4:]

    if len(number) <= 3:
        masked_number = "*" * len(number)
    else:
        masked_number = number[0] + "*" * (len(number) - 1)

    return f"{prefix}{masked_number}"


def normalize_order(order):
    """Remove spaces, uppercase, and add ORD- if missing."""

    if not isinstance(order, str):
        raise TypeError("order must be a string")

    cleaned = order.strip().upper()

    if not cleaned.startswith("ORD-"):
        cleaned = "ORD-" + cleaned

    return cleaned