import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os
# Set seed so results are reproducible
random.seed(42)
np.random.seed(42)

# Categories and realistic transactions
expenses = {
    'Housing': ['Rent', 'Home Insurance', 'Council Tax', 'Electricity Bill', 'Gas Bill', 'Water Bill', 'Broadband'],
    'Food': ['Tesco', 'Sainsburys', 'Asda', 'Lidl', 'Aldi', 'Marks and Spencer', 'Waitrose', 'Co-op'],
    'Transport': ['TfL Oyster', 'National Rail', 'Uber', 'Petrol', 'Car Insurance', 'MOT'],
    'Health': ['Boots Pharmacy', 'GP Prescription', 'Gym Membership', 'Dentist', 'Optician'],
    'Entertainment': ['Netflix', 'Spotify', 'Cinema', 'Amazon Prime', 'Dining Out', 'Takeaway'],
    'Clothing': ['ASOS', 'Primark', 'Next', 'Nike', 'H&M'],
    'Savings': ['Savings Transfer', 'Emergency Fund', 'ISA Contribution'],
    'Personal': ['Haircut', 'Phone Bill', 'Amazon Purchase', 'eBay', 'Miscellaneous']
}

income = {
    'Salary': ['Monthly Salary'],
    'Freelance': ['Freelance Payment', 'Consulting Fee'],
    'Other': ['HMRC Tax Refund', 'Bank Interest', 'Gift Received']
}# Realistic amount ranges per category (min, max)
expense_ranges = {
    'Housing': (400, 1200),
    'Food': (15, 120),
    'Transport': (10, 150),
    'Health': (10, 80),
    'Entertainment': (8, 60),
    'Clothing': (20, 150),
    'Savings': (100, 400),
    'Personal': (5, 50)
}

# Income ranges
income_ranges = {
    'Salary': (2200, 2200),
    'Freelance': (200, 800),
    'Other': (20, 300)
}
def generate_transactions(start_date, end_date):
    transactions = []
    current_date = start_date

    while current_date <= end_date:
        # Add monthly salary on the 25th
        if current_date.day == 25:
            transactions.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'description': 'Monthly Salary',
                'category': 'Salary',
                'amount': 2200.00,
                'type': 'income'
            })

        # Generate 3-6 random expense transactions per day
        num_transactions = random.randint(0, 3)
        for _ in range(num_transactions):
            category = random.choice(list(expenses.keys()))
            description = random.choice(expenses[category])
            min_amount, max_amount = expense_ranges[category]
            amount = round(random.uniform(min_amount, max_amount), 2)

            transactions.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'description': description,
                'category': category,
                'amount': amount,
                'type': 'expense'
            })

        # Occasionally add freelance or other income
        if random.random() < 0.05:
            category = random.choice(['Freelance', 'Other'])
            description = random.choice(income[category])
            min_amount, max_amount = income_ranges[category]
            amount = round(random.uniform(min_amount, max_amount), 2)

            transactions.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'description': description,
                'category': category,
                'amount': amount,
                'type': 'income'
            })

        current_date += timedelta(days=1)

    return transactions

# Generate 12 months of data
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

print("Generating transactions...")
transactions = generate_transactions(start_date, end_date)

# Convert to dataframe
df = pd.DataFrame(transactions)

# Sort by date
df = df.sort_values('date').reset_index(drop=True)

# Save to CSV
output_path = os.path.join('data', 'transactions_raw.csv')
df.to_csv(output_path, index=False)

print(f"Done! {len(df)} transactions generated.")
print(f"File saved to: {output_path}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nDate range: {df['date'].min()} to {df['date'].max()}")
print(f"Total income: £{df[df['type']=='income']['amount'].sum():,.2f}")
print(f"Total expenses: £{df[df['type']=='expense']['amount'].sum():,.2f}")