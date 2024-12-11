### README: Simulador de Lucro - Última do Semestre

---

#### Descrição do Projeto

O **Simulador de Lucro - Última do Semestre** foi desenvolvido para atender a uma necessidade prática durante o planejamento de um evento. A ideia surgiu da demanda de calcular e simular com precisão os custos, receitas e lucros, ajudando a organizar as finanças e a tomar decisões estratégicas sobre o evento. Com base em entradas personalizáveis, o simulador facilita a visualização do lucro potencial e identifica os pontos de equilíbrio financeiro para diferentes tamanhos de público.

---

#### Funcionalidades

- **Cálculo de Lucro**: Determina o lucro com base nas receitas e gastos totais.
- **Receitas e Gastos Personalizáveis**: Permite configurar valores como custos de aluguel, lineup, open bar, segurança, ingressos e outros.
- **Identificação de Pontos de Equilíbrio**: Calcula os pontos de equilíbrio para diferentes faixas de público.
- **Gráficos Interativos**: Gera gráficos que mostram o comportamento do lucro em função do número de participantes.
- **Download de Gráficos**: Permite baixar os gráficos gerados para análise externa.
- **Análises Estatísticas**: Apresenta margens de lucro e lucros médios ao longo do evento.

---

#### Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Streamlit**: Framework para desenvolvimento de aplicações web interativas.
- **NumPy**: Biblioteca para manipulação de arrays e cálculos matemáticos.
- **Matplotlib**: Biblioteca para geração de gráficos.
- **SciPy**: Utilizada para trabalhar com distribuições estatísticas.
- **BytesIO**: Para criação de botões de download.

---

#### Como Executar o Projeto

1. **Pré-requisitos**:
   - Python 3.8 ou superior instalado.
   - Instale as bibliotecas necessárias utilizando o comando:
     ```bash
     pip install streamlit numpy matplotlib scipy
     ```

2. **Clonar o Repositório**:
   Clone este repositório para o seu ambiente local:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <PASTA_DO_PROJETO>
   ```

3. **Executar a Aplicação**:
   No terminal, execute o seguinte comando:
   ```bash
   streamlit run app.py
   ```

4. **Interagir com a Interface**:
   Abra o navegador no endereço exibido no terminal (geralmente `http://localhost:8501`).

---

#### Como Usar

1. **Configurar os Gastos**:
   Insira os valores para os principais custos, como:
   - Locação do espaço.
   - Horas e custo do open bar.
   - Custos com staff, lineup e divulgação.

2. **Configurar as Receitas**:
   Defina:
   - Valor inicial dos ingressos e incremento por lote.
   - Gasto médio por pessoa no bar e margem de lucro do bar.

3. **Visualizar Resultados**:
   - Gráfico: Observe a relação entre o número de participantes e o lucro.
   - Pontos de equilíbrio: Verifique a quantidade mínima de pessoas necessária para atingir o lucro.

4. **Baixar Gráfico**:
   Clique no botão "Baixar Gráfico" para salvar o gráfico gerado em formato PNG.

---

#### Configurações Disponíveis

##### **Gastos**
- Custo de locação para até 300 ou 700 pessoas.
- Custo por segurança/brigadista.
- Custo com lineup e divulgação.
- Horas e valor por pessoa/hora de open bar.

##### **Receitas**
- Valor inicial do ingresso e incremento por lote.
- Quantidade de lotes.
- Gasto médio por pessoa no bar.
- Margem de lucro do bar.

---

#### Exemplos de Saídas

- **Gráfico de Lucro**: Representa o lucro em função do número de participantes.
- **Pontos de Equilíbrio**:
  - Público mínimo necessário para cobrir os custos e gerar lucro.
- **Margem de Lucro**:
  - Apresenta a margem de lucro para públicos específicos (300 e 700 pessoas).
- **Lucro Médio**:
  - Calcula o lucro médio ao longo de todos os cenários simulados.

---

#### Origem do Projeto

Este projeto foi idealizado para solucionar uma necessidade específica de planejamento financeiro de um evento. A criação do simulador ajudou a organizar e visualizar os dados essenciais para garantir a viabilidade do evento, fornecendo uma ferramenta prática para entender os impactos das decisões financeiras e operacionais. Ele é uma aplicação útil para quem está organizando eventos e precisa de suporte para tomar decisões estratégicas.

---

#### Melhorias Futuras

- Adicionar suporte a outras distribuições estatísticas além da Beta.
- Implementar exportação dos resultados completos em formato CSV ou PDF.
- Tornar os gráficos interativos com zoom e visualização detalhada.
- Incluir análises mais detalhadas, como sensibilidade a mudanças nos parâmetros.

---

#### Autor

- **Nome**: Henrique Dias
- **LinkedIn**: [LinkedIn.com](https://www.linkedin.com/in/henriquejoaquimnapolisdias/)

---
