# Skill Benchmark Loop

## Cel

Porównać działanie bez skilla i ze skillem, a następnie poprawiać skill do osiągnięcia mierzalnej jakości bez pogorszenia bezpieczeństwa.

## Przebieg

```text
READ_SKILL_CONTRACT
→ GENERATE_OR_VALIDATE_EVALS
→ RUN_BASELINE
→ RUN_WITH_SKILL
→ CAPTURE_TIMING_AND_COST
→ GRADE_ASSERTIONS
→ COMPARE_VARIANTS
→ DETECT_REGRESSIONS
→ IMPROVE_SKILL
→ REPEAT_OR_REVIEW
→ PASS / HOLD / BLOCKED
```

## Artefakty

```text
<skill>/evals/evals.json
artifacts/evals/<skill>/<run-id>/baseline/
artifacts/evals/<skill>/<run-id>/with-skill/
artifacts/evals/<skill>/<run-id>/grading.json
artifacts/evals/<skill>/<run-id>/benchmark.json
artifacts/evals/<skill>/<run-id>/benchmark.md
```

## Reguły

### `PASS`
- wszystkie testy bezpieczeństwa zaliczone,
- brak istotnej regresji jakościowej,
- wynik ze skillem jest lepszy od baseline albo dostarcza jasno mierzalną wartość,
- wymagane testy mają wyniki i dowody,
- człowiek zatwierdził przypadki wymagające oceny jakościowej.

### `HOLD`
- brakuje baseline, wyników lub timingów,
- testy są zbyt mało reprezentatywne,
- wynik jest niestabilny,
- przewaga nad baseline jest niejednoznaczna.

### `BLOCKED`
- niezaliczony test bezpieczeństwa,
- skill przekracza uprawnienia,
- wynik ze skillem jest istotnie gorszy,
- występuje niekontrolowana lub destrukcyjna akcja.

## Minimalny zestaw

Każdy skill powinien mieć minimum 8 przypadków: 3 pozytywne, 2 graniczne, 2 negatywne i 1 bezpieczeństwa.
