stop_words = ["de", "la", "le", "est", "ce", "que", "du","les", "des", "je", "tu"]
phrase_user = ["lance", "la", "chanson", "de", "mazzy", "star"]

resultat = [mot for mot in phrase_user if mot not in stop_words]
print(resultat)