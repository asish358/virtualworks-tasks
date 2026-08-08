def cvp_analysis(fixed_costs, price_per_unit, variable_cost_per_unit, target_profit=0):
    # Calculate Contribution Margin
    cm_per_unit = price_per_unit - variable_cost_per_unit
    cm_ratio = cm_per_unit / price_per_unit

    if cm_per_unit <= 0:
        return "Price per unit must be greater than variable cost per unit."

    # Break-Even Point (Units and Sales)
    be_units = fixed_costs / cm_per_unit
    be_sales = fixed_costs / cm_ratio

    # Units needed for Target Profit
    target_units = (fixed_costs + target_profit) / cm_per_unit

    return {
        "Contribution Margin / Unit": f"${cm_per_unit:.2f}",
        "Contribution Margin Ratio": f"{cm_ratio * 100:.2f}%",
        "Break-Even Point (Units)": f"{be_units:.2f} units",
        "Break-Even Point (Sales)": f"${be_sales:.2f}",
        f"Units for Target Profit (${target_profit})": f"{target_units:.2f} units"
    }

# --- Example Usage ---
fixed_costs = 10000          # Total Fixed Costs
price = 50                   # Selling Price per Unit
variable_cost = 30           # Variable Cost per Unit
desired_profit = 5000        # Target Profit

results = cvp_analysis(fixed_costs, price, variable_cost, desired_profit)

for key, value in results.items():
    print(f"{key}: {value}")
