import random as rd

# Gerar a estrutura de silabas no taamnho correspondente
# Gerar o Nome a Partir da Estrutura de Silabas
# Retornar o Nome Completo


class Gerador_Nome_Aleatorio():
    def __init__(self, tamanho=0):
        self.tamanho = tamanho

        self.consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j',
                           'k', 'l', 'm', 'n', 'p', 'q', 'r',
                           's', 't', 'v', 'w', 'x', 'z']

        self.consoantes_finais = ['s', 'z', 'x', 'r', 'l', 'm', 'n']
        self.especiais = ['-', '\'']
        self.vogais = ['a', 'e', 'i', 'o', 'u']

        self.silabas = ['CV', 'V', 'CVC', 'CCV', 'VC', 'VV', 'CVV', 'VCC']
        self.silabas_pesos = [10, 9, 2, 1, 2, 2, 3, 2, ]

        self.estrutura = []
        self.nome = []

        self.Gerar_Estrutura()
        self.Gerar_Nome()

    def Gerar_Estrutura(self):
        tamanho = 0
        especial = 0
        # Gerar Tamanho do nome de acordo com o parametro
        if self.tamanho == 0:
            tamanho = rd.randint(1, 3)
        elif self.tamanho == 1:
            tamanho = rd.randint(2, 3)
            especial = rd.randint(0, 100)
        elif self.tamanho == 2:
            tamanho = rd.randint(3, 5)
            especial = rd.randint(0, 100)
        else:
            tamanho = rd.randint(2, 4)

        # Gerar Estrutura

        for i in range(tamanho):
            self.estrutura.append(rd.choices(
                self.silabas, weights=self.silabas_pesos))
            especial = rd.randint(0, 100)
            if especial > 95 and i < tamanho-1:
                self.estrutura.append(rd.choices(
                    self.especiais, weights=[1, 5]))


    def Gerar_Nome(self):
        for i in self.estrutura:
            silaba = "".join(i)
            final = 1
            for i in silaba:
                if final == len(silaba) and i == 'C':
                    self.nome.append(rd.choice(self.consoantes_finais))
                    continue

                if i == "C":
                    self.nome.append(rd.choice(self.consoantes))
                elif i == "V":
                    self.nome.append(rd.choice(self.vogais))
                else:
                    self.nome.append(rd.choice(i))
                final +=1          

    def Retornar_Nome(self):
        nome = "".join(self.nome)
        return nome

# i = 0
# texto = ''
# while i <100:

#     nome = Gerador_Nome_Aleatorio(2)
#     texto += 'Nome => '+nome.Retornar_Nome()+'\n'
#     i +=1
# print(texto)
'''
C = Consoante, V - Vogal
*CV = Sílaba Canônica (Mais Comum)

EXEMPLOS:

CV => CABELO, HIPOPÓTAMO
CCV => PRAto, caTRAca, CLAro, FRÁgil
CVV => BOI, InspiraÇÃO
CVC => CANsado, AMOr, aDULto
V => Amor
VC => EScola
VCC => INSpiração 
CCVCC => TRANSforma
CCVV => TROUxe
CVVC => QUANto

'''
