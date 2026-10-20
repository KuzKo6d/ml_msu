from typing import List


def hello(name: str = None) -> str:
    msg = f"Hello, {name}!" if (name and len(name) > 0) else "Hello!"
    return msg


def int_to_roman(num: int) -> str:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


def longest_common_prefix(strs_input: List[str]) -> str:
    if not strs_input:
        return ""

    cleaned_strs = [s.lstrip() for s in strs_input]
    if not cleaned_strs or any(len(s) == 0 for s in cleaned_strs):
        return ""

    prefix = ""
    for chars in zip(*cleaned_strs):
        if len(set(chars)) == 1:
            prefix += chars[0]
        else:
            break
    return prefix


def primes():
    yield 2
    p_list = [2]
    n = 3
    while True:
        is_prime = True
        for p in p_list:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            p_list.append(n)
            yield n
        n += 2


class BankCard:
    def __init__(self, total_sum: int, balance_limit: int = None):
        self.total_sum = total_sum
        self.balance_limit = balance_limit

    def __call__(self, sum_spent: int):
        if sum_spent > self.total_sum:
            print(f"Not enough money to spend {sum_spent} dollars.")
            raise ValueError(f"Not enough money to spend {sum_spent} dollars.")
        self.total_sum -= sum_spent
        print(f"You spent {sum_spent} dollars.")

    def __str__(self) -> str:
        return "To learn the balance call balance."

    @property
    def balance(self) -> int:
        if self.balance_limit is not None:
            if self.balance_limit <= 0:
                print("Balance check limits exceeded.")
                raise ValueError("Balance check limits exceeded.")
            self.balance_limit -= 1
        return self.total_sum

    def put(self, sum_put: int):
        self.total_sum += sum_put
        print(f"You put {sum_put} dollars.")

    def __add__(self, other):
        if not isinstance(other, BankCard):
            return NotImplemented
        if self.balance_limit is None or other.balance_limit is None:
            new_limit = None
        else:
            new_limit = max(self.balance_limit, other.balance_limit)
        return BankCard(self.total_sum + other.total_sum, new_limit)
