def gauss(coeffs):
    a = np.copy(coeffs)
    n = len(a)
    # drive to upper-diagonal form
    for i in range(n):
        if a[i][i] == 0.0:
            print('Divide by zero detected!')
            break
        for j in range(i+1,n):
            scale = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - scale * a[i][k]
    # backfill
    x = np.zeros(n)
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = x[i]/a[i][i]
    return x
