# Sala Startup do Source



# Description

Enumerate and root the box attached to this task. Can you discover the source of the disruption and leverage it to take control?




# Requisitos para invasão
- [x] Nmap
- [x] FTP
- [x] Ffuf
- [x] Alguma web shell php
- [x] nc





# Scan Inicial 

![vuln2.jpg](img/scan.png)



# Descobrimos uma tela de login aqui no webmin
![vuln2.jpg](img/tela_de_login_webmin.png)


# Procurando exploit no Metasploit
![vuln2.jpg](img/search_weebmin.png)


# Comandos no exploit
![vuln2.jpg](img/comandos_msfconsole.png)

# Root
![vuln2.jpg](img/whoami2.png)