# Fortigate Firewall Formatting Logs

Este script foi desenvolvido para extrair informações relevantes dos logs do webfilter de usuários do firewall FortiGate da Fortinet. O objetivo é fornecer uma maneira simples e eficiente de analisar o histórico de navegação de usuários, permitindo verificar sites visitados, se o acesso foi permitido ou bloqueado pelo firewall, detalhes da URL acessada, e outras informações de tráfego relacionadas ao web filter. Com isso, é possível realizar uma análise mais detalhada do comportamento de navegação dentro da rede, facilitando a monitoração e auditoria do tráfego de internet. Este script organiza os dados de maneira legível, ajudando a identificar padrões de acesso, sites bloqueados e permitir o acompanhamento eficaz da utilização da web pelos usuários monitorados.

## Baixando
Você pode baixar o script apenas clonando diretamente o repositório
``` bash
git clone https://github.com/andradesysadmin/formatlogpy
cd formatlogpy
```
ou através da sua imagem docker
``` bash
git clone https://github.com/andradesysadmin/formatlogpy
cd formatlogpy
docker build -t formatlogs .
docker run -it formatlogs bash
```

## Usando


Para executar o script use
``` bash
    python3 main.py meulog.log saida.log

```

ou execute a partir do notebook index.ipynb
