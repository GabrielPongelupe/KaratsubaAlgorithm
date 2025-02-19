# Algoritmo de Karatsuba

O **algoritmo de Karatsuba** é uma técnica eficiente para multiplicação de números inteiros grandes. Ele foi introduzido por **Anatolii Karatsuba** em 1960 e reduz a complexidade da multiplicação tradicional \\( O(n^2) \\) para **O(n^{\log_2 3})** \\( \approx O(n^{1.585}) \\), tornando a operação mais rápida.

## 📌 Como Funciona?
1. **Divisão:** O número é dividido em duas partes aproximadamente iguais.
2. **Recursão:** Multiplicações menores são realizadas recursivamente.
3. **Combinação:** Os resultados são combinados para formar o produto final.

A multiplicação segue a seguinte fórmula:

\[
X \times Y = 10^{2m} \cdot AC + 10^m \cdot (AD + BC) + BD
\]


Onde:
- **A** e **B** são as partes do primeiro número.
- **C** e **D** são as partes do segundo número.
- As multiplicações são feitas da seguinte forma:
  - **AC** = A * C
  - **BD** = B * D
  - **AD + BC** = (A + B) * (C + D) - AC - BD

Esse método reduz o número de multiplicações de **4** (no método tradicional) para **3**, aumentando a eficiência para números grandes.

## 🚀 Vantagens
- **Mais rápido que o método tradicional** para números grandes.
- **Menos operações de multiplicação**, reduzindo o tempo de execução.
- **Aplicado em computação de alto desempenho** e criptografia.

Karatsuba é amplamente utilizado para cálculos eficientes em aplicações que exigem multiplicações de alta precisão e desempenho.


# 🚀 Como Executar o Projeto

Este projeto implementa o **algoritmo de Karatsuba** para multiplicação eficiente de números inteiros. O código está localizado dentro da pasta **KaratsubaAlgorithm** e contém os seguintes arquivos:

- `karatsuba.py`: Implementação do algoritmo de Karatsuba.
- `main.py`: Permite que o usuário insira dois números e veja o resultado da multiplicação.
- `karatsuba_test.py`: Contém testes unitários para validar a implementação.

  ### 1️⃣ Clonar o Repositório  
Se ainda não clonou o repositório, faça isso com o seguinte comando:  

```bash
git clone https://github.com/GabrielPongelupe/KaratsubaAlgorithm.git
cd KaratsubaAlgorithm
```

### 2️⃣ Rodar a Versão Principal (main.py)
Para executar o programa principal, que solicita ao usuário dois números e retorna o resultado da multiplicação, utilize:
```bash
python3 main.py
```

### 3️⃣ Rodar os Testes (karatsuba_test.py)
Se quiser testar a implementação, execute:

```bash
python3 -m unittest karatsuba_test.py
```

Isso validará o algoritmo utilizando diferentes casos de teste.
