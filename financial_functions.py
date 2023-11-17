def present_amount(P, r, n):
    return P*(1 + r/100)**n

def initial_amount(A, r, n):
    return A*(1 + r/100)**(-n)

def annual_rate(P, A, n):
    return 100*((A/P)**(1.0/n) - 1)