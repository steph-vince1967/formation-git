def total_ht(quantite, prix_unitaire):
    if quantite < 0 or prix_unitaire < 0:
        raise ValueError("Les valeurs doivent etre positives")
    return quantite * prix_unitaire
