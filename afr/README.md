Afrikaans text resources for TTS
================================

This directory contains text resources for R&D associated with the [Lwazi2 Afrikaans TTS corpus][rma:afr].

 - `lwazi2_utts.pos.tsv` is the part-of-speech (POS) tagged prompts for the corpus.
 - `lwazi2_utts.pos.eval.tsv` is a subset of the above prompts POS tagged verified by a second annotator.
 - `lwazi2_utts.prom.tsv` is the prompts annotated for perceived prominence by two listeners.

## Evaluation

To calculate agreement statistics for the prominence annotation, the following can be used:

```bash
tail -n +2 lwazi2_utts.prom.tsv | cut -f 2- | sed '/^$/d' | python scripts/print_agreement_stats.py
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

[rma:afr]: http://rma.nwu.ac.za/index.php/lwazi2-afr-tts-corpus.html
