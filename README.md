# Ottimizzazione su reti

Materiale didattico ed esempi Python per il corso di **Ottimizzazione su reti**.
Il repository affianca alle dispense teoriche implementazioni riproducibili basate
su [NetworkX](https://networkx.org/).

**Giampaolo Liuzzi — Sapienza Università di Roma, DIAG**  
Contatto: [liuzzi@diag.uniroma1.it](mailto:liuzzi@diag.uniroma1.it)

## Contenuti

| Capitolo | Argomento | Materiale |
|---:|---|---|
| 1 | Introduzione all'ottimizzazione su reti | [PDF](dispense/pdf/Capitolo_01_Introduzione.pdf) |
| 2 | Grafi: definizioni e rappresentazioni | [PDF](dispense/pdf/Capitolo_02_Grafi.pdf) |
| 3 | Alberi e grafi aciclici | [PDF](dispense/pdf/Capitolo_03_Alberi_e_grafi_aciclici.pdf) |
| 4 | Reti di flusso e flusso a costo minimo | [PDF](dispense/pdf/Capitolo_04_Reti_di_flusso.pdf) |
| 5 | Simplesso su reti | [PDF](dispense/pdf/Capitolo_05_Simplesso_su_reti.pdf) |
| 6 | Massimo flusso | [PDF](dispense/pdf/Capitolo_06_Massimo_flusso.pdf) |
| 7 | Cammini minimi | [PDF](dispense/pdf/Capitolo_07_Cammini_minimi.pdf) |
| 8 | CPM | [PDF](dispense/pdf/Capitolo_08_CPM.pdf) |
| 9 | Python e NetworkX | [PDF](dispense/pdf/Capitolo_09_Python_e_NetworkX.pdf) |

I sorgenti LaTeX sono disponibili in [`dispense/sorgenti`](dispense/sorgenti).

## Convenzione per domande e offerte

Si adotta direttamente la convenzione di NetworkX. Per ogni nodo `i`,
`demand[i]` rappresenta il flusso netto entrante richiesto:

- `demand[i] > 0`: nodo di domanda (consumo);
- `demand[i] < 0`: nodo di offerta (produzione);
- `demand[i] = 0`: nodo di transito.

Il vincolo di bilancio è quindi

$$
\sum_{j:(j,i)\in A}x_{ji}-\sum_{j:(i,j)\in A}x_{ij}=d_i.
$$

Per un problema bilanciato deve valere $\sum_i d_i=0$. Non è pertanto
necessario cambiare segno ai dati quando si passa dalla formulazione teorica a
NetworkX.

## Installazione

È richiesto Python 3.10 o successivo. Dalla cartella principale:

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install -e ".[dev,notebook]"
```

## Primi esempi

```bash
python esempi/flusso_costo_minimo.py
python esempi/massimo_flusso.py
python esempi/cammino_minimo.py
python esempi/cpm.py
```

## Notebook

I notebook possono essere aperti in JupyterLab o direttamente nell'anteprima di
GitHub:

| Notebook | Contenuto |
|---|---|
| [`01_primi_passi_networkx.ipynb`](notebooks/01_primi_passi_networkx.ipynb) | Costruzione e visualizzazione di una rete |
| [`02_rappresentazione_dei_grafi.ipynb`](notebooks/02_rappresentazione_dei_grafi.ipynb) | Grafi, sottografi e sottografi indotti |
| [`03_alberi_e_grafi_aciclici.ipynb`](notebooks/03_alberi_e_grafi_aciclici.ipynb) | Alberi ricoprenti minimi e DAG |
| [`04_flusso_a_costo_minimo.ipynb`](notebooks/04_flusso_a_costo_minimo.ipynb) | Flusso a costo minimo e verifica dei bilanci |
| [`05_simplesso_su_reti.ipynb`](notebooks/05_simplesso_su_reti.ipynb) | Simplesso su reti e struttura delle soluzioni |
| [`06_massimo_flusso.ipynb`](notebooks/06_massimo_flusso.ipynb) | Massimo flusso e taglio minimo |
| [`07_cammini_minimi.ipynb`](notebooks/07_cammini_minimi.ipynb) | Dijkstra e Bellman–Ford |
| [`08_cpm.ipynb`](notebooks/08_cpm.ipynb) | Tempi, margini e attività critiche |
| [`09_esercizi_riepilogativi.ipynb`](notebooks/09_esercizi_riepilogativi.ipynb) | Esercizi guidati sui principali argomenti |

## Verifica del codice

```bash
pytest
```

## Struttura

- `dispense/`: PDF e sorgenti LaTeX;
- `src/ottimizzazione_reti/`: funzioni riutilizzabili;
- `esempi/`: programmi completi ed eseguibili;
- `notebooks/`: attività interattive;
- `dati/`: piccole istanze condivise;
- `tests/`: test automatici.

## Licenze

- Il codice Python contenuto in `src/`, `esempi/` e `tests/` è distribuito con
  licenza [MIT](LICENSE-CODE).
- Le dispense, gli esercizi, i dati didattici e i notebook sono distribuiti con
  licenza [Creative Commons Attribuzione–Non commerciale–Condividi allo stesso
  modo 4.0 Internazionale](LICENSE-MATERIALS.md) (CC BY-NC-SA 4.0).

Copyright © 2026 Giampaolo Liuzzi.
