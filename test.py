import pandas as pd

df = pd.DataFrame({
    'customer': ['Ali', 'Sara', 'Omar', 'Nour'],
    'payment_method': ['Cash', 'Card', 'Wallet', 'Cash'],
    'amount': [50, 120, 30, 75]
})

print(df)

df_encoded = pd.get_dummies(df, columns=['payment_method'])
print(df_encoded)