# AEGIS — P12 — Scénario d'ingénierie sociale physique

[![Vercel](https://img.shields.io/badge/Vercel-aegis-p12--blue?logo=vercel)](https://aegis-p12-social-eng-physical.vercel.app)
[![Tests](https://img.shields.io/badge/Tests-passing-brightgreen)]

Scénario d'ingénierie sociale physique — PFE P13 style AEGIS (Master 1 Sécurité informatique).

## Infos rapides

| Élément | Valeur |
|---|---|
| **GitHub** | https://github.com/LaidiMohammed/aegis-p12-social-eng-physical |
| **Vercel** | https://aegis-p12-social-eng-physical.vercel.app |
| **Stacks** | python, random, reportlab |
| **Type** | sim |
| **Ethique** | Labo local, anti-GPU, anti-cloud, stand-alone |

## Install

```bash
pip install -r requirements.txt
make install  # (venv)
```

## Smoke & tests (démo à la prof)

```bash
make smoke   # ou: scripts/run_smoke.sh
make test
```

## Fonctions à exécuter à la démo

Voir [`docs/ETHICS.md`](docs/ETHICS.md), [`docs/SPEC.md`](docs/SPEC.md).
