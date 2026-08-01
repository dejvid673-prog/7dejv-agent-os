# PrestaShop payment integration workflow

## Kiedy uzywac

Dla integracji platnosci, statusow zamowien, callbackow, webhookow i faktur.

## Wejscie

Dokumentacja operatora, wersja PrestaShop, flow platnosci, statusy, logi, sandbox.

## Skille

`zero-hallucination-coder`, `senior-backend`, `api-design-reviewer`, `security-guidance`, `code-reviewer`.

## Procedury agentow

`cs-backend-engineer`, `cs-engineer-grill`, `karpathy-check`.

## Kroki

1. Przeczytaj dokumentacje API operatora.
2. Sprawdz realne statusy i hooki w projekcie.
3. Zaplanuj flow: start, return, callback, failure, refund.
4. Dodaj logowanie i walidacje podpisu.
5. Testuj sandbox i scenariusze bledow.

## Weryfikacja

Platnosc sukces, blad, anulowanie, retry callbacku, brak podwojnego statusu.

## Ryzyka

Brak weryfikacji podpisu, race condition, status zamowienia zgadniety z pamieci.

## Output

Plan integracji, kod lub checklist, test matrix, ryzyka security.

