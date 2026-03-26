from datetime import datetime
from src.constants import DATE_FORMAT


def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        return False


def is_positive_number(value: str) -> bool:
    try:
        return float(value) > 0
    except Exception:
        return False
