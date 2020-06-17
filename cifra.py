import requests
import json
import hashlib

token = "5a68a31e69a1d5f96597deb45b09c576553500a0"

res = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='+token)

alf = [x for x in "abcdefghijklmnopqrstuvwxyz"]
a = json.loads(res.text)
def cifraEncr(casas,frase):
    casas = casas -1
    cifrado = []
    for x in frase:
        if x not in alf:
            cifrado.append(x)
            continue
        local = alf.index(x)
        limite = local + casas +1
        while limite/len(alf) >= 1:
            limite  = limite - len(alf)
        cifrado.append(alf[limite])
    return ''.join(cifrado)

def cifraDencr(casas,frase):
    cifrado = []
    for x in frase:
        if x not in alf:
            cifrado.append(x)
            continue
        local = alf.index(x)
        limite = local - casas
        if limite < 0:
            limite*=(-1)
            limite = len(alf) - limite
        while limite/len(alf) >= 1:
            limite  = limite - len(alf)
        cifrado.append(alf[limite])
    return ''.join(cifrado)

if a['cifrado'] != '':
    print("cifrado")
    print("entrada: ",a['cifrado'])
    b = cifraDencr(a['numero_casas'],a['cifrado'])
    print("saida: ",b)
if a['decifrado'] != '':
    print("decifrado")
    print("entrada: ",a['decifrado'])
    b = cifraEncr(a['numero_casas'],a['decifrado'])
    print("saida: ",b)

obj = hashlib.sha1(b.encode('UTF-8'))
dig = obj.hexdigest()
print(dig)
a['decifrado'] = b
a['resumo_criptografico'] = str(dig)

print(a)
with open('answer.json','w') as f:
    f.write(json.dumps(a))
    f.close()
with open('answer.json','r') as f:
    res = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='+token,files={'answer':f})
    print(res.status_code)
# cifra(a['numero_casas'],a['cifrado'])