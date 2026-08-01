# karpathy-check / cs-karpathy-reviewer

- Zrodlo: `alirezarezvani/claude-skills/commands/karpathy-check.md` i `agents/engineering/cs-karpathy-reviewer.md`
- Typ: procedura review, nie natywna komenda Codexa.
- Uzywaj gdy: przed commitem, po wiekszej zmianie, po naprawie buga, przy podejrzeniu overengineeringu.
- Laczyc ze skillami: `code-reviewer`, `pr-review-expert`, `dependency-auditor`, `security-guidance`, `focused-fix`.

## Pytania przed praca

1. Czy review dotyczy staged diff czy ostatniego commita?
2. Jaki byl cel zmiany?
3. Jakie testy lub walidacje wykonano?

## Workflow

Sprawdz diff, prostote, surgical change, ukryte zalozenia i weryfikacje celu. Wskaz konkretne pliki i linie, jesli cos wymaga poprawy.

## Output

Raport: PASS, PASS WITH WARNINGS albo NEEDS WORK; konkretne poprawki; brak ogolnikow.

## Ryzyka

Nie zastepuje testow. Przy zmianach DB/API/security dodaj dedykowane skille.

## Adaptacja do Codexa

Jesli skrypty Karpathy nie sa dostepne, wykonaj reczny review wedlug 4 zasad.

