# Skill: dpdshipmvp Audit

## Cel

Audyt modułu `dpdshipmvp`, czyli osobnego modułu DPD dla PrestaShop Back Office.

## Kiedy używać

Używać przy:

- problemach z panelem DPD w zamówieniu,
- problemach z hookami,
- problemach z API DPD,
- problemach z FID,
- problemach z etykietami,
- obawach o obciążenie sklepu,
- przebudowie starego modułu DPD.

## Dane wejściowe

- wersja PrestaShop,
- wersja PHP,
- pliki modułu,
- opis błędu,
- logi, jeśli są dostępne,
- dokumentacja DPD, jeśli jest dostępna.

## Procedura

1. Sprawdź, czy moduł działa głównie w Back Office.
2. Sprawdź hooki zamówienia.
3. Sprawdź konfigurację API.
4. Sprawdź, czy API nie jest wywoływane niepotrzebnie.
5. Sprawdź zapis FID.
6. Sprawdź etykiety.
7. Sprawdź tracking.
8. Sprawdź logowanie błędów.
9. Sprawdź ryzyka wydajnościowe.
10. Przygotuj raport i plan naprawy.

## Szczególna kontrola

Unikać powtórzenia błędów starego modułu DPD Shipping:

- globalnego działania na froncie,
- nadmiarowego logowania,
- ładowania ciężkich zasobów na każdej stronie,
- wykonywania operacji DPD bez świadomej akcji administratora.

## Wynik końcowy

- raport audytu,
- lista błędów,
- plan poprawek,
- checklista testowa,
- rekomendacja kolejnych etapów.
