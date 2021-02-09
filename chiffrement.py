def chiffrement(message):
    message_chiffre = ""
    for lettre in message:
        nb_lettre = ord(lettre) -65
        nb_lettre_chiffree = (nb_lettre+3) % 26
        lettre_chiffree = chr(nb_lettre_chiffree + 65)
        message_chiffre += lettre_chiffree
    return message_chiffre