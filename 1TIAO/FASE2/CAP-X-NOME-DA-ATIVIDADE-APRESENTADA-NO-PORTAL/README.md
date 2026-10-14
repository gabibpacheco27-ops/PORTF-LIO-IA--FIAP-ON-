# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../../assets/logo-fiap.png" 
       alt="FIAP - Faculdade de Informática e Administração Paulista" 
       width="40%">
</a>
</p>

<br>

# Nome do projeto/atividade

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="Link do perfil no LinkedIn ou GitHub">Raila Cruz</a>
- <a href="Link do perfil no LinkedIn ou GitHub"> Gabriela Pacheco</a>
- <a href="Link do perfil no LinkedIn ou GitHub">Leonardo Kenji</a> 
- <a href="Link do perfil no LinkedIn ou GitHub">Gabriel Pietrobon 4</a> 


## 👩‍🏫 Professores:

### Tutor(a)
- <a href="Link do perfil no LinkedIn">Sabrina Otoni</a>
  
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi Chiovato</a>

## 📜 Descrição
# Análise de Dados do Agronegócio com R

## Sobre o projeto

Este projeto acadêmico foi desenvolvido na FIAP com o objetivo de aplicar conceitos de estatística e análise de dados ao agronegócio brasileiro.

O trabalho reúne a pesquisa de dados públicos, a organização de bases em Excel e a realização de análises no R, envolvendo variáveis quantitativas e qualitativas.

## Objetivos

- Pesquisar dados reais sobre o agronegócio em fontes públicas.
- Identificar e classificar diferentes tipos de variáveis.
- Organizar os dados em planilhas.
- Calcular medidas estatísticas de uma variável quantitativa no R.
- Representar variáveis por meio de gráficos.
- Interpretar os resultados considerando o contexto e as limitações das bases.

## Organização das bases de dados

A atividade exige uma base com, pelo menos, 30 registros e quatro tipos de variáveis:

| Tipo de variável | Característica |
|---|---|
| Quantitativa discreta | Representa contagens, como o número de animais. |
| Quantitativa contínua | Representa medidas, como área, massa e volume. |
| Qualitativa nominal | Representa categorias sem ordem natural, como estado e região. |
| Qualitativa ordinal | Representa categorias ordenadas, como faixas baixa, média e alta. |

As bases utilizadas nas análises possuem recortes distintos. Por isso, os resultados devem ser interpretados conforme a fonte, o período e a unidade de observação de cada base.

## Análise quantitativa em R

A análise exploratória quantitativa utiliza a variável de área em hectares, identificada como `area_total_ha`, em uma base com 81 registros por unidade da Federação e uso da terra.

A fonte indicada para essa base é o Censo Agropecuário 2017 do IBGE, disponibilizado no SIDRA, tabela 6882.

O código contempla:

- **Medidas de tendência central:** média, mediana e verificação da moda.
- **Medidas de dispersão:** amplitude, variância amostral, desvio padrão amostral e coeficiente de variação.
- **Medidas separatrizes:** quartis, decis e percentis selecionados.
- **Análise gráfica:** histograma e boxplot.
- **Interpretação:** observação da dispersão, da assimetria e de possíveis valores extremos.

Os valores utilizados estão inseridos diretamente no script R, permitindo executar a análise sem importar a planilha.

## Análise qualitativa em R

A análise qualitativa utiliza a variável ordinal `faixa_leite`, construída a partir da produção anual de leite de 10 estados selecionados, nos anos de 2021, 2022 e 2023.

São 30 registros, sendo que cada linha representa um estado em um ano.

Os dados de produção têm como fonte a Pesquisa da Pecuária Municipal do IBGE, disponibilizada no SIDRA, tabela 74.

### Critérios das faixas

| Faixa | Produção anual de leite |
|---|---|
| Baixa | Até 1.000 milhões de litros, inclusive. |
| Média | Acima de 1.000 e até 3.000 milhões de litros, inclusive. |
| Alta | Acima de 3.000 milhões de litros. |

Essas faixas foram definidas para o trabalho. Não são classificações oficiais do IBGE e representam volume de produção, não qualidade do leite.

### Resultados

| Faixa | Frequência absoluta | Percentual |
|---|---:|---:|
| Baixa | 9 | 30,00% |
| Média | 8 | 26,67% |
| Alta | 13 | 43,33% |
| **Total** | **30** | **100,00%** |

