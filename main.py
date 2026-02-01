from qrng import get_qrng_bits
from hybrid_entropy import get_classical_entropy, generate_hybrid_seed
from prng import HybridPRNG
from prime_gen import generate_prime

def main():
    print("[*] Fetching quantum entropy...")
    qrng_bits = get_qrng_bits(512)

    print("[*] Generating classical entropy...")
    crng_bits = get_classical_entropy(4096)

    print("[*] Creating hybrid seed...")
    seed = generate_hybrid_seed(qrng_bits, crng_bits)

    print("[*] Initializing PRNG...")
    prng = HybridPRNG(seed)

    print("[*] Generating RSA prime p...")
    p = generate_prime(prng)

    print("[*] Generating RSA prime q...")
    q = generate_prime(prng)

    print("\nRSA primes generated:")
    print("p =", p)
    print("q =", q)
    print("p == q ?", p == q)


if __name__ == "__main__":
    main()
