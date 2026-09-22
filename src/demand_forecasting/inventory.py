"""Business rules that convert demand forecasts into stock recommendations."""


def recommended_order_quantity(
    forecast_demand_during_lead_time: float,
    current_inventory: int,
    safety_stock: int,
) -> int:
    """Return the non-negative number of units that should be ordered.

    Values are rounded up because inventory is ordered in whole units.
    """
    if forecast_demand_during_lead_time < 0:
        raise ValueError("forecast_demand_during_lead_time must not be negative")
    if current_inventory < 0:
        raise ValueError("current_inventory must not be negative")
    if safety_stock < 0:
        raise ValueError("safety_stock must not be negative")

    required_units = forecast_demand_during_lead_time + safety_stock - current_inventory
    return max(0, int(-(-required_units // 1)))
