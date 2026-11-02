
import re
from typing import Callable, Iterator


def generator_numbers(text: str) -> Iterator[float]:
    # Дійсні числа в умові відділені пробілами з обох боків.
    pattern = r"(?<= )\d+\.\d+(?= )"

    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable) -> float:
    total = sum(func(text))

    return total


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими "
        "надходженнями 27.45 і 324.00 доларів."
    )

    total_income = sum_profit(text, generator_numbers)

    print(f"Загальний дохід: {total_income}")
