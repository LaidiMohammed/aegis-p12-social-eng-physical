const SCENARIOS: Record<string, any> = {
  phishing_email: { title: "Email de phishing ciblé", description: "Vous recevez un email prétendu venant de votre DSI demandant de transférer des fonds vers un compte bancaire étranger.", choices: [
    { id: "a", text: "Transférer immédiatement les fonds demandé", risk: "très élevé", consequence: "Perte financière confirmée" },
    { id: "b", text: "Vérifier l'identité de l'expéditeur par canal secondaire", risk: "faible", consequence: "Situation évitée" },
    { id: "c", text: "Signaler l'email au équipe sécurité", risk: "faible", consequence: "Signalement effectué" },
  ], correct: "b" },
  tailgating: { title: "Accès non autorisé (tailgating)", description: "Vous voyez une personne sans badge tenter d'entrer dans zone sécurisée en suivant un employé.", choices: [
    { id: "a", text: "Laisser passer la personne sans badge", risk: "élevé", consequence: "Accès non autorisé à la zone sécurisée" },
    { id: "b", text: "Demander poliment le badge et contacter la sécurité", risk: "faible", consequence: "Accès bloqué correctement" },
    { id: "c", text: "Ignorer la personne et continuer votre chemin", risk: "moyen", consequence: "Personne déplacée" },
  ], correct: "b" },
  pretexting_phone: { title: "Appel de pretexting téléphonique", description: "Un appel prétendument venant de la banque demandant votre code PIN pour 'problème de sécurité'.", choices: [
    { id: "a", text: "Communiquer votre code PIN par téléphone", risk: "critique", consequence: "Vol d'identité, virement non autorisé" },
    { id: "b", text: "Accrocher et rappeler le numéro officiel de votre banque", risk: "faible", consequence: "Appel vérifié" },
    { id: "c", text: "Demander l'adresse email de l'appelant pour vérification", risk: "moyen", consequence: "Vérification en cours" },
  ], correct: "b" },
};
export function runScenario(scenarioId: string, userChoice?: string) {
  const s = SCENARIOS[scenarioId];
  if (!s) return { error: "Scénario inconnu" };
  const choice = userChoice || s.correct;
  const analysis = s.choices.map((c: any) => ({ id: c.id, text: c.text, risk: c.risk, consequence: c.consequence, is_correct: c.id === s.correct, selected_by_user: c.id === choice }));
  const correct = choice === s.correct;
  return {
    scenario_id: scenarioId, scenario_title: s.title, scenario_description: s.description,
    chosen_choice: choice, user_was_correct: correct, correct_choice: s.correct,
    choices_analysis: analysis,
    educational_feedback: [
      "Scénario: " + s.description,
      "Résultat: " + (correct ? "Correct - bien choisi" : "Incorrect - à risque"),
      "Niveau de risque: " + s.choices.find((c: any) => c.id === choice)?.risk,
    ],
  };
}