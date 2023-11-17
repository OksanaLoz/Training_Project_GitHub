from financial_functions import years

P = 1; r = 5
n = round(years(P, 2*P, r))

print(f'Money has doubled after {n} years')