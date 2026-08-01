# Skill: PrestaShop Module DB Install

Data utworzenia: 2026-06-06
Główne zastosowanie: tabele modułów `orderpanelmvp` i `dpdshipmvp`

---

## Cel skillu

Ten skill służy do projektowania, tworzenia i audytu tabel bazodanowych modułu PrestaShop.

Ma pilnować, żeby moduły miały:

- proste tabele,
- sensowne indeksy,
- bezpieczny `install()` i `uninstall()`,
- brak nadmiarowych zapisów,
- brak danych wrażliwych w logach,
- możliwość dalszej rozbudowy bez przebudowy całego modułu.

---

## Kiedy używać

Użyj tego skillu, gdy zadanie dotyczy:

- tworzenia tabel modułu,
- statusów pakowania,
- historii akcji,
- zapisu FID,
- zapisu etykiet,
- zapisu tracking number,
- logów diagnostycznych,
- instalacji/deinstalacji modułu,
- migracji struktury danych.

---

## Źródła do sprawdzenia

Przed pracą przeczytaj:

1. `README.md`
2. `AGENTS.md`
3. `.ai/CONTEXT.md`
4. `.ai/GOTCHAS.md`
5. `.ai/PRESTASHOP_MODULE_FACTORY.md`
6. `docs/modules/orderpanelmvp/granica-orderpanelmvp-dpdshipmvp.md`
7. `docs/sources/prestashop-example-modules-map.md`
8. opcjonalnie `_external/prestashop-example-modules/demodoctrine/`

---

## Reguła główna

Tabele modułu mają przechowywać tylko dane potrzebne do działania modułu.

Nie wolno tworzyć lokalnej kopii całego zamówienia, klienta ani produktów, jeśli PrestaShop już ma te dane.

---

## Proponowane tabele dla `orderpanelmvp`

MVP może potrzebować jednej lekkiej tabeli:

```text
PREFIX_orderpanelmvp_pack_status
```

Przykładowe pola:

```text
id_pack_status INT AUTO_INCREMENT PRIMARY KEY
id_order INT NOT NULL
pack_status VARCHAR(32) NOT NULL
problem_flag TINYINT(1) NOT NULL DEFAULT 0
problem_note TEXT NULL
updated_by INT NULL
date_add DATETIME NOT NULL
date_upd DATETIME NOT NULL
```

Rekomendowane indeksy:

```text
INDEX(id_order)
INDEX(pack_status)
INDEX(problem_flag)
INDEX(date_upd)
```

---

## Proponowane tabele dla `dpdshipmvp`

### 1. Przesyłki DPD

```text
PREFIX_dpdshipmvp_shipment
```

Przykładowe pola:

```text
id_dpd_shipment INT AUTO_INCREMENT PRIMARY KEY
id_order INT NOT NULL
fid VARCHAR(64) NULL
shipment_number VARCHAR(64) NULL
label_path VARCHAR(255) NULL
tracking_number VARCHAR(64) NULL
shipment_status VARCHAR(64) NULL
last_error_code VARCHAR(64) NULL
last_error_message TEXT NULL
created_by INT NULL
created_at DATETIME NOT NULL
updated_at DATETIME NOT NULL
```

Rekomendowane indeksy:

```text
INDEX(id_order)
INDEX(fid)
INDEX(shipment_number)
INDEX(tracking_number)
INDEX(shipment_status)
INDEX(updated_at)
```

### 2. Logi diagnostyczne DPD

```text
PREFIX_dpdshipmvp_log
```

Przykładowe pola:

```text
id_dpd_log INT AUTO_INCREMENT PRIMARY KEY
id_order INT NULL
action VARCHAR(64) NOT NULL
level VARCHAR(16) NOT NULL
message TEXT NOT NULL
error_code VARCHAR(64) NULL
duration_ms INT NULL
date_add DATETIME NOT NULL
```

Nie zapisywać w tej tabeli sekretów, haseł, tokenów, pełnych danych klienta ani pełnych odpowiedzi API z danymi wrażliwymi.

---

## Install

Przy `install()` sprawdź:

- czy tabele mają prefiks PrestaShop,
- czy kolumny mają typy zgodne z MySQL/MariaDB,
- czy są indeksy,
- czy moduł rejestruje tylko potrzebne hooki,
- czy konfiguracja domyślna nie zawiera sekretów,
- czy instalacja może zostać uruchomiona ponownie bez chaosu.

---

## Uninstall

Przed `uninstall()` ustal decyzję biznesową:

```text
Czy usuwać dane modułu przy deinstalacji?
TAK / NIE / tylko po zaznaczeniu opcji
```

Bezpieczny wariant MVP:

- usuwać konfigurację techniczną,
- nie usuwać danych przesyłek bez świadomej decyzji,
- nie usuwać danych, jeśli mogą być potrzebne do reklamacji lub historii zamówienia.

---

## Reguły bezpieczeństwa

Nie przechowuj:

- haseł API w tabelach logów,
- tokenów w logach,
- pełnych danych klienta,
- pełnych adresów, jeśli nie są konieczne,
- pełnych odpowiedzi API,
- plików PDF jako blob w bazie.

Preferuj:

- ID zamówienia jako odniesienie,
- skrócone kody błędów,
- statusy techniczne,
- ścieżki do plików etykiet zamiast blobów,
- ograniczone logi.

---

## Reguły wydajności

- Dodaj indeksy do pól używanych w filtrach.
- Nie rób zapytań w pętli dla każdego zamówienia.
- Nie zapisuj logu dla każdej normalnej sytuacji.
- Ogranicz historię logów albo dodaj mechanizm czyszczenia.
- Nie buduj wielkiej tabeli analitycznej w MVP.

---

## Procedura pracy Codex

```text
Etap 1: Określ, czy moduł naprawdę potrzebuje tabeli.
Etap 2: Zaprojektuj minimalny schemat.
Etap 3: Określ indeksy.
Etap 4: Określ dane wrażliwe i czego nie zapisywać.
Etap 5: Zaprojektuj install/uninstall.
Etap 6: Przygotuj test instalacji i deinstalacji.
Etap 7: Wykonaj audyt bezpieczeństwa i wydajności.
```

---

## Wynik końcowy

Codex powinien zwrócić:

- proponowane tabele,
- listę kolumn,
- indeksy,
- decyzję uninstall,
- ryzyka,
- testy,
- informację, czy tabela jest konieczna już w MVP.
