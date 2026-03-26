from dataclasses import dataclass


@dataclass
class Transaction:
    date: str
    tx_type: str
    amount: float
    category: str
    description: str
