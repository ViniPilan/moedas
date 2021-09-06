# Moedas - Informações e conversor

## Acesso a aplicação
Para acessar a aplicação basta acessar o link https://share.streamlit.io/vinipilan/moedas/script_web.py, ou clicar [aqui](https://share.streamlit.io/vinipilan/moedas/script_web.py)

## Objetivo
Desenvolver uma aplicação capaz de, ao usuário fornecer o nome de uma moeda, apresentar o preço (em real), a variação do preço dos últimos dias e uma calculadora de conversão de valor, que converte a moeda em questão para real ou valor em real para a moeda (dolar para real ou real para dolar, por exemplo).

Aplicação tem atualização autônoma: Atualizações diariamente das informações voláteis (preço e variação) por meio de web scraping.

## Metas
1. Geração automática de um data frame com as informações de cada moeda e informações sobre o momento da atualização.
2. Aplicação lê o data frame criado em 1, em tempo real, e já atualiza na tela do StreamLit.
3. O aplicativo também deve apresentar uma calculadora que realize a conversão do preço da moeda de acordo com o valor inserido pelo usuário.

## Desenvolvimento
1. Criar código de automação web scraping;
2. Criar data frame utilizando as informações obtidas no processo 1;
3. Criar uma aplicação com o StreamLit que possa ler o processo 2 e atualizar o front-end em tempo real;
4. Hospedagem do programa com o StreamLit no github.

## Moedas abrangidas
- Dólar Americano
- Euro
- Libra esterlina
- Iene
- Peso Argentino
- Bitcoin


## Sobre os códigos:
### script_web.py (código da página)
Código principal de toda a aplicação. Nele, estão contidos os códigos sobre a estrutura do site, sobre os widgets que o usuário pode interagir, sobre os dados expressos em gráfico, sobre a calculadora e sobre os textos que aparecem na tela.

### web_scraping.py (código do web scraping)
Código responsável por atualizar os dados do arquivo [moedas.csv](https://github.com/ViniPilan/moedas/blob/master/moedas.csv). Ao ser executado, faz uma busca, através do Chrome, de todas as moedas abrangidas pela aplicação, armazenando o nome de cada moeda, o valor, a data e o horário em que a busca foi feita. 

Ademais, esse mesmo arquivo contém a restrição de armazenar apenas uma busca de cada moeda por dia. Portanto, caso duas execuções desse programa aconteçam no mesmo dia, uma sobrescreve os dados da outra, ficando apenas armazenados os dados resultantes da execução mais recente.

Além disso, a execução desse código cria/atualiza o arquivo [moedas_anteriores_backup.csv](https://github.com/ViniPilan/moedas/blob/master/moedas_anteriores_backup.csv), que contém uma cópia do data frame para moedas armazenadas no dia anterior da atual execução de web_scraping.py. 

### funcoes.py (código de funções)
Tal código contém funções auxiliares que são utilizadas pelo script principal. Cada função presente no arquivo tem seu funcionamento descrito no próprio código.

## Ferramentas utilizadas
Os códigos foram desenvolvidos utilizando a linguagem de programação Python, juntamente com as seguintes bibliotecas:

- Pandas
- Plotly
- Streamlit
- Selenium (webdriver para Chrome)
- Datetime
- Os

## Sobre o autor
Me chamo Vinícius Pilan, sou estudante de Ciência da Computação pela Universidade Estadual Paulista 'Júlio de Mesquita Filho' UNESP, no campus de Bauru. Pretendo me especializar na área de dados e este projeto faz parte do meu portifólio de projetos. Para saber mais sobre mim e outros projetos de autoria minha, deixo algumas das minhas redes sociais:

- Linkedin: Vinícius de Paula Pilan
- GitHub: [ViniPilan](https://github.com/ViniPilan)
- GitHub do projeto: https://github.com/ViniPilan/moedas
