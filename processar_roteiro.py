def processar_roteiro(texto_roteiro):
    texto_roteiro = texto_roteiro.lower()

    cenas = []

    if "gol" in texto_roteiro:
        cenas.append("Cena de gol sendo marcado")
    if "drible" in texto_roteiro:
        cenas.append("Cena de drible desconcertante")
    if "defesa" in texto_roteiro or "goleiro" in texto_roteiro:
        cenas.append("Defesa impressionante do goleiro")
    if "torcida" in texto_roteiro:
        cenas.append("Torcida vibrando no estádio")
    if "cartão vermelho" in texto_roteiro:
        cenas.append("Jogador sendo expulso com cartão vermelho")
    if "cartão amarelo" in texto_roteiro:
        cenas.append("Jogador recebendo cartão amarelo")
    if "pênalti" in texto_roteiro:
        cenas.append("Cobrança de pênalti")
    if "comemoração" in texto_roteiro:
        cenas.append("Comemoração dos jogadores")

    if not cenas:
        cenas.append("Cenas gerais de jogo de futebol")

    return cenas

# Exemplo de teste
if __name__ == "__main__":
    roteiro_exemplo = """
    Um jogador faz um drible incrível, em seguida marca um gol. 
    Logo depois o goleiro faz uma defesa espetacular, e a torcida comemora muito!
    """
    resultado = processar_roteiro(roteiro_exemplo)
    for cena in resultado:
        print(cena)
