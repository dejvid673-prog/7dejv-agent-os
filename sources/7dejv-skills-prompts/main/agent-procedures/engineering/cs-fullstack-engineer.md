# cs-fullstack-engineer

- Zrodlo: `alirezarezvani/claude-skills/agents/engineering/cs-fullstack-engineer.md`
- Typ: procedura agenta, nie natywny agent Codexa.
- Uzywaj gdy: zadanie dotyczy stacku, nowego produktu, wiekszego modulu, wyboru frameworka, API, bazy, CI/CD albo audytu fullstack.
- Laczyc ze skillami: `zero-hallucination-coder`, `senior-fullstack`, `api-design-reviewer`, `database-schema-designer`, `slo-architect`, `ci-cd-pipeline-builder`, `performance-profiler`.

## Pytania przed praca

1. Jaki jest zespol teraz i za 12 miesiecy?
2. Jaka jest kadencja wdrozen?
3. Czy powierzchnia jest customer-facing, internal tool, czy marketing site?
4. Jaki jest roczny forecast ruchu p50/p99?
5. Czy zespol rekrutuje pod stack, czy bedzie sie szkolic?
6. Jaki jest miesieczny limit cloud/SaaS?
7. Jakie sa 3 mierzalne kryteria sukcesu?

## Workflow

Zbierz odpowiedzi, uruchom profil decyzyjny tylko gdy dane sa znane, potem rozdziel prace na API, baze, SLO, CI/CD i performance. Nie scaffoldkuj kodu przed zamknieciem pytan.

## Output

Krotki digest: rekomendowany profil, 3 kryteria sukcesu, approver chain, wybrane skille i nastepne kroki.

## Ryzyka

Przeskoczenie pytan prowadzi do zlego stacku. Skrypty scaffoldera wymagaja osobnego audytu przed uruchomieniem.

## Adaptacja do Codexa

Codex ma czytac ten plik jako procedure. Nie zakladaj natywnego `Agent({subagent_type: ...})`.

