import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AutonomousPriceElasticityOptimizerClient

def main():
    client = AutonomousPriceElasticityOptimizerClient()
    res = client.optimize_price_elasticity()
    print("=== Autonomous Price Elasticity Optimizer Output ===")
    print(f"Current Price: ${res['current_price_usd']} -> Optimal: ${res['recommended_optimal_price_usd']}")
    print(f"Demand: {120} units/wk -> Projected: {res['projected_weekly_demand']} units/wk")
    print(f"Weekly Profit: ${res['current_weekly_profit_usd']} -> ${res['projected_weekly_profit_usd']} ({res['projected_profit_lift_percentage']})")
    print(f"Verdict: {res['verdict']}")

if __name__ == '__main__':
    main()
