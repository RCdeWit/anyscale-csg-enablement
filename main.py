import ray

from math import isqrt
from utils.init_logger import init_logger

@ray.remote
def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False

    # Check divisibility up to square root
    for i in range(3, isqrt(num) + 1, 2):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    # Initialize Ray first, before any Ray operations
    ray.init()
    logger = init_logger(name="prime_finder", level="INFO")

    upper_limit = 2**20

    logger.info(f"Starting prime number calculation up to {upper_limit}")

    # Create tasks for each number
    prime_refs = [is_prime.remote(i) for i in range(upper_limit)]

    # Process results in chunks to avoid memory issues
    chunk_size = 10000
    total_chunks = (len(prime_refs) + chunk_size - 1) // chunk_size
    logger.info(f"Total chunks to process: {total_chunks}")

    primes = []

    for chunk_idx in range(total_chunks):
        start_idx = chunk_idx * chunk_size
        end_idx = min(start_idx + chunk_size, len(prime_refs))

        logger.info(f"Processing chunk {chunk_idx+1}/{total_chunks} (indices {start_idx} to {end_idx-1})")

        chunk_refs = prime_refs[start_idx:end_idx]
        results = ray.get(chunk_refs)

        # Filter prime numbers
        chunk_primes = []
        for j, is_prime_result in enumerate(results):
            if is_prime_result:
                chunk_primes.append(start_idx + j)

        primes.extend(chunk_primes)
        logger.info(f"Found {len(chunk_primes)} primes in chunk {chunk_idx+1}")

    logger.info(f"Total prime numbers found: {len(primes)}")

    # logging.info(f"Primes found: {primes}")
    ray.shutdown()