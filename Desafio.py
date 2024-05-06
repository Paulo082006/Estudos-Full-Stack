def repeatedString(s, n):
    contagem_a = s.count("a")
    repetiao = n // len(s)
    sobra = n % len(s)
    resultado = repetiao * contagem_a + s[:sobra].count("a")
    return resultado


