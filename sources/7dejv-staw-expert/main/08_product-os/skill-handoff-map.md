# Skill handoff map — STAW EXPERT

## Cel

Mapa określa, jakie etapy pracy i zewnętrzne skille powinny być używane przy tworzeniu produktów STAW EXPERT.

Kanoniczne skille powinny mieszkać w repo `7dejv-skills-prompts`. Ten plik opisuje lokalne użycie tych skilli w repo produktowym.

## Mapa etapów

| Etap | Lokalny dokument | Skill / kompetencja | Wynik |
|---|---|---|---|
| Problem klienta | `01_badania-rynku/` | market researcher | objawy, sezon, intencja zakupu |
| Brief produktu | `02_produkty/szablon-briefu-produktu.md` | product brief builder | karta robocza produktu |
| Konkurencja | `04_konkurencja/protokol-badania-konkurencji.md` | competitor researcher | porównanie ofert |
| Ryzyko | `07_regulacje-i-bezpieczenstwo/` | claims safety checker | bezpieczne i ryzykowne deklaracje |
| Laboratorium | `03_laboratoria/` | lab verification brief builder | pytania i testy |
| Opis | `05_opisy_seo/` | product description builder | opis, SEO, FAQ |
| Etykieta | `06_grafiki-i-etykiety/` | label DTP builder | front, tył, pola techniczne |
| Grafiki | `06_grafiki-i-etykiety/mapa-grafik-g1-g30.md` | product graphics builder | lista grafik G1-G30 |
| Cena | `09_ceny-logistyka/` | pricing builder | cena minimalna i rekomendowana |
| Logistyka | `09_ceny-logistyka/` | logistics planner | gabaryt, pakowanie, wysyłka |
| Commerce | `10_wdrozenie-commerce/` | PrestaShop / Allegro publisher | karta produktu i oferta |
| Audyt | `08_product-os/product-release-gate.md` | product auditor | decyzja końcowa |

## Zasada pracy

Nie wykonywać kolejnego etapu, jeżeli poprzedni ma status `blokada`, `do konsultacji` albo `do weryfikacji krytycznej`, chyba że dokument jest wyraźnie oznaczony jako wersja robocza.
