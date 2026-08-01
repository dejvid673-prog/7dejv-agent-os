# Skill: README Builder

## Cel skillu

Pomagać w pisaniu, poprawianiu i audytowaniu README dla repozytoriów, modułów, skilli, promptów, dokumentacji projektowej, narzędzi lokalnych i folderów roboczych.

README ma być praktyczne, krótkie, konkretne i aktualne. Ma pomagać szybko zrozumieć, co znajduje się w repo lub folderze, do czego służy i jak z tym pracować.

## Kiedy używać

Używać, gdy zadanie dotyczy:

- napisania README od zera,
- poprawy istniejącego README,
- audytu README,
- uporządkowania opisu repozytorium,
- opisania modułu PrestaShop,
- opisania skilla,
- opisania promptów,
- opisania narzędzia lokalnego,
- opisania folderu dokumentacji albo folderu roboczego.

## Typy README

- README repozytorium.
- README modułu PrestaShop.
- README skilla.
- README promptów.
- README dokumentacji projektowej.
- README narzędzia lokalnego.
- README folderu roboczego.
- README archiwum.

## Minimalny README

Minimalny README powinien zawierać:

```text
# Nazwa projektu

## Co to jest

## Cel

## Status

## Jak używać

## Następne kroki
```

Używać minimalnej wersji dla małych folderów, szybkich narzędzi i szkiców.

## Pełny README

Pełny README powinien zawierać:

1. Nazwę projektu.
2. Krótki opis: co to jest.
3. Cel projektu.
4. Status projektu: `szkic`, `w trakcie`, `MVP`, `runtime ready`, `testowany`, `gotowy`, `archiwum`.
5. Dla kogo jest projekt.
6. Co znajduje się w repo lub folderze.
7. Strukturę folderów.
8. Jak używać.
9. Jak uruchomić, jeśli dotyczy.
10. Zależności, jeśli dotyczy.
11. Zasady bezpieczeństwa.
12. Czego nie robić.
13. Aktualny etap prac.
14. Następne kroki.
15. Powiązane pliki.
16. Historię zmian albo link do CHANGELOG.
17. Krótką sekcję `Decyzje projektowe`.

## README dla modułu PrestaShop

README modułu PrestaShop powinien dodatkowo opisywać:

- wersję PrestaShop,
- cel modułu,
- zakres funkcji,
- instalację,
- konfigurację,
- hooki,
- kontrolery,
- tabele bazy danych,
- zależności,
- ograniczenia,
- checklistę bezpieczeństwa,
- czego moduł celowo nie robi.

Nie dodawać danych produkcyjnego sklepu, bazy, SMTP, hostingu ani sekretów.

## README dla repozytorium

README repozytorium powinien odpowiadać na pytania:

- po co istnieje repo,
- czy repo jest aktywne,
- jaka jest jego rola,
- co jest w środku,
- jak pracować z repo,
- czego tutaj nie trzymać,
- jakie repozytoria są powiązane,
- jaki jest następny etap.

## README dla folderu dokumentacji

README folderu dokumentacji powinien opisywać:

- typy dokumentów w folderze,
- zasady nazewnictwa,
- które dokumenty są aktualne,
- które są archiwalne,
- gdzie zapisywać raporty,
- gdzie zapisywać decyzje projektowe.

## README dla skillu

README lub opis skilla powinien zawierać:

- cel skilla,
- kiedy go używać,
- dane wejściowe,
- procedurę,
- wynik końcowy,
- checklistę jakości,
- czego unikać,
- przykładowy prompt użycia.

## README dla promptów

README dla promptów powinien zawierać:

- kategorię promptów,
- przeznaczenie,
- sposób użycia,
- wymagane dane wejściowe,
- ograniczenia,
- wersję aktualną,
- przykłady,
- informacje, których nie wolno wpisywać w prompt.

## Checklist jakości README

- Czy README ma jasną nazwę projektu?
- Czy opis mówi, co to jest?
- Czy cel jest konkretny?
- Czy status jest aktualny?
- Czy wiadomo, dla kogo jest projekt?
- Czy struktura folderów jest zrozumiała?
- Czy instrukcja użycia jest praktyczna?
- Czy uruchomienie opisano tylko wtedy, gdy dotyczy?
- Czy zależności są wymienione?
- Czy są zasady bezpieczeństwa?
- Czy jest sekcja `Czego nie robić`?
- Czy są aktualny etap i następne kroki?
- Czy są powiązane pliki?
- Czy jest historia zmian albo link do CHANGELOG?
- Czy README nie zawiera sekretów ani danych produkcyjnych?

## Czego unikać

- Długich opisów bez decyzji praktycznych.
- Nieaktualnych instrukcji.
- Marketingowego tonu zamiast konkretów.
- Kopiowania całej dokumentacji do README.
- Sekretów, loginów, haseł, danych SMTP, danych bazy i danych hostingu.
- Opisywania funkcji, których projekt nie ma.
- Mieszania statusu `gotowe` z elementami `DO DECYZJI`.

## Przykładowy prompt użycia

```text
Użyj skill-readme-builder.md.
Przygotuj README dla tego repozytorium:
- krótko,
- praktycznie,
- z jasnym statusem,
- z zasadami bezpieczeństwa,
- z następnymi krokami.
Nie dodawaj danych produkcyjnych ani sekretów.
```
