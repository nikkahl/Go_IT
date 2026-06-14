import random

def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list:
    if not (1 <= min_val <= max_val <= 1000):
        return []
    
    if not (1 <= quantity <= (max_val - min_val + 1)):
        return []

    return sorted(random.sample(range(min_val, max_val + 1), quantity))
