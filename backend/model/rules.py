def apply_rules(base_demand, trend=1.1, event=1.2, feedback=0.9):
    return base_demand * trend * event * feedback
