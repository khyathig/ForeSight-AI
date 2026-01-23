from flask import Flask, jsonify
import pandas as pd
from model.forecast import generate_forecast
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Load datasets
orders = pd.read_csv("data/blinkit_orders.csv")
order_items = pd.read_csv("data/blinkit_order_items.csv")
products = pd.read_csv("data/blinkit_products.csv")
inventory = pd.read_csv("data/blinkit_inventory.csv")
feedback = pd.read_csv("data/blinkit_customer_feedback.csv")
events = pd.read_csv("data/events.csv")
policy = pd.read_csv("data/policy_impact.csv")

# Parse dates safely
orders["order_date"] = pd.to_datetime(orders["order_date"])
inventory["date"] = pd.to_datetime(inventory["date"], format="mixed", errors="coerce")
events["date"] = pd.to_datetime(
    events["date"],
    format="mixed",
    errors="coerce"
)

policy["date"] = pd.to_datetime(
    policy["date"],
    format="mixed",
    errors="coerce"
)



@app.route("/")
def home():
    return "Backend running. Use /dashboard, /events, /policies, /feedback"


@app.route("/dashboard")
def dashboard():
    df = generate_forecast(
        orders, order_items, products,
        inventory, feedback, events, policy
    )
    return jsonify(df.to_dict(orient="records"))


@app.route("/events")
def events_api():
    return jsonify(events.to_dict(orient="records"))


@app.route("/policies")
def policies_api():
    return jsonify(policy.to_dict(orient="records"))


@app.route("/feedback")
def feedback_api():
    merged = (
        feedback
        .merge(order_items, on="order_id")
        .merge(products, on="product_id")
    )

    low_rated = merged[merged["rating"] < 3]

    result = (
        low_rated.groupby(["product_name", "category"])["rating"]
        .mean()
        .reset_index()
    )

    return jsonify(result.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)
