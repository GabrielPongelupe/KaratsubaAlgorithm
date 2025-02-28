# Algoritmo de Karatsuba

Trabalho realizado para a disciplina de Fundamentos de Projeto e Análise de Algoritmos do curso de Engenharia de Software da PUC Minas.

O **algoritmo de Karatsuba** é uma técnica eficiente para multiplicação de números inteiros grandes. Ele foi introduzido por **Anatolii Karatsuba** em 1960 e reduz a complexidade da multiplicação tradicional \\( O(n^2) \\) para **O(n^{\log_2 3})**, aproximadamente O(n^{1.585}), tornando a operação mais rápida.

## 📌 Como Funciona?
1. **Divisão:** O número é dividido em duas partes aproximadamente iguais.
2. **Recursão:** Multiplicações menores são realizadas recursivamente.
3. **Combinação:** Os resultados são combinados para formar o produto final.

A multiplicação segue a seguinte fórmula:

X × Y=(10^2m × AC) + (10^m × (AD + BC)) + BD


Onde:
- **A** e **B** são as partes do primeiro número.
- **C** e **D** são as partes do segundo número.
- As multiplicações são feitas da seguinte forma:
  - **AC** = A * C
  - **BD** = B * D
  - **AD + BC** = (A + B) * (C + D) - AC - BD

Esse método reduz o número de multiplicações de **4** (no método tradicional) para **3**, aumentando a eficiência para números grandes.

---


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

---

# 📊 Relatório Técnico
 
## 🔍 Complexidade Ciclomática

A **complexidade ciclomática** é uma métrica usada em análise de algoritmos para medir a complexidade de um programa, especificamente o número de caminhos independentes que um programa pode seguir.

## 📌 Como Calcular a Complexidade Ciclomática?
A complexidade ciclomática pode ser determinada através da seguinte fórmula:
```
M = E - N + 2P
```

M: Complexidade Ciclomática

E: Número de arestas (conexões entre blocos de código no grafo de fluxo de controle)

N: Número de nós (blocos de código distintos no grafo)

P: Componentes conectados (geralmente 1 para programas isolados, podendo ser maior em sistemas modulares)

Agora que compreendemos a métrica, vamos aplicá-la ao algoritmo de multiplicação de Karatsuba, que é uma técnica eficiente para multiplicação de números grandes, dividindo os operandos em partes menores.

Para calcular sua complexidade ciclomática, representamos o código como um grafo de fluxo de controle, onde:

* Cada bloco de decisão (if, else, recursões) se torna um nó.

* Cada transição entre blocos representa uma aresta.

Nós Encontrados (N):
1. Início do método
2. Checagem da condição inicial (if)
3. Retorno imediato do produto entre ```numberOne x numberTwo```)
4. Determinação do tamanho de maxLenght
5. Cálculo do valor de ```half```
6. Cálculo das partes do ```numberOne``` (parte alta e parte baixa)
7. Cálculo das partes de ```numberTwo``` (parte alta e parte baixa)
8. Chamada recursiva de multiplicação das partes altas ```karatsuba(a, c)```
9. Atribuição de ac ```ac = karatsuba(a, c)```
10. Chamada recursiva de multiplicação das partes baixas
11. Atribuição de bd
12. Chamada recursiva de multiplicação ```karatsuba(a + b, c + d) - ac - bd```
13. Cálculo de ad_plus_bc ```ad_plus_bc = karatsuba(a + b, c + d) - ac - bd```
14. Retorno do resultado final da multiplicação

