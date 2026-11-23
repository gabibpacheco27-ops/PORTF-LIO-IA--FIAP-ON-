# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../assets/logo-fiap.png" 
       alt="FIAP - Faculdade de Informática e Administração Paulista" 
       width="40%">
</a>
</p>

<br>

# Nome do projeto/atividade

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="Link do perfil no LinkedIn ou GitHub">Gabriela Pacheco - RM575120</a>
- <a href="Link do perfil no LinkedIn ou GitHub">Raila Cruz - RM576112</a>
- <a href="Link do perfil no LinkedIn ou GitHub">Leonardo Kenji - RM575829</a> 
- <a href="Link do perfil no LinkedIn ou GitHub">Gabriel Pietrobon - RM574967</a> 


## 👩‍🏫 Professores:

### Tutor(a)
- <a href="Link do perfil no LinkedIn">Sabrina Otoni</a>
  
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi Chiovato</a>

## 📜 Descrição

*Este projeto analisa custos de uma frota com dados simulados de combustível, manutenção, pedágios, multas e impostos. O programa integra os dados, compara veículos de perfis semelhantes e identifica quais apresentam custos acima do esperado. Também compara o diagnóstico por regras com o resultado de um modelo de Machine Learning e inclui uma simulação de telemetria com ESP32 no Wokwi.*

## 📁 Estrutura de pastas 
TODOS OS ARQUIVOS DO PROJETO SE ENCONTRAM NA PASTA ZIP
| CONTEÚDO DENTRO DO ZIP |
|---|---|
| `main.py` e `requirements.txt` | Programa principal e dependências |
| `src/` | Código de tratamento dos dados, comparação de custos, diagnóstico e modelo |
| `data/` | Dados simulados de entrada, telemetria e arquivos processados |
| `outputs/` e `assets/` | Tabelas de resultados, gráficos e diagrama do projeto |
| `wokwi/` e `telemetria/` | Código e circuito do ESP32 e scripts para gerar ou importar leituras |
| `tests/` | Testes das regras de diagnóstico |
| `docs/` e `notebooks/` | Documentação, evidências da simulação e notebook de análise |



### 🔗 Links do Projeto

* **[Nome do Link (Video demonstração do funcionamento do projeto da sprint 2)]**(https://youtu.be/hlGBrp3aKME) 



### 📢 Observações Gerais


* **Participação na Competição:** [x] Sim, aceitamos participar / [ ] Não vamos participar.
* *Outras observações gerais (opcional):* Escreva aqui...

## 🔧 Como executar o código

*Você precisa ter o **Python 3.10 ou superior** instalado.

No macOS ou Linux, crie e ative o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows, usando o Prompt de Comando:

```bat
python -m venv .venv
.venv\Scripts\activate
```

Depois, instale as dependências e execute o projeto:

```bash
python -m pip install -r requirements.txt
python main.py
```

Para executar os quatro testes das regras de diagnóstico:

```bash
python -m unittest discover -s tests -p "teste_*.py" -v
```.*

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/fiap-tutoria/FIAP-PORTFOLIO-AI">TEMPLATE - FIAP PORTFÓLIO AI</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
