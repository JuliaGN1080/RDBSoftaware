# Arquivo: test_escolha.py
import pytest
from unittest.mock import patch
from Testedeescolha import fazer_escolha

def test_programacao():
    with patch('builtins.input', return_value='1'):
        resultado = fazer_escolha()
        assert resultado == "Você escolheu Programação."

def test_manutencao():
    with patch('builtins.input', return_value='2'):
        resultado = fazer_escolha()
        assert resultado == "Você escolheu Manutenção."

def test_marketing():
    with patch('builtins.input', return_value='3'):
        resultado = fazer_escolha()
        assert resultado == "Você escolheu Marketing."

def test_consultoria():
    with patch('builtins.input', return_value='4'):
        resultado = fazer_escolha()
        assert resultado == "Você escolheu Consultoria de TI."

def test_opcao_invalida():
    with patch('builtins.input', return_value='5'):
        resultado = fazer_escolha()
        assert resultado == "Opção inválida. Por favor, escolha um número de 1 a 4."
