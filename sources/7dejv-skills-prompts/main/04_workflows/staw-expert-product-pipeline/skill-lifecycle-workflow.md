# Skill Lifecycle Workflow

## Cel

Dodać kontrolowany proces budowy skilli wymaganych przez STAW EXPERT Product Pipeline.

## Etapy

```text
SKILL_REQUESTED
→ DUPLICATE_CHECK
→ INTENT_CAPTURED
→ CONTRACT_DEFINED
→ SKILL_DRAFTED
→ STATIC_AUDIT
→ TEST_CASES_READY
→ EVAL_RUNNING
→ EVAL_REVIEW
→ IMPROVEMENT
→ SECURITY_REVIEW
→ READY_FOR_REVIEW
→ APPROVED
```

## Logika

1. `SKILL_REQUESTED` — utwórz kartę zapotrzebowania.
2. `DUPLICATE_CHECK` — przeszukaj repo pod kątem podobnych skilli.
3. `INTENT_CAPTURED` — określ, co skill robi i kiedy się uruchamia.
4. `CONTRACT_DEFINED` — opisz wejście, wyjście, błędy i wymagane narzędzia.
5. `SKILL_DRAFTED` — utwórz `SKILL.md` i niezbędne zasoby.
6. `STATIC_AUDIT` — sprawdź strukturę, YAML, ścieżki, zakazy i sekrety.
7. `TEST_CASES_READY` — dodaj testy pozytywne, graniczne i negatywne.
8. `EVAL_RUNNING` — uruchom test ze skillem i wersję bazową bez skilla.
9. `EVAL_REVIEW` — oceń jakość, czas, koszt i stabilność.
10. `IMPROVEMENT` — popraw instrukcje i opis uruchamiający.
11. `SECURITY_REVIEW` — sprawdź minimalne uprawnienia i odporność na niebezpieczne wejście.
12. `READY_FOR_REVIEW` — przygotuj PR i raport.
13. `APPROVED` — człowiek zatwierdza publikację skilla.

## Warunki STOP

- duplikat bez uzasadnienia,
- brak jednoznacznego kontraktu,
- brak testów dla wyniku możliwego do weryfikacji,
- dostęp do sekretów nieuzasadniony zadaniem,
- niebezpieczne skrypty lub nieznana licencja,
- skill nie poprawia wyniku względem wersji bazowej,
- zbyt szeroki zakres odpowiedzialności.

## Wymagane artefakty

```text
skill-name/
├── SKILL.md
├── references/        opcjonalnie
├── scripts/           opcjonalnie
├── assets/            opcjonalnie
├── evals/evals.json
└── AUDIT.md
```
