
# 🛡️ Validador de CPF

Este projeto é um programa em Python que recebe CPFs do usuário, valida cada um deles conforme as regras oficiais de cálculo dos dígitos verificadores e exibe estatísticas sobre a validade dos CPFs informados.

---

## 🎯 Objetivo

* Receber múltiplos CPFs do usuário.  
* Validar os CPFs verificando seus dígitos finais.  
* Armazenar os CPFs com status de "VÁLIDO" ou "INVÁLIDO".  
* Exibir a quantidade e a porcentagem de CPFs válidos e inválidos no final.

---

## 🧠 Lógica implementada

* Verificação do tamanho e caracteres numéricos do CPF.  
* Cálculo dos dois dígitos verificadores segundo o algoritmo oficial.  
* Armazenamento dos CPFs e seus resultados em uma lista de dicionários.  
* Repetição para entrada contínua até o usuário decidir parar.  
* Apresentação de resumo estatístico ao final da execução.

---

## 🖥️ Como executar

1. Certifique-se de ter o Python instalado.  
2. Salve o código em um arquivo `.py` chamado `validarCPF.py`.  
3. Execute no terminal ou pelo seu editor de preferência:

python validarCPF.py
---

## ✨ Exemplo de uso

digite um cpf: 12345678909  
Deseja continuar? [S/N] S  
digite um cpf: 11144477735  
Deseja continuar? [S/N] N

---

[{'CPF': \[1, 2, 3, 4, 5, 6, 7, 8, 9], 'VALIDAÇÃO': 'INVÁLIDO'}, {'CPF': \[1, 1, 1, 4, 4, 4, 7, 7, 7], 'VALIDAÇÃO': 'VÁLIDO'}]  
Quantidade de CPFS VÁLIDOS: 1  
Quantidade de CPFS INVÁLIDOS: 1  
Quantidade total de CPFS testados: 2  
Porcentagem de CPFS VÁLIDOS: 50.00%  
Porcentagem de CPFS INVÁLIDOS: 50.00%

---

## 👩‍💻 Autores

* **Amanda Leite**  
* **Yure Campos Camilo**

---

### 🎓 Instituição

**Colégio Técnico Antonio Teixeira Fernandes – UNIVAP**  
**Professor responsável:** Alberson Wander