Arestas Encontrados (E):
1. Início do método **para** Checagem da condição inicial (if)
2. Checagem da condição inicial (if) **para** Retorno imediato do produto entre ```numberOne x numberTwo``` (se a condição for verdadeira)
3. Checagem da condição inicial (if) **para** Determinação do tamanho de ```maxLenght``` (se a condição for falsa)
4. Determinação do tamanho de ```maxLenght``` **para** Cálculo do valor de ```half```
5. Cálculo do valor de ```half``` **para** Cálculo das partes do ```numberOne``` (parte alta e parte baixa)
6. Cálculo das partes do ```numberOne``` (parte alta e parte baixa) **para** Cálculo das partes de ```numberTwo``` (parte alta e parte baixa)
7. Cálculo das partes de ```numberTwo``` (parte alta e parte baixa) **para** Chamada recursiva de multiplicação das partes altas ```karatsuba(a, c)```
8. Chamada recursiva de multiplicação das partes altas ```karatsuba(a, c)``` **para** Início do método
9. Chamada recursiva de multiplicação das partes altas ```karatsuba(a, c)``` **para** Atribuição de ```ac (ac = karatsuba(a, c))```
10. Atribuição de ac ```(ac = karatsuba(a, c))``` **para** Chamada recursiva para multiplicação das partes baixas
11. Chamada recursiva de multiplicação das partes baixas **para** Início do método
12. Chamada recursiva de multiplicação das partes baixas **para** Atribuição de ```bd```
13. Atribuição de ```bd``` **para** Chamada recursiva de multiplicação ```karatsuba(a + b, c + d) - ac - bd```
14. Chamada recursiva de multiplicação ```karatsuba(a + b, c + d) - ac - bd``` **para** Início do método
15. Chamada recursiva de multiplicação ```karatsuba(a + b, c + d) - ac - bd``` **para** Cálculo de ```ad_plus_bc (ad_plus_bc = karatsuba(a + b, c + d) - ac - bd)```
16. Cálculo de ```ad_plus_bc (ad_plus_bc = karatsuba(a + b, c + d) - ac - bd)``` **para** Retorno do resultado final da multiplicação

**GRAFO DE FLUXO:**

Resultado:

* E (Número de arestas) = 16
* N (Número de nós) = 14
* P (Número de componentes conectados 1) = 1

Agora que temos os nós (N) e as arestas (E) identificadas, podemos calcular a complexidade ciclomática da função Karatsuba usando a fórmula:
### ```M = E − N + 2P```
### ```M = 16 − 14 + 2(1)``` 
### ```M = 4``` 

**Conclusão**
A complexidade ciclomática da função Karatsuba é 4, indicando que há 4 caminhos independentes no fluxo de execução. Isso significa que, para testar completamente a função, seriam necessários 4 casos de teste distintos, cobrindo todos os possíveis fluxos do algoritmo.

## 🔍 Complexidade Assintótica

**Complexidade temporal:** A complexidade temporal do algoritmo Karatsuba melhora significativamente em comparação com a multiplicação tradicional de números grandes. Enquanto a multiplicação convencional tem complexidade O(n²), o Karatsuba reduz esse tempo para O(n^1,585), o que representa uma melhoria considerável à medida que o tamanho dos números cresce. 
No **melhor caso**, quando os números são pequenos o suficiente para a multiplicação direta, o algoritmo tem uma complexidade O(1). Já no **pior caso**, que ocorre quando os números são grandes e o algoritmo precisa realizar várias recursões, a complexidade atinge seu valor de  O(n^[log(3;2)]) ≈ O(n^1,585), que é muito mais eficiente do que os métodos tradicionais. Assim, o Karatsuba é especialmente vantajoso para a multiplicação de números de grande escala, reduzindo o número de operações necessárias.

**Complexidade de Espaço:** A complexidade de espaço do algoritmo Karatsuba é **O(log n)** , pois, a cada chamada recursiva, o algoritmo realiza três novas chamadas e divide os números pela metade, reduzindo assim o tamanho do problema em cada nível de recursão. Como a profundidade da recursão é proporcional ao logaritmo do tamanho do número, o número de chamadas recursivas simultâneas é limitado a **O(log n)**  o que implica que o espaço necessário para armazenar as chamadas na pilha de execução é também **O(log n)**. Dessa forma, embora o Karatsuba exija mais espaço do que métodos iterativos simples, ele é ainda mais eficiente em termos de uso de memória em comparação com algoritmos que exigem espaço linear ou quadrático.

---
