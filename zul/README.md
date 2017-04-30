IsiZulu text resources for TTS
===============================

This directory contains text resources intended for R&D of isiZulu TTS systems. Files prefixed with `lwazi2_` originate from the [Lwazi2 IsiZulu TTS corpus][rma:zul]. The prototypes require software from [here](https://github.com/NWU-MuST/ttslab2).

 - `lwazi2_utts.zul.automorph.scm` is the isiZulu portion of prompts with simplified automatic morphological decomposition during the NTTS project (see top level `README.md`).
 - `lwazi2_utts.zul.manualmorph.scm` is the isiZulu portion of prompts with simplified manual morphological decomposition during the NTTS project (see top level `README.md`).
 - `lwazi2_utts.zul.prom.tsv` are the prompts from the isiZulu portion of the corpus annotated for perceived prominence by two listeners.
 - `zul_lwazi2_htsmelp16k_nopause_baseline_20170430.voice.pickle` is a "baseline" Lwazi2 TTS system implementation.
 - `zul_lwazi2_htsmelp16k_nopause_newproto_20170430.voice.pickle` is a prototype Lwazi2 TTS system using additional morphological processing.

[rma:zul]: http://rma.nwu.ac.za/index.php/lwazi2-zu-tts-corpus.html
