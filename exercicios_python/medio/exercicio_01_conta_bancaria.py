# ============================================================
# EXERCÍCIO 01 — NÍVEL MÉDIO
# ============================================================
# Arquivo: medio/exercicio_01_conta_bancaria.py
#
# 📚 O que você vai aprender/praticar:
#   - Funções com parâmetros e retorno
#   - Escopo de variáveis
#   - Tratamento de erros (try/except)
#   - Operadores lógicos
#
# 🎯 Título: Sistema de Conta Bancária
#
# 📝 Enunciado:
#   Crie funções para gerenciar uma conta bancária simples.
#   O programa deve ter as seguintes funções:
#   1. depositar(saldo, valor): adiciona valor ao saldo
#   2. sacar(saldo, valor): subtrai valor se houver saldo suficiente
#   3. exibir_extrato(saldo, transacoes): mostra saldo e histórico
#   4. Programa principal com menu: 1-Depositar, 2-Sacar, 3-Extrato, 0-Sair
#   5. Trate erros de valor inválido e saldo insuficiente
#
# 💡 Dica:
#   Use lista para armazenar transações. Valide com try/except ValueError!
#
# 📥 Exemplo de entrada e saída esperada:
#   Saldo inicial: R$ 0.00
#   1 - Depositar | 2 - Sacar | 3 - Extrato | 0 - Sair
#   Opção: 1
#   Valor: 1000
#   Deposito realizado! Saldo: R$ 1000.00
#   Opção: 0
#
# ============================================================
# ✏️  ESCREVA SEU CÓDIGO ABAIXO DESTA LINHA
# ============================================================

import json
import pandas as pd

transacoes = {"Id": [],
              "Data":[],
              "Valor":[]}


def depositar(saldo, valor):
    saldo += valor
    return saldo

def sacar(saldo,valor):
    saldo -= valor
    return saldo

def exibir_extrato(saldo, transacoes):
    print(f"Saldo: {saldo}\n {transacoes}")

depositar(0, 100)
saldo_conta = depositar(saldo)


