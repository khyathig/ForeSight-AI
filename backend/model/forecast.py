import pandas as pd


def rolling_average_forecast(series, window=7):
    """
    Simple rolling average forecast.
    Stable, explainable, and production-safe.
    """
    return series.tail(window).mean()


def generate_forecast(
    orders,
    order_items,
    products,
    inventory,
    feedback,
    events,
    policy
):
    # --- MERGE SALES DATA ---
    sales = (
        order_items
        .merge(orders, on="order_id")
        .merge(products, on="product_id")
    )

    sales["order_date"] = pd.to_datetime(
        sales["order_date"], dayfirst=True
    ).dt.normalize()

    daily_sales = (
        sales
        .groupby(["category", "order_date"])["quantity"]
        .sum()
        .reset_index()
    )

    # --- INVENTORY BY CATEGORY ---
    inventory_cat = (
        inventory
        .merge(products, on="product_id")
        .groupby("category")["available_stock"]
        .sum()
        .reset_index()
    )

    results = []

    for category in daily_sales["category"].unique():
        cat_sales = daily_sales[
            daily_sales["category"] == category
        ].sort_values("order_date")

        if len(cat_sales) < 7:
            continue

        base_demand = rolling_average_forecast(
            cat_sales["quantity"]
        )

        multiplier = 1.0

        # --- EVENT IMPACT ---
        if category in events["category"].values:
            impact = events[
                events["category"] == category
            ]["impact_level"].iloc[0]

            if impact == "High":
                multiplier *= 1.25
            elif impact == "Medium":
                multiplier *= 1.15

        # --- POLICY IMPACT ---
        if category in policy["category"].values:
            impact = policy[
                policy["category"] == category
            ]["impact_level"].iloc[0]

            if impact == "High":
                multiplier *= 1.20
            elif impact == "Medium":
                multiplier *= 1.10

        # --- FEEDBACK IMPACT ---
        fb = (
            feedback
            .merge(order_items, on="order_id")
            .merge(products, on="product_id")
        )

        bad_reviews = fb[
            (fb["category"] == category) &
            (fb["rating"] < 3)
        ]

        if len(bad_reviews) > 0:
            multiplier *= 0.85

        adjusted_demand = base_demand * multiplier

        stock_row = inventory_cat[
            inventory_cat["category"] == category
        ]

        available_stock = (
            stock_row["available_stock"].iloc[0]
            if not stock_row.empty else 0
        )

        status = (
            "High Demand"
            if adjusted_demand > available_stock
            else "Low Demand"
        )

        results.append({
            "category": category,
            "base_demand": round(base_demand, 2),
            "adjusted_demand": round(adjusted_demand, 2),
            "available_stock": round(available_stock, 2),
            "status": status
        })

    return pd.DataFrame(results)
