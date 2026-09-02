import networkx as nx
import pytest

from ottimizzazione_reti import cammino_minimo, flusso_costo_minimo, massimo_flusso
from ottimizzazione_reti.problemi import verifica_domande


def test_cammino_minimo():
    grafo = nx.DiGraph()
    grafo.add_weighted_edges_from([("s", "a", 2), ("a", "t", 3), ("s", "t", 8)])
    assert cammino_minimo(grafo, "s", "t") == (5, ["s", "a", "t"])


def test_massimo_flusso():
    grafo = nx.DiGraph()
    grafo.add_edge("s", "a", capacity=3)
    grafo.add_edge("a", "t", capacity=2)
    grafo.add_edge("s", "t", capacity=1)
    valore, _ = massimo_flusso(grafo, "s", "t")
    assert valore == 3


def test_flusso_costo_minimo_rispetta_convenzione_domande():
    grafo = nx.DiGraph()
    grafo.add_node("s", demand=-4)
    grafo.add_node("t", demand=4)
    grafo.add_edge("s", "t", capacity=4, weight=3)
    costo, flusso = flusso_costo_minimo(grafo)
    assert costo == 12
    assert flusso["s"]["t"] == 4


def test_domande_non_bilanciate():
    grafo = nx.DiGraph()
    grafo.add_node("s", demand=-3)
    grafo.add_node("t", demand=2)
    with pytest.raises(ValueError, match="non è bilanciato"):
        verifica_domande(grafo)

