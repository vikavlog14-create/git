def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n0.5) + 1):
        if n % i == 0: return False
    return True

def count_divisors(n):
    count = 0
    for i in range(1, int(n0.5) + 1):
        if n % i == 0:
            if i * i == n: count += 1
            else: count += 2
    return count

def solve(l, m):
    funny_count = 0
    for num in range(l, m + 1):
        # Число має бути складеним (не простим і > 1)
        if not is_prime(num) and num > 1:
            divs = count_divisors(num)
            # Кількість дільників має бути простим числом
            if is_prime(divs):
                funny_count += 1
                print(f"Кумедне число: {num} (дільників: {divs})")
    return funny_count
