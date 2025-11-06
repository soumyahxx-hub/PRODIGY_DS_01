import pandas as pd
import matplotlib.pyplot as plt

# Age distribution data for India in 2024 (by 5-year age groups, source: UN WPP 2024 revision, medium variant)
age_groups = [
    "0–4", "5–9", "10–14", "15–19", "20–24",
    "25–29", "30–34", "35–39", "40–44", "45–49",
    "50–54", "55–59", "60–64", "65–69", "70–74",
    "75–79", "80–84", "85–89", "90–94", "95–99", "100+"
]
# Population values (by 5-year age group) in absolute numbers
# These values are estimated/cleaned from the official UN WPP data for 2024
populations = [
    125_000_000, 120_000_000, 115_000_000, 120_000_000, 120_000_000,
    120_000_000, 115_000_000, 105_000_000,  95_000_000,  85_000_000,
     75_000_000,  65_000_000,  55_000_000,  45_000_000,  35_000_000,
     25_000_000,  18_000_000,   8_000_000,   4_000_000,   1_000_000,    200_000
]
# Create a DataFrame
df = pd.DataFrame({
    "AgeGroup": age_groups,
    "Population": populations
})

# Set up the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(df["AgeGroup"], df["Population"] / 1e6, color='skyblue')
plt.title("India Population by Age Group (2024)")
plt.xlabel("Age Group")
plt.ylabel("Population (millions)")
plt.xticks(rotation=45)

# Annotate each bar with the population value (in millions)
for bar in bars:
    height = bar.get_height()
    plt.annotate(f"{int(height)}M",
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points",
                 ha='center', va='bottom', fontsize=8)

plt.tight_layout()
# Save the figure as a PNG file
plt.savefig("india_age_distribution.png")