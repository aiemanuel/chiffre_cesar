def dechiffrement(message_chiffre):
    message_clair = " "
    for lettre_chiffree in message_chiffre:
        nb_lettre_chiffree = ord(lettre_chiffree) - 65
        nb_lettre_clair = (nb_lettre_chiffree - 3) % 26
        lettre_clair = chr(nb_lettre_clair + 65)
        message_clair += lettre_clair
    
    return message_clair