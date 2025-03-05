def staircase(n, display="#"):
    if not (0 < n <= 30):
        return False
    result = []
    for i in range(1, n + 1):
        row = " " * (n - i) + display * i
        result.append(row)
    return "\n".join(result)
