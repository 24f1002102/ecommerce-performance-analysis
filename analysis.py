import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/retention_2024.csv")

# Calculate average
average = df['retention_rate'].mean()
print("Average Retention Rate:", round(average, 2))

# Industry target
industry_target = 85

# Plot Trend + Benchmark
plt.figure(figsize=(8,5))
plt.plot(df['quarter'], df['retention_rate'], marker='o', label='Customer Retention Rate')
plt.axhline(y=industry_target, linestyle='--', label='Industry Benchmark')

plt.title('Customer Retention Trend (2024)')
plt.xlabel('Quarter')
plt.ylabel('Retention Rate (%)')
plt.legend()
plt.tight_layout()

plt.savefig('retention_trend.png')
print("Chart saved as retention_trend.png")
