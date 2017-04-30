Setswana text resources for TTS
===============================

This directory contains text resources intended for R&D of Setswana TTS systems.  Files prefixed with `lwazi2_` originate from the [Lwazi2 Setswana TTS corpus][rma:tsn].

 - `lwazi2_utts.tsn.scm` is the Setswana portion of the corpus annotated for vowel height during the NTTS project (see top level `README.md`).
 - `lwazi2_utts.tsn.contfunc.punct.tsv` is the Setswana portion of the corpus annotated for _content_ and _function_ word distinctions (with punctuation tokens).
 - `lwazi2_utts.tsn.contfunc.nopunct.tsv` is the Setswana portion of the corpus annotated for _content_ and _function_ word distinctions (lowercased and without punctuation tokens).
 - `lwazi2_utts.tsn.prom.tsv` are the prompts from the Setswana portion of the corpus annotated for perceived prominence by two listeners.
 - `tsn_lwazi2_htsmelp16k_nopause_baseline_20170430.voice.pickle` is a "baseline" Lwazi2 TTS system implementation.
 - `tsn_lwazi2_htsmelp16k_nopause_newproto_20170430.voice.pickle` is a prototype Lwazi2 TTS system using additional vowel distinctions and _content/function_ distinction.

[rma:tsn]: http://rma.nwu.ac.za/index.php/lwazi2-tn-tts-corpus.html
