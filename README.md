# README – Projeto da Máquina de Bebidas 

Este projeto implementa uma **máquina de vendas de bebidas** totalmente em **modo texto (console)**. Ele permite cadastrar produtos, listar itens, gerenciar estoque, receber pagamentos, 
calcular troco e manter um controle interno do caixa.

---

## 📌 **Objetivo do Projeto**

Simular o funcionamento de uma máquina de bebidas utilizando apenas **Python e lógica de programação**, sem interface gráfica. O foco é praticar:

* Estruturas de decisão
* Estruturas de repetição
* Funções
* Manipulação de dicionários e listas
* Modularização
* Controle de fluxo do programa
* Validação de dados

---

## 🧩 **Funcionalidades**

### ✔ 1. **Listar produtos disponíveis**

Exibe o código do produto, nome, preço e quantidade em estoque.

### ✔ 2. **Realizar venda**

O usuário informa:

* Código do produto
* Quantidade desejada
* Pagamento em notas/moedas

O sistema:

* Verifica estoque
* Calcula valor total
* Confere pagamento
* Gera troco usando o algoritmo guloso de denominações
* Atualiza o caixa
* Atualiza o estoque

### ✔ 3. **Cadastrar novos produtos**

Gera automaticamente um novo ID usando:

```python
novo_id = max(produtos.keys()) + 1
```

Explicação: encontra o maior ID existente e cria outro logo acima, garantindo que nunca haja duplicação.

### ✔ 4. **Atualizar estoque**

Permite adicionar mais unidades de um produto já existente.

### ✔ 5. **Exibir caixa**

Mostra todas as notas e moedas existentes na máquina.

### ✔ 6. **Salvar e carregar dados**

Produtos e caixa podem ser salvos em arquivo JSON.

---

## 💡 **Principais Funções do Sistema**

### **`quebrar_valor_em_denominacoes(valor)`**

Recebe um valor inteiro (em centavos) e retorna uma lista de quantas notas/moedas são necessárias.
Usa um algoritmo guloso com denominações:

```python
[500, 200, 100, 50, 25, 10, 5, 1]
```

### **`atualizar_caixa(lista_de_pagamento)`**

Recebe a lista de notas e moedas entregues e soma ao caixa.

### **`calcular_troco(valor_pago, valor_total)`**

Gera troco usando `quebrar_valor_em_denominacoes`.

### **`realizar_venda()`**

Fluxo completo:

* selecionar produto
* validar estoque
* receber pagamento
* verificar se é suficiente
* gerar troco
* atualizar estoque e caixa

---

## 🏗 **Estrutura básica do projeto**

```
maquina_bebidas/
│-- main.py
│-- produtos.json
│-- caixa.json
│-- readme.md
```

---

## ▶️ **Como Executar**

1. Instale o Python 3.
2. Coloque todos os arquivos na mesma pasta.
3. Execute no terminal:

```
python main.py
```

---

## 📘 **Fluxo do Programa (Resumo)**

1. Carrega produtos e caixa
2. Mostra menu principal
3. Usuário escolhe uma opção
4. Uma função específica é executada
5. Retorna ao menu até a opção “Sair”
6. Salva arquivos JSON

---

## 📜 **Exemplo de Venda (Console)**

```
Produtos:
1 – Coca 600ml – R$ 6.50 – Estoque: 10
2 – Pepsi 350ml – R$ 4.00 – Estoque: 8

Escolha o produto: 1
Quantidade: 1
Total: R$ 6.50

Digite pagamento em centavos (ex: 500 = R$5,00): 1000
Troco: 350 centavos
→ 1x 2 reais, 1x 1 real, 1x 50 centavos

Venda realizada com sucesso!
```

---





ou
✅ um **diagrama de fluxo** do programa.
