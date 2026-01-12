# Agrigulture Vision System

O objetivo principal é processar imagens aéreas capturadas por drones para diferenciar a vegetação do solo, permitindo análises de cobertura vegetal e monitoramento da lavoura.

> Projeto desenvolvido com o intuito de pôr em prática os conhecimentos da biblioteca **OpenCV**.

## Scripts Disponíveis

Na pasta `Agriculture_Projects`, você encontrará os seguintes códigos:

| Arquivo | Descrição |
| :--- | :--- |
| **`plantationProject.py`** | Realiza a segmentação da imagem, distinguindo apenas a vegetação do solo. |
| **`porcentageBiomass.py`** | Além de distinguir a vegetação, calcula e exibe a **porcentagem** da área total que possui vegetação (biomassa). |

## Funcionalidades
- Processamento de imagens capturadas por drones.
- Segmentação de imagem: Diferenciação entre Planta e Terra.
- Cálculo de porcentagem de cobertura verde.

## Tecnologias Utilizadas
- **Linguagem:** Python.
- **Bibliotecas:** OpenCV e Numpy.

## Como Rodar o Programa
1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/caio-alm/agri-vision-system.git](https://github.com/caio-alm/agri-vision-system.git)
   ```

2. **Entre na pasta:**
   ```bash
   cd cd agri-vision-system
   ```
3. **Instale o requirements.txt:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Execute o processamento: Navegue até a pasta de projetos e rode o script:**
   ```bash
   cd Agriculture_Projects
   python seu_arquivo.py
