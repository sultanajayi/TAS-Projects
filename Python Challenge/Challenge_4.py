#P*R*T / 100  where A = final amount ,P = initial principal balance  r =interest rate t = time


def simple_interest(principal, rate, time):

    si = principal*rate*time
    result = si/100
    print(result)
    return result


simple_interest(2000, 9, 1)
