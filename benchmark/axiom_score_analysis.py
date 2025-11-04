import json
import os

def axiom_score_diff(ax_dict1, ax_dict2, axiom_keys=None):
    """
    Berechnet die Summe der absoluten Differenzen der Axiome zwischen zwei Dicts.
    Falls axiom_keys angegeben: nur diese Keys vergleichen (sonst: Schnittmenge).
    """
    if axiom_keys is None:
        axiom_keys = set(ax_dict1.keys()).intersection(set(ax_dict2.keys()))
    diff = 0.0
    for k in axiom_keys:
        diff += abs(ax_dict1.get(k, 0.0) - ax_dict2.get(k, 0.0))
    return diff

def main():
    # Datei anpassen!
    infile = "../data/tests/wmt23_deen_benchmark_mistral.json"
    outfile = "../data/tests/wmt23_deen_benchmark_mistral_scored.json"

    with open(infile, encoding="utf-8") as fin:
        data = json.load(fin)

    scored = []
    for entry in data:
        # Extrahiere die axiom_scores für input, reference, llm_response
        input_scores = entry.get("input_axiom_scores", {})
        ref_scores   = entry.get("reference_axiom_scores", {})
        output_scores= entry.get("llm_response_axiom_scores", {})

        # Liste aller Keys für einheitlichen Vergleich
        all_keys = set(input_scores) | set(ref_scores) | set(output_scores)

        # Score-Berechnung: input <-> ref, ref <-> output, input <-> output
        score_in_ref = axiom_score_diff(input_scores, ref_scores, all_keys)
        score_ref_out= axiom_score_diff(ref_scores, output_scores, all_keys)
        score_in_out = axiom_score_diff(input_scores, output_scores, all_keys)

        # Neue Felder anhängen
        entry["score_input_reference"] = score_in_ref
        entry["score_reference_output"] = score_ref_out
        entry["score_input_output"] = score_in_out

        scored.append(entry)

    with open(outfile, "w", encoding="utf-8") as fout:
        json.dump(scored, fout, ensure_ascii=False, indent=2)

    print(f"Auswertung mit Scores geschrieben: {outfile}")

if __name__ == "__main__":
    main()
