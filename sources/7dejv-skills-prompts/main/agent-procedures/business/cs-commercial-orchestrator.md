# cs-commercial-orchestrator

- Zrodlo: `alirezarezvani/claude-skills/commercial/agents/cs-commercial-orchestrator.md`
- Typ: procedura agenta, nie natywny agent Codexa.
- Uzywaj gdy: pricing, marza, deal review, rabaty, partnerzy, channel economics, polityka handlowa, RFP, forecast.
- Laczyc ze skillami: `pricing-strategist`, `deal-desk`, `partnerships-architect`, `channel-economics`, `commercial-policy`, `rfp-responder`, `commercial-forecaster`.

## Pytania przed praca

1. Jaka jest marza przy pelnym rabacie?
2. Czy ten deal tworzy precedens?
3. Kto zatwierdza decyzje handlowa?

## Workflow

Najpierw rozpoznaj lane: pricing, deal, partner, channel, policy, RFP, forecast. Dla pricingu dawaj model i range, nie jedna liczbe. Dla rabatow wskaz approvera.

## Output

Rekomendacja ekonomiczna, zalozenia, ryzyka precedensu, approver, nastepna akcja.

## Ryzyka

Auto-approval rabatow i prognozy bez jawnych konwersji.

## Adaptacja do Codexa

Uzywaj recznie jako procedury decyzyjnej.

