# ETHICS — P12 — Scénario d'ingénierie sociale physique (AEGIS)

Engagements éthiques du projet — stand-alone, labo local, GPU refused, anti-cloud.

- **Cible** : [AEGIS Scénario d'ingénierie sociale physique](https://github.com/LaidiMohammed/aegis-p12-social-eng-physical)
- **Périmètre** : [AEGIS Scénario d'ingénierie sociale physique](https://aegis-p12-social-eng-physical.vercel.app) — smoke + fonctions CLI.
- **GPU refused** : implementation uniquement CPU/pure Python.
- **Données locales** : sources acceptées : labo local (localhost, Juice Shop, DVWA, etc.).
- **Smoke au prof** : cmds à exécuter — voir README/scripts/run_smoke.sh.
- **Smoke clé de validation** : voir `smoke()` dans `src/social_eng_physical_main.py` — doit retourner `{"ok": true, ...}`.
- **Site statique Vercel** : disponible pour la démo statique (smoke uniquement).

See SPEC.md (avec use cases + tableaux attendus).
