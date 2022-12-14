# Laborátorio Scavenger Hunt do picoCTF

O objetivo do Laborátorio é conhecer a estrutura de arquivos de alguns serviços e de olhar com calma por conteúdo oculto nas páginas

## Description

There is some interesting information hidden around this site http://mercury.picoctf.net:5080/. Can you find it?


# Requisitos para invasão
- [x] Navegador



# Tela inicial
Depois de entrar no site, tive a curiosidade de abrir o código fonte para buscar por novas informações do site
![vuln2.jpg](img/telainicial.png)


#### HTML code
```html
<!doctype html>
<html>
  <head>
    <title>Scavenger Hunt</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="mycss.css">
    <script type="application/javascript" src="myjs.js"></script>
  </head>

  <body>
    <div class="container">
      <header>
		<h1>Just some boring HTML</h1>
      </header>

      <button class="tablink" onclick="openTab('tabintro', this, '#222')" id="defaultOpen">How</button>
      <button class="tablink" onclick="openTab('tababout', this, '#222')">What</button>

      <div id="tabintro" class="tabcontent">
		<h3>How</h3>
		<p>How do you like my website?</p>
      </div>

      <div id="tababout" class="tabcontent">
		<h3>What</h3>
		<p>I used these to make this site: <br/>
		  HTML <br/>
		  CSS <br/>
		  JS (JavaScript)
		</p>
	<!-- Here's the first part of the flag: picoCTF{t -->
      </div>

    </div>

  </body>
</html>

```

Vocês conseguiram achar a flag no código? 

Antes de comentar sobre a flag, quero que vocês guardem bem esses dois arquivos.

```html
  <link rel="stylesheet" type="text/css" href="mycss.css">
    <script type="application/javascript" src="myjs.js"></script>
```

E a flag está na linha comentada do html

```
	<!-- Here's the first part of the flag: picoCTF{t -->
```

Vamos ganhar essa primeira parte para somar com as outras flags: picoCTF{t





Essa falha tenta simular caso um desenvolvedor comente algo sensível no código fonte, pensando que o usuário não irá conseguir ver, pois, o código comentado não é renderizado na página, mas, como o código fonte é enviado ao cliente, outras pessoas poderiam ver esse código caso simplesmente olhassem o código fonte da aplicação.



Vamos olhar o CSS também

```html
 <link rel="stylesheet" type="text/css" href="mycss.css">
```


#### CSS code
```html
div.container {
    width: 100%;
}

header {
    background-color: black;
    padding: 1em;
    color: white;
    clear: left;
    text-align: center;
}

body {
    font-family: Roboto;
}

h1 {
    color: white;
}

p {
    font-family: "Open Sans";
}

.tablink {
    background-color: #555;
    color: white;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    font-size: 17px;
    width: 50%;
}

.tablink:hover {
    background-color: #777;
}

.tabcontent {
    color: #111;
    display: none;
    padding: 50px;
    text-align: center;
}

#tabintro { background-color: #ccc; }
#tababout { background-color: #ccc; }

/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```


Separando a flag para ficar de mais fácil visualização. 

```html
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

Agora a flag é : picoCTF{t + h4ts_4_l0

Vamos para o javascript


```html
<script type="application/javascript" src="myjs.js"></script>
```
#### JS code

```html
function openTab(tabName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
	tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
	tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(tabName).style.display = "block";
    if(elmnt.style != null) {
	elmnt.style.backgroundColor = color;
    }
}

window.onload = function() {
    openTab('tabintro', this, '#222');
}

/* How can I keep Google from indexing my website? */
```

Aqui não encontramos nada no javascript da flag, mas encontramos uma dica: Como posso impedir que o Google indexe meu site?

E esse arquivo é nada mais menos que o robots.txt


#### Robots.txt code

```html
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```


Agora a flag é : picoCTF{t + h4ts_4_l0 + t_0f_pl4c

A dica é sobre um arquivo do apache, tentando alguns arquivos consegui com o .htaccess

http://mercury.picoctf.net:5080/.htaccess

```html
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

Agora a flag é : picoCTF{t + h4ts_4_l0 + t_0f_pl4c + 3s_2_lO0k



Depois de pesquisar um pouco no google sobre arquivos ocultos no google
"file hidden mac directory commons filessystem"

com essa pesquisa achei esse link

# Pesquisa no google
![vuln2.jpg](img/pesquisagoogle.jpeg)

# Stackoverflow
![vuln2.jpg](img/arquivooculto.jpeg)


link: http://mercury.picoctf.net:5080/.DS_Store


#### .DB_Store code

```html
Congrats! You completed the scavenger hunt. Part 5: _35844447}
```


Agora a flag é : picoCTF{t + h4ts_4_l0 + t_0f_pl4c + 3s_2_lO0k + _35844447} 

E está completa! 
Laborátorio finaliazado!