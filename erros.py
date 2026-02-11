"""Módulo de definições de exceções personalizadas para a calculadora."""

class OperadorInvalidoError(Exception):
    """Exceção lançada quando o operador informado não é válido."""

class DivisaoPorZeroError(Exception):
    """Exceção lançada quando ocorre divisão por zero."""

class NumeroInvalidoError(Exception):
    """Exceção lançada quando o número informado não é válido."""

class ExceptionGenericaError(Exception):
    """Exceção genérica para erros inesperados."""
