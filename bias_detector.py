male_words = ["leadership", "analytical", "managed", "led"]
female_words = ["communication", "teamwork", "coordination", "support"]

def bias_score(text):
    m = sum(word in text.lower() for word in male_words)
    f = sum(word in text.lower() for word in female_words)

    total = m + f
    if total == 0:
        return 0

    return round(abs(m - f) / total * 100, 2)