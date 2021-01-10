import json
import hashlib

# print(r.json())
with open('answer.json', 'w') as json_file:
    json.dump(json_file.json(), json_file, indent=4)
    
with open('answer.json', 'r') as json_file:
    answer = json.load(json_file)
numero_casas = answer["numero_casas"]
# print(numero_casas)

cifrado = answer["cifrado"]
# print(cifrado)

tamanho = len(cifrado)  # 46
answer["decifrado"] = ""

# 97 - (a)  até  122 - (z)
# caso menor que 97 ou maior que 122 = permanecer o numero.
# (chr) -> retorna letra através de um numero.
# (ord) -> retorna um numero através de uma letra.

for i in range(tamanho):
    if ord(cifrado[i]) < 97 or ord(cifrado[i]) > 122:
        answer["decifrado"] += cifrado[i]

    elif((ord(cifrado[i])-numero_casas) < 97):
        answer["decifrado"] += chr(ord(cifrado[i])-numero_casas+26)
    
    elif((ord(cifrado[i])-numero_casas) > 122):
        answer["decifrado"] += chr(ord(cifrado[i])-numero_casas-25)
    
    else:
        answer["decifrado"] += chr(ord(cifrado[i])-numero_casas)
# print(answer["decifrado"])

answer["resumo_criptografico"] = hashlib.sha1(
    answer["decifrado"].encode('utf-8')).hexdigest()
    
with open('answer.json', 'w') as json_file:
    json.dump(answer, json_file, indent=4)