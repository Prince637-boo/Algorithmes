def factorielle(n):
    if n == 0 or n == 1:       # Cas de base
        return 1
    else:
        return n * factorielle(n - 1)  # Appel récursif
