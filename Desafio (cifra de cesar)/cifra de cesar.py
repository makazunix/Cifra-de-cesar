import json
import hashlib

with open('answer.json', 'w') as json_file:
    json.dump(json_file.json(), json_file, indent=4)
    
with open('answer.json', 'r') as json_file:
    resposta = json.load(json_file)

numero_casas = resposta["numero_casas"]
cifrado = resposta["cifrado"]

tamanho = len(cifrado)  # 46
resposta["decifrado"] = ""

# 97 - (a)  até  122 - (z)
# caso menor que 97 ou maior que 122 = permanecer o numero.
# (chr) -> retorna letra através de um numero.
# (ord) -> retorna um numero através de uma letra.

for i in range(tamanho):
    if ord(cifrado[i]) < 97 or ord(cifrado[i]) > 122:
        resposta["decifrado"] += cifrado[i]

    elif((ord(cifrado[i])-numero_casas) < 97):
        answer["decifrado"] += chr(ord(cifrado[i])-numero_casas+26)
    
    elif((ord(cifrado[i])-numero_casas) > 122):
        resposta["decifrado"] += chr(ord(cifrado[i])-numero_casas-25)
    
    else:
        resposta["decifrado"] += chr(ord(cifrado[i])-numero_casas)

resposta["resumo_criptografico"] = hashlib.sha1(
    resposta["decifrado"].encode('utf-8')).hexdigest()

with open('answer.json', 'w') as json_file:
    json.dump(resposta, json_file, indent=4)