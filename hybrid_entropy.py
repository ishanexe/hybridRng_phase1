import secrets

def get_classical_entropy(n_bits=4096):
    """Cryptographically secure classical entropy"""
    return ''.join(str(secrets.randbits(1)) for _ in range(n_bits))


def xor_bits(a, b):
    min_len = min(len(a), len(b))
    return ''.join(
        '1' if a[i] != b[i] else '0'
        for i in range(min_len)
    )


def generate_hybrid_seed(qrng_bits, crng_bits):
    hybrid = xor_bits(qrng_bits, crng_bits)
    return int(hybrid, 2)
