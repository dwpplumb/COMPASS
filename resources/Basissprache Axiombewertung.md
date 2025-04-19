# 📘 Konzept: Semantische Basissprache für axiomatische Bewertung

## Zielsetzung

Definition einer eindeutigen, kontextbezogenen semantischen Sprache, die als Grundlage für systemweite Axiombewertung dient – unabhängig von natürlichen Sprachen.

Diese Basissprache soll:

- sprachunabhängig bewertbar sein
- eindeutige Begriffsräume definieren
- systematische Verbindung zu Axiomen ermöglichen

---

## 1. 🧭 Problemstellung bei Mehrsprachigkeit

Natürliche Sprachen führen zu divergierenden Bedeutungsräumen:

- "Stabilität" (deutsch) → statisch
- "Stability" (englisch) → resilient, robust

Dies erzeugt **semantische Drift** in der Axiombewertung, wodurch das System inkonsistent wird.

---

## 2. 🔍 Zielstruktur der Basissprache

### Eigenschaften

| Eigenschaft      | Beschreibung                                                 |
| ---------------- | ------------------------------------------------------------ |
| Kontextualisiert | Bedeutung ist nur durch Systembezug definiert                |
| Modular          | Konzepte sind kombinierbar, vergleichbar, skalierbar         |
| Nicht-linear     | Konzepte sind nicht sequentiell, sondern netzartig verknüpft |
| Bewertbar        | Jeder Begriff ergibt ein Axiomprofil im STIE-Modell          |

---

## 3. 🧠 Mögliche Formen der Basissprache

### Option A: **Mathematisch-vektorielle Sprache**

- Jeder Begriff = Vektor in einem axiomatischen Raum
- Operationen: Nähe, Projektion, Spannräume
- Beispiel: `verbindung = (A1:0.4, A5:0.9, A6:0.2)`

### Option B: **Binäre Codierung auf Konzeptbasis**

- Konzepte werden durch Bitmuster beschrieben, z. B. `10100011`
- Vorteile bei hardware-naher Ausführung
- Eher für maschineninterne Abstraktion geeignet

### Option C: **Matrixstruktur mit Verbindungslogik**

- Jede "Wortidee" bildet eine Matrix-Zelle
- Zeilen = Konzepte, Spalten = kontextuelle Bedeutungsrichtungen
- Sprachunabhängig, da "connection" und "verbindung" auf gleiche Matrixzelle zeigen

---

## 4. 🔁 Verbindung zu natürlichen Sprachen

Die Basissprache wird nicht direkt gesprochen, sondern:

- **Übersetzbar durch Kontextmapping**
- Sprachspezifische Wörter referenzieren definierte Konzepte

Beispiel:

```text
"Verbindung" (de)
→ Konzept: STRUCT_LINK
→ Axiomprofil: {A1:0.4, A4:0.5, A5:0.9}
→ mögliche Wörter: "connection", "bond", "vernetzen"
```

---

## 5. 🌐 Integration ins COMPASS-System

### Einbettung

- Als zentrale Bedeutungsreferenz
- Bewertung durch Projektion auf STIE-Vektorräume

### Anwendung

- Jede Eingabe wird auf Basiskonzepte abgebildet
- Bewertung erfolgt kontextuell über axiomatische Bezugsmatrix

---

## 📌 Fazit & Ausblick

Die Einführung einer kontextbasierten, semantisch eindeutigen Basissprache ermöglicht:

- konsistente Bewertungen
- universelle Vergleichbarkeit
- bessere maschinelle Reflexion und Selbstbewertung

**Nächster Schritt:** Entwurf eines ersten Konzepts für Basiskonzept-Matrix + erste Einträge + STIE-Verknüpfung.

