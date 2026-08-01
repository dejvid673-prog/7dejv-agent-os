# Skill: PrestaShop Symfony Config Form

Data utworzenia: 2026-06-06
Źródło wzorca: `_external/prestashop-example-modules/demosymfonyformsimple` oraz `_external/prestashop-example-modules/demosymfonyform`
Główne zastosowanie: konfiguracja modułów, szczególnie `dpdshipmvp`

---

## Cel skillu

Ten skill służy do projektowania i audytu formularzy konfiguracji modułów PrestaShop opartych o Symfony Form.

Najważniejsze zastosowania:

- konfiguracja danych DPD,
- formularz testu połączenia,
- ustawienia etykiet,
- ustawienia trybu sandbox/production,
- konfiguracja zachowania modułu.

---

## Kiedy używać

Użyj tego skillu, gdy zadanie dotyczy:

- strony konfiguracji modułu,
- Symfony Form,
- `FormHandler`,
- `FormDataProviderInterface`,
- `DataConfigurationInterface`,
- zapisu ustawień modułu,
- pól sekretów,
- walidacji konfiguracji.

---

## Źródła do sprawdzenia

Przed pracą przeczytaj:

1. `README.md`
2. `AGENTS.md`
3. `.ai/CONTEXT.md`
4. `.ai/GOTCHAS.md`
5. `docs/sources/prestashop-example-modules-map.md`
6. `_external/prestashop-example-modules/demosymfonyformsimple/`
7. opcjonalnie `_external/prestashop-example-modules/demosymfonyform/`

---

## Minimalna konfiguracja DPD

Dla `dpdshipmvp` konfiguracja MVP może zawierać:

```text
DPD login
DPD password / token
FID / payer number, jeśli wymagane
tryb sandbox / production
format etykiety
włączone / wyłączone logowanie diagnostyczne
```

Dane wrażliwe muszą być ukryte w formularzu i nie mogą trafić do repo.

---

## Zasady bezpieczeństwa

- Nie zapisuj prawdziwych sekretów w repo.
- Nie pokazuj hasła po zapisaniu formularza.
- Nie wypisuj sekretów w błędach.
- Nie loguj pełnej konfiguracji.
- Waliduj wymagane pola.
- Rozdziel sandbox i production.
- Test połączenia powinien być świadomą akcją administratora.

---

## Procedura pracy Codex

```text
Etap 1: Przeczytaj przykład formularza Symfony.
Etap 2: Wypisz potrzebne pola konfiguracji.
Etap 3: Określ, które pola są sekretami.
Etap 4: Zaprojektuj strukturę FormType / DataProvider / Configuration.
Etap 5: Zaprojektuj walidację.
Etap 6: Zaprojektuj test połączenia jako osobną akcję.
Etap 7: Wykonaj audyt bezpieczeństwa.
```

---

## Czego unikać

- nie mieszać formularza konfiguracji z tworzeniem przesyłki,
- nie odpalać testu połączenia przy każdym otwarciu strony,
- nie zapisywać haseł w plikach,
- nie tworzyć rozbudowanych opcji przed MVP,
- nie kopiować nazw demo z przykładów,
- nie przechowywać sekretów w logach.

---

## Wynik końcowy

Codex powinien zwrócić:

- listę pól konfiguracji,
- klasy i pliki do utworzenia,
- zasady walidacji,
- sposób zapisu ustawień,
- sposób ukrywania sekretów,
- plan testu połączenia,
- checklistę bezpieczeństwa.
