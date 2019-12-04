# Day 4

print('Day 4')

ok_sum = 0
for password in range(256310, 732736):
    decresing = False
    double = False
    last = -1
    streak = 1
    for n in str(password):        
        
        n_i = int(n)
        
        if last == n_i :
            streak += 1
        else:
            if streak == 2:
                double = True
            streak = 1
            
        if last > n_i:
            decresing = True
            break
            
        last = n_i

    if not decresing and double or streak == 2:
        print("OK: ", password)
        ok_sum += 1

print(str(ok_sum) + " viable passwords.")
