import hashlib
import hmac

#“PRNG acts as an entropy expander with evolving internal state”
class HybridPRNG:
    def __init__(self, seed: int):
        self.key = seed.to_bytes((seed.bit_length() + 7) // 8, 'big')
        self.counter = 0

    def random_bits(self, n_bits):
        output = b''
        while len(output) * 8 < n_bits:
            self.counter += 1
            msg = self.counter.to_bytes(8, 'big')
            block = hmac.new(self.key, msg, hashlib.sha256).digest()
            output += block

        bits = ''.join(f"{b:08b}" for b in output)
        return bits[:n_bits]
