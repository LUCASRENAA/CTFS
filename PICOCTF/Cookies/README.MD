# Laborátorio Cookies do picoCTF

Esse laborátorio Cookies do picoCTF tem como objetivo fazer com que o pentester aprenda a manipular os cookies em questão, aqui utilizarei o burp e com a opção de intruder para capturar a flag em questão.


# Requisitos para invasão
- [x] BurpSuite



# Tela inicial do Lab

Aqui vemos um input que tem uma sugestão para colocar um cookie "snickerdoodle", não esqueçam de deixar o burp com o intercept on
![vuln2.jpg](img/telainicial.jpeg)

# Interceptando requisição
Aqui encontramos a requisição no burp, tem o campo do cookie ali, que poderia ser usado para mais tarde um bruteforce, vamos passar a requisição para ver se tem outra coisa legal.
![vuln2.jpg](img/interceptei_primeira_requisição.jpeg)

# Achamos o cookie aqui
Aqui na segunda requisição achamos o campo cookie, e ele tem o valor 0, provavelmente porque é o primeiro cookie, vamos realizar um bruteforce nesse campo, iremos jogar essa requisição no intruder
![vuln2.jpg](img/segunda_requisição_com_cookie.jpeg)

# Configurar o intruder
E como vimos que o cookie era "0" o padrão deve ser números inteiros.

Vamos configurar para um bruteforce de 0 a 100
![vuln2.jpg](img/configurei_o_intruder.jpeg)

# Key encontrada
Filtrando pelo tamanho da requisição e o status 200, achamos a key do CTF
![vuln2.jpg](img/achei_a_key.jpeg)

