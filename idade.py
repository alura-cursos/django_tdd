def descobrir_idade(ano_nascimento, ano):
    return ano - ano_nascimento

assert descobrir_idade(1991, 2050) == 59

print(descobrir_idade(1996, 2060))