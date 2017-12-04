Setswana text resources for TTS
===============================

This directory contains text resources for R&D associated with the [Lwazi2 Setswana TTS corpus][rma:tsn].

 - `lwazi2_utts.tsn.scm` is the Setswana portion of the corpus annotated for vowel height.
 - `lwazi2_utts.tsn.eval.scm` is a subset of the above prompts with annotations for vowel height verified by a second annotator.
 - `lwazi2_utts.tsn.contfunc.punct.tsv` is the Setswana portion of the corpus annotated for _content_ and _function_ word distinctions (with punctuation tokens).
 - `lwazi2_utts.tsn.contfunc.nopunct.tsv` is the Setswana portion of the corpus annotated for _content_ and _function_ word distinctions (lowercased and without punctuation tokens).
 - `lwazi2_utts.tsn.contfunc.eval.01-50.punct.tsv` is a subset of the above prompts with annotations verified by a second annotator.
 - `lwazi2_utts.tsn.prom.tsv` are the prompts from the Setswana portion of the corpus annotated for perceived prominence by two listeners.

## Evaluation

To calculate agreement statistics for the prominence annotation, the following can be used:

```bash
tail -n +2 lwazi2_utts.tsn.prom.tsv | cut -f 2- | sed '/^$/d' | python scripts/print_agreement_stats.py
```

## References

 1. D.R. van Niekerk, __"Final technical report: Rapid development of increasingly natural sounding speech synthesis for South African languages,"__ North-West University, Vanderbijlpark, South Africa, Tech. Rep. 2017.
```bibtex
@techreport{vniekerk2017ntts,
	title = {{Final technical report: Rapid development of increasingly natural sounding speech synthesis for South African languages}},
	author = {van Niekerk, D. R.},
	institution = {{North-West University}},
	address = {Vanderbijlpark, South Africa},
	year = {2017},
}
```

[rma:tsn]: http://rma.nwu.ac.za/index.php/lwazi2-tn-tts-corpus.html

