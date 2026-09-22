import pytest

from demand_forecasting.inventory import recommended_order_quantity


def test_recommends_enough_stock_for_forecast_and_buffer() -> None:
    assert recommended_order_quantity(64, current_inventory=38, safety_stock=12) == 38


def test_never_recommends_negative_quantity() -> None:
    assert recommended_order_quantity(10, current_inventory=100, safety_stock=5) == 0


def test_rejects_invalid_inventory_values() -> None:
    with pytest.raises(ValueError, match="current_inventory"):
        recommended_order_quantity(10, current_inventory=-1, safety_stock=5)
