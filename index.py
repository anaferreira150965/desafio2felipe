vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))
saldoVitorias = vitorias - derrotas

if saldoVitorias <= 10:
   nivel = "Ferro"
elif saldoVitorias <= 20:
   nivel = "Bronze"
elif saldoVitorias <= 50:
   nivel = "Prata "
elif saldoVitorias <= 80: 
   nivel = "Ouro"
elif saldoVitorias <= 90:
   xp = "Diamante"
elif saldoVitorias >= 101:
   nivel = "Imortal"
else:   
   nivel = "Radiante"
print(f"O Herói tem de saldo de {saldoVitorias} está no nível de {nivel}")

 