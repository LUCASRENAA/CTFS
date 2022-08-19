# Sala Agent-sudo do TryHackMe



# Description

You found a secret server located under the deep sea. Your task is to hack inside the server and reveal the truth.


# Requisitos para invasão
- [x] BurpSuite


# Realizando o scan no alvo encontramos 3 portas abertas 

![vuln2.jpg](img/scan.png)


```
nmap 10.10.189.69 

```

## Tela inicial onde temos a dica do user-agent
![vuln2.jpg](img/telainicial.png)

## Depois de alterar o User-agent para R, onde percebi que tem uma saída diferente, fiz um bruteforce com o intruder do burp para encontrar outros usuários onde encontrei o usuário C

![vuln2.jpg](img/burp.jpeg)


## Ao ser redirecionado alterando o user-agent, descobrimos o nome verdadeiro do usuário, e com isso podemos realizar um bruteforce no ftp tanto para o usuário chris tanto para o C
![vuln2.jpg](img/redirecionamento.png)

## Descobrimos a senha do alvo
![vuln2.jpg](img/hydra_bruteforce.png)

```
hydra -L possiveis_login -P /usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt ftp://10.10.189.69
```

~só consegui até aqui sem  o writeup ~


## Extrair o zip da imagem
![vuln2.jpg](img/binwalk.png)

## Quebrando a senha do zip
![vuln2.jpg](img/quebrandozip.png)


## Extraindo arquivo
![vuln2.jpg](img/dezip_com_a_senha_alien.png)

## Senha em base64 do outro arquivo
![vuln2.jpg](img/base64.png)

## Com isso conseguimos achar a ultima messagem que é a senha do ssh do alvo
![vuln2.jpg](img/mensagem_final.png)


## Dentro do ssh encontrei a imagem de um alien
![vuln2.jpg](img/baixando_imagem_do_aliem.png)

## Procurei imagem no google
![vuln2.jpg](img/investigar_foto.png)

## Encontrei o caso na foxnews
![vuln2.jpg](img/incidente.png)


## root no ssh
![vuln2.jpg](img/root.png)

CVE:
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-14287

Comando root
```
sudo -u \#$((0xffffffff)) /bin/bash
```