<p align="center">
  <img src="./assets/python.png" width="300" alt="Python" /></a>
</p>

# API WISE-4051 ADVANTECH
```bash
Envie dados computados de um sensor a laser através do dispositivo Wise 4051 Advantech 
para uma base de dados SQLServer via Python.
```

## Fluxo do processo
<p align="center">
  <img src="./assets/fluxo.png" width="700" alt="Python" /></a>
</p>

```bash
DETALHES: 

Neste processo o Produto na área Fabril vai passando na esteira e sendo computado pelos 
sensores em cada parte do processo de produção e embalagem, estes dados computados são 
armazenados em memória interna onde existe uma API dentro do dispositivo.

O que fazemos neste caso é ler esta api do próprio dispositivo na porta específica onde 
se encontra o sensor e coletar estes dados para serem enviados para uma tabela no 
banco de dados SQLServer.

De lá temos um DashBoard desenvolvido em Power BI que mostra os indicadores de produção, 
onde cada esteira de cada sensor cuida de ler um determinado produto e para este existe 
uma platforma em PHP que gerencia este controle de produção mostrando seus indicadores 
de produção conforme o que for produzido, podendo ser ajustado ou não.

```

## Pré-Requisitos
```bash
Neste cenário o cliente deverá ter:
1 - Gateway WISE-4051 - Advantech.
2 - Um sensor a laser para coletar os dados.
3 - Acesso ao APP via browser para efetuar os testes do dispositivo.
4 - Fazer a conexão com o dispositivo via Postman para finalizar o teste.
5 - Criar uma base de dados, ou já tê-la e incluir a tabela na mesma estrutura que está.
    o codigo fonte ou mudar de acordo com sua necessidade.
6 - Alterar no main.py os dados de acesso, ip, banco, user, senha e tabela.
7 - Realizar o teste executando os comando abaixo.
```

## Execução
```bash
$ pip install -r requirements.txt
$ python3 main.py
```

## Suporte
```bash
WhatsApp: 85 997635122
E-Mail: geraldo@gpsoft.com.br
```
