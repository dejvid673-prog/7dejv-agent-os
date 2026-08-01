# PrestaShop performance audit workflow

## Kiedy uzywac

Dla wolnego sklepu, wolnych kategorii, koszyka, checkoutu, panelu lub importow.

## Wejscie

Wersja PrestaShop, hosting, moduly, logi, objawy, URL-e, wyniki pomiarow.

## Skille

`performance-profiler`, `senior-backend`, `sql-database-assistant`, `dependency-auditor`, `code-reviewer`.

## Procedury agentow

`cs-backend-engineer`, `cs-frontend-engineer`, `karpathy-check`.

## Kroki

1. Ustal metryke: TTFB, LCP, query time, memory, CPU.
2. Sprawdz moduly, cache, szablon, zapytania SQL.
3. Zmierz baseline.
4. Wskaz top 3 bottlenecks.
5. Zaproponuj minimalne zmiany i test po zmianie.

## Weryfikacja

Porownaj before/after ta sama metoda i na tych samych URL-ach.

## Ryzyka

Optymalizacja bez pomiaru, cache maskujacy problem, zmiany w module bez testu.

## Output

Raport performance, bottlenecki, plan napraw i wyniki pomiarow.

