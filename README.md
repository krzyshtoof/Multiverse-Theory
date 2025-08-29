# Multiverse Theory — QMNET (#HackTheUniverse)

[![arXiv](https://img.shields.io/badge/arXiv-pending-informational)](#)
[![DOI](https://img.shields.io/badge/Zenodo-DOI_pending-blue)](#)
[![License: MIT (code)](https://img.shields.io/badge/License-MIT-success.svg)](LICENSE)
[![License: CC BY 4.0 (docs)](https://img.shields.io/badge/Docs-CC%20BY%204.0-lightgrey.svg)](DOC_LICENSE.md)

Eksperymentalna, kwantowo-topologiczna koncepcja dwóch warstw rzeczywistości:
**(i)** temporalnego wszechświata (po „odparowaniu białej dziury”) oraz **(ii)** atemporalnej sieci splątania, z której emergują czasoprzestrzeń i świadomość.

> Status: **Research in progress** (preprint; pakiet Zenodo/arXiv w przygotowaniu).

## Struktura repo
- `paper/` – preprint LaTeX (CI buduje PDF artefakt)
- `notebooks/` – eksperymenty (Jupyter)
- `simulations/` – skrypty symulacyjne
- `diagrams/` – rysunki/wizualizacje
- `docs/` – strona projektu (GitHub Pages)

## Budowa PDF (preprint)
```bash
cd paper
make   # latexmk -pdf -interaction=nonstopmode main.tex
```

PDF buduje się też automatycznie przez GitHub Actions (zob. /.github/workflows/latex.yml).

## Cytowanie
Zob. `CITATION.cff`. Po wydaniu na Zenodo tutaj trafi poprawny badge DOI.

## Licencje
Kod: MIT  
Treści (tekst/grafiki): CC BY 4.0

## Współpraca
Zgłoszenia błędów/propozycje: Issues → Bug Report / Feature Request.  
Zasady: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.

