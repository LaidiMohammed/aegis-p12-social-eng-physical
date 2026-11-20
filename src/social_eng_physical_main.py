"""Module principal — P12 Scénario d'ingénierie sociale physique (AEGIS).

Fonctions :
  - run_scenario(scenario_id) -> dict : exécution d'un scénario SPE
  - analyze_choices(choices) -> dict : analyse des choix de l'utilisateur
  - main(argv) -> int : CLI

Éthique : simulation uniquement, pas d'attaque réelle, éducatif.
Tout est simulatoire en laboratoire contrôlé.
"""
from __future__ import annotations

import argparse
import json
import os
import random
from typing import Any, Dict, List, Optional

# Scénarios d'ingénierie sociale physique simulés
SCENARIOS: Dict[str, Dict[str, Any]] = {
    "phishing_email": {
        "title": "Email de phishing ciblé",
        "description": "Vous recevez un email prétendu venant de votre DSI demandant de transférer des fonds urgently vers un compte bancaire étranger.",
        "choices": [
            {"id": "a", "text": "Transférer immédiatement les fonds demandé", "risk": "très élevé", "consequence": "Perte financière confirmée, violation de politique"},
            {"id": "b", "text": "Vérifier l'identité de l'expéditeur par canal secondaire", "risk": "faible", "consequence": "None - situation évitée"},
            {"id": "c", "text": "Signaler l'email au équipe sécurité", "risk": "faible", "consequence": "None - signalement effectué"},
        ],
        "correct_choice": "b",
    },
    "tailgating": {
        "title": "Accès non autorisé (tailgating)",
        "description": "Vous voyez une personne sans badge tenter d'entrer dans zone sécurisée en suivant un employé.",
        "choices": [
            {"id": "a", "text": "Laisser passer la personne sans badge", "risk": "élevé", "consequence": "Accès non autorisé à la zone sécurisée"},
            {"id": "b", "text": "Demander poliment le badge et contacter la sécurité", "risk": "faible", "consequence": "None - accès bloqué correctement"},
            {"id": "c", "text": "Ignorer la personne et continuer votre chemin", "risk": "moyen", "consequence": "None - personne déplacée"},
        ],
        "correct_choice": "b",
    },
    "pretexting_phone": {
        "title": "Appel de pretexting téléphonique",
        "description": "Un appel prétendument venant de la banque demandant votre code PIN pour 'problème de sécurité' sur votre compte.",
        "choices": [
            {"id": "a", "text": "Communiquer votre code PIN par téléphone", "risk": "critique", "consequence": "Vol d'identité, virement non autorisé"},
            {"id": "b", "text": "Accrocher et rappeler le numéro officiel de votre banque", "risk": "faible", "consequence": "None - appel vérifié"},
            {"id": "c", "text": "Demander l'adresse email de l'appelant pour vérification", "risk": "moyen", "consequence": "None - verification en cours"},
        ],
        "correct_choice": "b",
    },
}


def run_scenario(scenario_id: str) -> Dict[str, Any]:
    """Exécute un scénario d'ingénierie sociale physique et retourne les résultats."""
    if scenario_id not in SCENARIOS:
        return {"error": f"Scénario inconnu: {scenario_id}", "chosen": None, "correct": None}

    scenario = SCENARIOS[scenario_id]
    
    # Choix aléatoire par défaut pour la démonstration (en vrai, utilisateur choisit)
    # Dans une vraie démo, l'utilisateur ferait son choix
    choice = random.choice(["a", "b", "c"])
    
    choices_analysis = []
    for choice_option in scenario["choices"]:
        is_correct = choice_option["id"] == scenario["correct_choice"]
        choice_data = {
            "id": choice_option["id"],
            "text": choice_option["text"],
            "risk": choice_option["risk"],
            "consequence": choice_option["consequence"],
            "is_correct": is_correct,
            "selected_by_user": choice == choice_option["id"],
        }
        choices_analysis.append(choice_data)
    
    # Déterminer si l'utilisateur a fait le bon choix
    chosen_option = next(c for c in scenario["choices"] if c["id"] == choice)
    user_was_correct = choice == scenario["correct_choice"]
    
    return {
        "scenario_id": scenario_id,
        "scenario_title": scenario["title"],
        "scenario_description": scenario["description"],
        "chosen_choice": choice,
        "user_was_correct": user_was_correct,
        "correct_choice": scenario["correct_choice"],
        "choices_analysis": choices_analysis,
        "educational_feedback": [
            f"Scénario: {scenario['description']}",
            f"Choix effectué: {chosen_option['text'] if 'chosen_option' in dir() else 'N/A'}",
            f"Résultat: {'Correct - bien choisi' if user_was_correct else 'Incorrect - à risque'}",
            f"Niveau de risque: {chosen_option['risk'] if 'chosen_option' in dir() else 'N/A'}",
        ],
    }


def analyze_choices(choices_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """ Analyse les choix de l'utilisateur et fournit un résumé statistique. """
    if not choices_data:
        return {"error": "Aucune donnée de choix fournie"}
    
    total = len(choices_data)
    correct = sum(1 for c in choices_data if c.get("is_correct", False))
    incorrect = total - correct
    risk_levels = [c.get("risk", "inconnu") for c in choices_data]
    
    return {
        "total_scenarios": total,
        "correct_choices": correct,
        "incorrect_choices": incorrect,
        "success_rate": round(correct / total * 100, 1) if total > 0 else 0,
        "risk_distribution": {
            "critique": risk_levels.count("critique"),
            "élevé": risk_levels.count("élevé"),
            "moyen": risk_levels.count("moyen"),
            "faible": risk_levels.count("faible"),
        },
        "recommendations": [
            "Renforcer la formation utilisateurs sur les risques électriques",
            "Mettre en place des procédures de vérification d'identité",
            "Simuler régulièrement des scénarios d'ingénierie sociale",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    import warnings
    warnings.filterwarnings("ignore")

    ap = argparse.ArgumentParser(prog="social_eng_physical",
                                 description="AEGIS - P12 - Scénario d'ingénierie sociale physique")
    ap.add_argument("--scenario", default="phishing_email", help="ID scénario à exécuter")
    ap.add_argument("--save-json", default=None, help="Écrire le résultat JSON")
    ap.add_argument("--pdf", default="outputs/rapport-p12.pdf", help="Chemin du PDF")
    ap.add_argument("--json", action="store_true", help="Sortir en JSON")
    args = ap.parse_args(argv)

    try:
        out = run_scenario(args.scenario)
    except Exception as exc:  # noqa: BLE001
        print(f"[ERREUR] {exc}")
        return 1

    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(f"[SUMMARY] P12 - Ingénierie sociale physique")
        print(f"  Scénario: {out.get('scenario_title', 'N/A')}")
        print(f"  Choix: {out.get('chosen_choice', 'N/A')}")
        print(f"  Correct: {out.get('user_was_correct', False)}")
        print(f"  Risque: {out.get('choices_analysis', [{}])[0].get('risk', 'N/A') if out.get('choices_analysis') else 'N/A'}")

    if args.save_json:
        p = Path(args.save_json)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[OK] écriture : {p}")

    if args.save_json and args.pdf:
        from src.generate_report import main as gen_main
        rc = gen_main(["--json", args.save_json, "--pdf", args.pdf])
        if rc != 0:
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())