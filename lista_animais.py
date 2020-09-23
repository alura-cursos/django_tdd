lista_animais = [
    {'nome_animal':'urso','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'javali','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'búfalo','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'guepardo','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'molusco','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'caranguejo','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'lagostim','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'corvo','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'golfinho','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'pomba','predador': 'não','venenoso': 'não','domestico': 'sim'},
    {'nome_animal':'pato','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'elefante','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'flamingo','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'pulga','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'rã','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'morcego-da-fruta','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'girafa','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'mosquito','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'bode','predador': 'não','venenoso': 'não','domestico': 'sim'},
    {'nome_animal':'gorila','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'gaivota','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'hadoque','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'hamster','predador': 'não','venenoso': 'não','domestico': 'sim'},
    {'nome_animal':'falcão','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'abelha','predador': 'não','venenoso': 'sim','domestico': 'sim'},
    {'nome_animal':'mosca','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'joaninha','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'leopardo','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'leão','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'lagosta','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'lince','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'salamandra','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'polvo','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'gambá','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'órix','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'avestruz','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'periquito','predador': 'não','venenoso': 'não','domestico': 'sim'},
    {'nome_animal':'pinguim','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'faisão','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'pique','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'piranha','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'ornitorrinco','predador': 'sim','venenoso': 'sim','domestico': 'não'},
    {'nome_animal':'doninha','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'pónei','predador': 'não','venenoso': 'não','domestico': 'sim'},
    {'nome_animal':'toninha','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'puma','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'gato','predador': 'sim','venenoso': 'não','domestico': 'sim'},
    {'nome_animal':'guaxinim','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'rena','predador': 'não','venenoso': 'não','domestico': 'sim'},
    {'nome_animal':'ema','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'escorpião','predador': 'sim','venenoso': 'sim','domestico': 'não'},
    {'nome_animal':'cavalo marinho','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'leão marinho','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'verme','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'lesma','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'pardal','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'esquilo','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'estrela do Mar','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'arraia','predador': 'sim','venenoso': 'sim','domestico': 'não'},
    {'nome_animal':'cisne','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'cupim','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'sapo','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'tartaruga','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'tuatara','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'atum','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'abutre','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'vespa','predador': 'não','venenoso': 'sim','domestico': 'não'},
    {'nome_animal':'lobo','predador': 'sim','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'minhoca','predador': 'não','venenoso': 'não','domestico': 'não'},
    {'nome_animal':'carriça','predador': 'não','venenoso': 'não','domestico': 'não'}
]

import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from animais.models import Animal

def gerando_animais():
    for animal in lista_animais:
        nome = animal['nome_animal']
        predador = animal['predador']
        venenoso = animal['venenoso']
        domestico = animal['domestico']
        animal = Animal(nome_animal=nome, predador=predador, venenoso=venenoso, domestico=domestico)
        animal.save()

gerando_animais()
print('animais gerados')