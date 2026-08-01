# Skill: PrestaShop Module CI and ZIP

Data utworzenia: 2026-06-06

---

## Cel skillu

Ten skill służy do przygotowania kontroli jakości, CI i paczki ZIP modułu PrestaShop.

---

## Kiedy używać

Użyj tego skillu, gdy zadanie dotyczy:

- PHP lint,
- PHPStan,
- PHPUnit,
- GitHub Actions,
- pakowania ZIP,
- testu instalacji,
- checklisti wydania,
- wersjonowania modułu.

---

## Źródła do sprawdzenia

Przed pracą przeczytaj:

1. `.ai/CONTEXT.md`
2. `.ai/GOTCHAS.md`
3. `.ai/PRESTASHOP_MODULE_FACTORY.md`
4. `templates/checklista-instalacji-modulu.md`
5. `templates/checklista-bezpieczenstwa-modulu.md`
6. `templates/checklista-zip-modulu.md`
7. `docs/prestashop/pakowanie-zip-modulu.md`
8. `docs/prestashop/docker-test-env.md`
9. `docs/prestashop/wersjonowanie-modulow.md`

---

## Minimalne CI MVP

Na start CI powinno robić tylko bezpieczne kontrole:

```text
composer validate, jeśli composer.json istnieje
php -l dla plików PHP
podstawowe sprawdzenie struktury modułu
sprawdzenie braku zakazanych plików
```

Nie dodawaj skomplikowanego CI przed pierwszym działającym szkieletem.

---

## ZIP

Paczka ZIP musi zawierać katalog modułu jako katalog główny.

Przykład:

```text
orderpanelmvp-0.1.0.zip
  orderpanelmvp/
    orderpanelmvp.php
```

---

## Czego unikać

- nie pakować `.git/`,
- nie pakować `_external/`,
- nie pakować `node_modules/`,
- nie pakować `.env`,
- nie pakować logów,
- nie pakować danych klientów,
- nie robić release bez testu instalacji.

---

## Procedura pracy Codex

```text
Etap 1: Sprawdź strukturę modułu.
Etap 2: Sprawdź wersję modułu.
Etap 3: Sprawdź checklistę bezpieczeństwa.
Etap 4: Przygotuj minimalne CI.
Etap 5: Przygotuj procedurę ZIP.
Etap 6: Sprawdź paczkę ZIP.
Etap 7: Zapisz raport wydania.
```

---

## Wynik końcowy

Codex powinien zwrócić:

- plan CI,
- listę komend testowych,
- plan ZIP,
- listę plików zakazanych,
- decyzję, czy można wydać paczkę.
