import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_outdated_products(mock_datetime):
    mock_datetime.date.today.return_value = datetime.date.today()
    test_data = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 8, 1),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 8, 1),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 8, 1),
            "price": 160
        }
    ]
    assert outdated_products(test_data) == ["chicken", "duck"]
