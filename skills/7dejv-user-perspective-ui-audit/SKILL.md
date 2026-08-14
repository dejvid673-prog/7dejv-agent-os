---
name: 7dejv-user-perspective-ui-audit
description: Audit a web UI from the end-user perspective using screenshots, live browser behavior and task flows. Focus on first impression, visual hierarchy, clarity, navigation, mobile usability, readability, interaction feedback and friction. Use after a UI prototype exists and before product approval.
---

# 7DEJV User Perspective UI Audit

## Cel
Oceniac interfejs tak, jak odbiera go realny uzytkownik wykonujacy codzienna prace, a nie jak autor kodu.

## Wejscie
- wymagania i glowny cel ekranu,
- screenshoty lub dostep do dzialajacego prototypu,
- docelowe urzadzenia i viewporty,
- 2-5 najwazniejszych zadan uzytkownika,
- ograniczenia projektu.

## Procedura
1. Wykonaj test pierwszego wrazenia: czy w 5 sekund wiadomo, gdzie jestes i co jest najwazniejsze.
2. Sprawdz hierarchie informacji: priorytety, CTA, alerty, statusy i rozroznienie elementow drugorzednych.
3. Przejdz najwazniejsze task flows bez wiedzy autora o systemie.
4. Ocen nawigacje, nazewnictwo, odkrywalnosc funkcji i liczbe decyzji wymaganych od uzytkownika.
5. Sprawdz czytelnosc: typografia, kontrast, gestosc, odstepy, szerokosc kolumn, skanowalnosc tabel i kart.
6. Sprawdz mobile osobno: tap targets, dolna nawigacja, elementy stale, overlap, przewijanie i dostep do glownej akcji jedna reka.
7. Sprawdz feedback po kliknieciu: loading, success, warning, error, disabled i empty state.
8. Ocen spojnosc wzorcow UI miedzy ekranami.
9. Zapisz dowod dla kazdego istotnego problemu: ekran, viewport, element i obserwowany skutek dla uzytkownika.
10. Oddziel bledy blokujace od kosmetycznych.

## Kryteria oceny 0-10
- pierwsze wrazenie i orientacja,
- hierarchia wizualna,
- czytelnosc i skanowalnosc,
- nawigacja i odkrywalnosc,
- latwosc wykonania glownego zadania,
- mobile/responsywnosc,
- spojnosc komponentow,
- feedback i stany,
- podstawowa dostepnosc,
- ogolne odczucie profesjonalizmu i zaufania.

## Output
Zwroc:
- `decision`: PASS / WARNING / FAIL / BLOCKED,
- `score`: 0-10,
- `first_impression`,
- `top_user_pain_points` maks. 5,
- `blocking_issues`,
- `quick_wins` maks. 5,
- `what_works_well`,
- `mobile_findings`,
- `desktop_findings`,
- `evidence`,
- `recommended_next_action`.

## Zasady
1. Nie oceniaj estetyki w oderwaniu od celu operacyjnego.
2. Nie premiuj efektownych animacji kosztem szybkosci i czytelnosci.
3. Nie uznawaj zgodnosci technicznej za dowod dobrego UX.
4. Nie zgaduj zachowania niewidocznych stanow; oznacz je jako `not_tested`.
5. Kazdy problem HIGH/BLOCKER musi miec dowod i skutek dla uzytkownika.
6. Nie modyfikuj kodu podczas audytu; przekaz poprawki agentowi frontendowemu.

## Powiazane skille
- `7dejv-eval-grader` — do formalnego scoringu i porownania iteracji.
- `7dejv-agent-contract-builder` — gdy agent ma wejsc do runtime lub automatycznej orkiestracji.

## Warunki STOP
- `BLOCKED`, jesli brak screenshotu/prototypu lub nie wiadomo, jakie zadanie ma wykonac uzytkownik.
- `WARNING`, jesli da sie ocenic tylko jeden viewport.

## Akceptacja
PASS wymaga braku blockerow, sredniej >= 8.5/10 oraz braku krytycznego problemu mobile w glownym task flow.
