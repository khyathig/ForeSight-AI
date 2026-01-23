from pytrends.request import TrendReq
import random
import datetime

def fetch_realtime_trends():
    try:
        # Attempt real-time Google Trends
        pytrend = TrendReq(hl="en-IN", tz=330)
        trending_df = pytrend.trending_searches(pn="india")
        keywords = trending_df[0].head(10).tolist()
        source = "Google Trends (Live)"
    except Exception:
        # Fallback: dynamic simulated trends
        keywords = [
            "Summer drinks",
            "Protein snacks",
            "Healthy groceries",
            "Baby products",
            "Festival offers",
            "Cold beverages",
            "Organic food",
            "Fitness supplements",
            "Instant meals",
            "Energy drinks"
        ]
        random.shuffle(keywords)
        source = "Simulated Trends (Offline Mode)"

    category_map = {
        "drink": "Beverages",
        "beverage": "Beverages",
        "protein": "Health",
        "fitness": "Health",
        "baby": "Baby Care",
        "snack": "Snacks",
        "meal": "Grocery",
        "festival": "Grocery",
        "organic": "Grocery",
        "energy": "Beverages"
    }

    results = []

    for kw in keywords[:8]:
        category = "General"
        for key, cat in category_map.items():
            if key in kw.lower():
                category = cat
                break

        results.append({
            "keyword": kw,
            "category": category,
            "trend_score": random.randint(60, 100),
            "impact": "Increase stock" if category != "General" else "Monitor",
            "timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
            "source": source
        })

    return results