A faixa Alta é a categoria mais frequente no recorte analisado, embora represente menos da metade dos registros.

Os percentuais mostram a proporção de registros em cada categoria. Eles não representam a participação das faixas no volume total de leite produzido.

O script insere os dados diretamente no R, constrói a variável ordinal, calcula as frequências e gera um gráfico de barras com interpretação dos resultados.

## Tecnologias utilizadas

- **Excel:** organização e documentação das bases.
- **R:** tratamento dos dados, cálculos estatísticos e geração de gráficos.
- **RStudio:** ambiente para execução dos scripts.
- **GitHub:** organização e compartilhamento dos arquivos do projeto.

## Como executar

1. Baixe os arquivos `.R` disponíveis neste repositório.
2. Abra o script desejado no RStudio.
3. Clique em **Source** para executar o código completo.
4. Consulte os resultados no Console e os gráficos gerados.

Os scripts utilizam funções do R base, sem necessidade de instalar pacotes adicionais.

O script `agronegocio_pessoa5.R` também salva o gráfico, os dados, a tabela de frequências e a interpretação na pasta `resultados_pessoa5`, criada dentro do diretório de trabalho do R.

## Divisão das atividades

| Integrantes | Responsabilidade |
|---|---|
| Pessoas 1, 2 e 3 | Pesquisa de dados públicos, seleção e classificação das variáveis e organização das planilhas com fontes, anos e links. |
| Pessoa 4 | Análise exploratória de uma variável quantitativa no R. |
| Pessoa 5 | Análise gráfica de uma variável qualitativa no R, acompanhada de interpretação. |

## Limitações

- Os resultados descrevem os recortes selecionados e não devem ser generalizados automaticamente para todo o agronegócio brasileiro.
- Registros agregados por estado ou uso da terra não representam propriedades rurais individuais.
- Na análise qualitativa, os mesmos estados aparecem em três anos; portanto, 30 registros não equivalem a 30 estados diferentes.
- As faixas ordinais dependem dos limites definidos no trabalho.
- As análises são descritivas e não demonstram relações de causa e efeito.

## Fontes

- [IBGE — Portal institucional](https://www.ibge.gov.br/)
- [IBGE — Censo Agropecuário 2017, SIDRA, tabela 6882](https://sidra.ibge.gov.br/tabela/6882)
- [IBGE — Produção de origem animal, SIDRA, tabela 74](https://sidra.ibge.gov.br/tabela/74)
- [IBGE — Efetivo dos rebanhos, SIDRA, tabela 3939](https://sidra.ibge.gov.br/tabela/3939)

Os períodos de referência e os detalhes das variáveis estão documentados nas bases e nos scripts correspondentes.
*Descreva aqui seu projeto em detalhes de forma estruturada e organizada*

## 📁 Estrutura de pastas 


Abaixo encontra-se a descrição da organização da raiz do projeto e a finalidade de cada diretório e arquivo:

* **`data/`** Armazena todas as bases de dados utilizadas no projeto, incluindo arquivos estruturados (como CSV, Excel, JSON), bases de dados sintéticas e outros formatos brutos ou processados.

* **`docs/`** Centraliza a documentação técnica e de negócio do projeto.

* **`IR-ALEM/`** Espaço reservado exclusivamente para desenvolvimentos do módulo opcional "Ir Além" da atividade. O objetivo é isolar este escopo para evitar a mistura com as entregas principais da atividade.

* **`notebooks/`** Destinado a cadernos interativos (como *Jupyter Notebooks* ou *Google Colab*) utilizados para análise exploratória de dados, experimentação de algoritmos, prototipagem de modelos, etc.

* **`src/`** Contém todo o código-fonte desenvolvido para o projeto. Dependendo do âmbito da atividade, pode incluir arquivos como: scripts (Python, R, JS), ficheiros web (HTML), firmware para hardware (ESP32/Arduino), além de APIs, microsserviços e ficheiros de modelos e inferências.

* **`README.md`** Este ficheiro. Funciona como o guia principal de introdução, configuração e contextualização do projeto.



* **[Nome do Link (ex: Vídeo de Entrega no YouTube)]**(http://url-aqui) - Breve descrição.



---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/fiap-tutoria/FIAP-PORTFOLIO-AI">TEMPLATE - FIAP PORTFÓLIO AI</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
