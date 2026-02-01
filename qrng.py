import requests
import os

ANU_QRNG_URL = "https://qrng.anu.edu.au/API/jsonI.php"

def get_qrng_bits(n_bits=512):
    """
    Fetch quantum random bits from ANU QRNG.
    Falls back to OS entropy if API fails.
    """
    try:
        n_bytes = n_bits // 8
        params = {
            "length": n_bytes,
            "type": "uint8"
        }
        r = requests.get(ANU_QRNG_URL, params=params, timeout=5)
        r.raise_for_status()
        data = r.json()["data"]

        bitstring = ''.join(f"{byte:08b}" for byte in data)
        return bitstring[:n_bits]

    except Exception as e:
        print("[!] QRNG failed, falling back to os.urandom")
        return ''.join(f"{b:08b}" for b in os.urandom(n_bits // 8))
