def f(n):
    if n == 0:
        return [0]
    r = []
    if n < 0:
        r.append(-1)
        n = -n
    i = 2
    while i * i <= n:
        while n % i == 0:
            r.append(i)
            n //= i
        i += 1
    if n > 1:
        r.append(n)
    return r


if __name__ == "__main__":
    x = input()
    try:
        x = int(x)
    except:
        raise SystemExit

    a = f(x)
    for i in range(len(a)):
        if i > 0:
            print(" ", end="")
        print(a[i], end="")