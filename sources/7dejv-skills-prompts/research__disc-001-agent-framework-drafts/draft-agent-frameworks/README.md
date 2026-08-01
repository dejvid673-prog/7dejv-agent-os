# Robocze frameworki agentowe

Ten katalog zawiera zewnętrzne projekty pobrane jako materiał roboczy do badań i porównań.

Nie są to zatwierdzeni agenci Repetytorium. Nie wolno ich automatycznie uruchamiać, instalować ani podłączać do środowiska wykonawczego.

## Statusy

- `RESEARCH_ONLY` — projekt może być używany wyłącznie jako materiał badawczy.
- `NOT_APPROVED` — projekt nie został zatwierdzony do użycia ani integracji.
- `DO_NOT_EXECUTE` — nie wolno uruchamiać kodu, skryptów, testów ani instalatorów projektu.
- `UPSTREAM_PINNED` — projekt jest przypięty do konkretnego commita w repozytorium źródłowym.

Każdy projekt jest zapisany jako submoduł Git przypięty do pełnego identyfikatora commita wskazanego w `manifest.json`.

Wykorzystanie, integracja albo adaptacja któregokolwiek projektu wymaga osobnej kontroli kodu, bezpieczeństwa i licencji oraz osobnej decyzji zatwierdzającej.
