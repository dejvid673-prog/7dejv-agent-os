# cs-frontend-engineer

- Zrodlo: `alirezarezvani/claude-skills/agents/engineering/cs-frontend-engineer.md`
- Typ: procedura agenta, nie natywny agent Codexa.
- Uzywaj gdy: frontend, React/Next/Vite/Astro, rendering, Core Web Vitals, bundle, WCAG, design system.
- Laczyc ze skillami: `senior-frontend`, `a11y-audit`, `performance-profiler`, `full-page-screenshot`, `playwright-pro`, `dependency-auditor`.

## Pytania przed praca

1. Jakie glowne urzadzenie i siec: mobile-4G, low-end Android, desktop, corporate?
2. Jaki target LCP/INP/CLS?
3. SSR, SSG, RSC czy SPA i dlaczego?
4. Jaki bundle budget per route?
5. SEO-dependent czy auth-walled?
6. Gdzie jest source of truth design systemu?
7. Jaki poziom WCAG i kto jest wlascicielem a11y?

## Workflow

Najpierw profil renderingu, potem a11y/performance audit, dopiero potem implementacja lub refactor. Przy UI zawsze sprawdz screenshotem.

## Output

Profil frontend, CWV targety, bundle budget, lista ryzyk i plan testow.

## Ryzyka

Defaultowanie do Next.js bez uzasadnienia, brak budzetu JS, brak a11y ownera.

## Adaptacja do Codexa

Uzywaj jako checklisty i procedury, nie jako natywnego subagenta.

