IsiZulu text resources for TTS
===============================

This directory contains text resources for R&D associated with the [Lwazi2 IsiZulu TTS corpus][rma:zul].

 - `lwazi2_utts.zul.contfunc.manual.scm` is the isiZulu portion of prompts in the corpus with simplified manual morphological (content/function) annotation.
 - `lwazi2_utts.zul.contfunc.eval.scm` is a subset of the above prompts verified by a second annotator.
 - `lwazi2_utts.zul.contfunc.auto.scm` is the isiZulu portion of prompts in the corpus with simplified automatic morphological (content/function) annotation.
 - `lwazi2_utts.zul.prom.tsv` is the isiZulu portion of the corpus annotated for perceived prominence by two listeners.

## Evaluation

To calculate agreement statistics for the prominence annotation, the following can be used:

```bash
tail -n +2 lwazi2_utts.zul.prom.tsv | cut -f 2- | sed '/^$/d' | python scripts/print_agreement_stats.py
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

[rma:zul]: http://rma.nwu.ac.za/index.php/lwazi2-zu-tts-corpus.html
