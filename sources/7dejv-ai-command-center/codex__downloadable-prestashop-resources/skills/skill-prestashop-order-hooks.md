# Skill: PrestaShop Order Hooks

Data utworzenia: 2026-06-06
Źródło wzorca: `_external/prestashop-example-modules/demovieworderhooks`
Główne zastosowanie: `dpdshipmvp`

---

## Cel skillu

Ten skill służy do bezpiecznego projektowania paneli i akcji w szczegółach zamówienia Back Office PrestaShop.

Najważniejsze zastosowanie:

- `dpdshipmvp` — panel DPD w szczegółach zamówienia,
- status przesyłki,
- świadoma akcja administratora,
- link do etykiety,
- historia nadań,
- tracking.

---

## Kiedy używać

Użyj tego skillu, gdy zadanie dotyczy:

- `displayAdminOrderMain`,
- `displayAdminOrderSide`,
- `displayAdminOrderSideBottom`,
- `displayAdminOrderTabContent`,
- `displayAdminOrderTabLink`,
- `actionGetAdminOrderButtons`,
- panelu DPD w zamówieniu,
- przycisków administracyjnych w zamówieniu,
- widoku statusu przesyłki.

---

## Źródła do sprawdzenia

Przed pracą przeczytaj:

1. `README.md`
2. `AGENTS.md`
3. `.ai/CONTEXT.md`
4. `.ai/GOTCHAS.md`
5. `docs/prestashop/hooki-back-office.md`
6. `docs/modules/dpdshipmvp/wymagania.md`
7. `docs/modules/orderpanelmvp/granica-orderpanelmvp-dpdshipmvp.md`
8. `docs/sources/prestashop-example-modules-map.md`
9. `_external/prestashop-example-modules/demovieworderhooks/`

---

## Reguła najważniejsza

Hook w zamówieniu może wyświetlać panel i lekkie dane, ale nie powinien automatycznie wykonywać ciężkich operacji.

Nie wolno:

- tworzyć przesyłki przy samym wejściu w zamówienie,
- generować etykiety bez kliknięcia administratora,
- pobierać PDF przy każdym wyświetleniu,
- odpytywać DPD API bez potrzeby,
- logować normalnego braku przesyłki jako błędu krytycznego.

---

## Minimalny panel DPD MVP

Panel w zamówieniu powinien pokazać:

- czy DPD jest skonfigurowane,
- czy zamówienie ma już przesyłkę,
- FID, jeśli istnieje,
- status etykiety,
- przycisk `Nadaj przesyłkę`,
- przycisk `Pobierz etykietę`, jeśli etykieta istnieje,
- krótki komunikat błędu, jeśli konfiguracja jest niepełna.

---

## Świadome akcje administratora

Akcje wykonujące DPD API muszą być uruchamiane tylko po kliknięciu:

- test połączenia,
- utworzenie przesyłki,
- pobranie etykiety,
- sprawdzenie trackingu.

Każda akcja powinna mieć:

- walidację `id_order`,
- sprawdzenie uprawnień,
- obsługę błędów,
- timeout,
- bezpieczne logowanie,
- komunikat użytkownika.

---

## Bezpieczne logowanie

Logi mogą zawierać:

- typ akcji,
- id zamówienia,
- status powodzenia lub błędu,
- skrócony kod błędu,
- czas wykonania.

Logi nie mogą zawierać:

- hasła API,
- tokenów,
- pełnych danych klienta,
- pełnych odpowiedzi API z danymi wrażliwymi,
- pełnej etykiety PDF,
- sekretów konfiguracji.

---

## Procedura pracy Codex

```text
Etap 1: Przeczytaj dokumentację hooków i demovieworderhooks.
Etap 2: Wypisz, które hooki są potrzebne.
Etap 3: Zaprojektuj minimalny panel DPD.
Etap 4: Oddziel renderowanie od akcji API.
Etap 5: Zaprojektuj kontrolery akcji.
Etap 6: Sprawdź bezpieczeństwo i wydajność.
Etap 7: Przygotuj checklistę testów.
```

---

## Audyt po implementacji

Sprawdź:

- czy panel pokazuje się tylko w Back Office,
- czy hook nie wykonuje API bez kliknięcia,
- czy brak konfiguracji nie powoduje błędu krytycznego,
- czy CSS/JS nie ładuje się globalnie,
- czy przyciski mają jasne komunikaty,
- czy błędy API są obsłużone,
- czy dane wrażliwe nie trafiają do logów,
- czy panel nie przejmuje funkcji `orderpanelmvp`.

---

## Wynik końcowy

Codex powinien zwrócić:

- wybrane hooki,
- strukturę panelu,
- listę kontrolerów akcji,
- listę serwisów,
- ryzyka,
- checklistę testów,
- decyzję, czy można implementować MVP.
