import datetime
from unittest import mock
from app.main import outdated_products


def test_outdated_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 9, 5),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 9, 1),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 9, 1),
            "price": 160
        }
    ]
    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2024, 9, 1)
        assert outdated_products(products) == ["chicken", "duck"]
