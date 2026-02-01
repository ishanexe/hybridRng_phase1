from sympy import isprime

def generate_prime(prng, bit_length=1024):
    attempts = 0

    while True:
        attempts += 1

        bits = prng.random_bits(bit_length)

        # Enforce constraints
        bits = '1' + bits[1:-1] + '1'  # MSB=1, odd
        candidate = int(bits, 2)

        if isprime(candidate):
            print(f"[✓] Prime found after {attempts} attempts")
            return candidate
