# hedg-summer-school

2026 HEDG Summer School: AI/ML for vision and language

## Slides

- [Lecture 1: Off-the-shelf models](https://raw.githack.com/TorbenSDJohansen/hedg-summer-school/refs/heads/cv2026/01_Off_the_shelf_models/Slides.html)
- [Lecture 2: From tokens to transcription](https://raw.githack.com/TorbenSDJohansen/hedg-summer-school/refs/heads/cv2026/02_From_Tokens_to_Transcription/Slides.html)

(Links point at the `cv2026` branch while this content is in progress. Update the branch in the URL - or move these to `main` - once merged.)

The original single-file version of the deck is still available for reference: [slides_cv_version.slides.html](https://raw.githack.com/TorbenSDJohansen/hedg-summer-school/refs/heads/main/slides_cv_version.slides.html).

## Repository structure

```
01_Off_the_shelf_models/          Lecture 1 (xaringan deck: Slides.Rmd -> Slides.html)
02_From_Tokens_to_Transcription/  Lecture 2 (xaringan deck: Slides.Rmd -> Slides.html)
exercises/                        Student exercise notebooks
exercises/solutions/              Corresponding solved notebooks
Tools/Slide_template/             Base xaringan template + Styleguide.md for new decks
Data/, Figures/                   Shared data and image assets
environment.yml                   Conda environment used by the slides and exercises
```

Each lecture folder is self-contained: its own `Figures/`, logo assets, and (after knitting) a `libs/` folder of xaringan JS/CSS - so it can be opened and rendered independently of the rest of the repo.

## Setup

### R (for knitting the slides)

Requires R with the `rmarkdown`, `xaringan`, and `xaringanExtra` packages, plus a working [pandoc](https://pandoc.org/) install (bundled with RStudio).

Open a lecture's `.Rproj` in RStudio and knit `Slides.Rmd`, or from a terminal:

```r
rmarkdown::render("01_Off_the_shelf_models/Slides.Rmd")
```

### Python (for the live code chunks and exercises)

Lecture 2 executes some Python chunks live via [reticulate](https://rstudio.github.io/reticulate/), backed by a conda environment. One-time setup:

```bash
conda env create -f environment.yml
```

This creates a `hedg-summer-school` environment with the packages used across both decks and the `exercises/` notebooks (torch, transformers, histocc, google-generativeai, etc.). See the comments in [environment.yml](environment.yml) for version-pinning notes (`torchtext` is intentionally excluded - see below).

**If knitting fails with `Unable to find conda binary`**, reticulate couldn't auto-discover your conda install. Fix it by creating a `.Renviron` file next to the `Slides.Rmd` you're knitting (one per lecture folder - these are gitignored since the path is machine-specific) containing:

```
RETICULATE_CONDA=/path/to/your/conda/Scripts/conda.exe   # Windows
RETICULATE_CONDA=/path/to/your/conda/bin/conda            # macOS/Linux
```

**`torchtext`** is unmaintained upstream and conflicts with the `torch` version `transformers` needs, so it's excluded from `environment.yml`. It's only needed for the GloVe embedding-space demo in `embedding_illustration.py` (not by anything the current slides or exercises execute live). If you need that to run, install `torchtext` in a separate environment pinned to `torch==2.3.*` and `torchtext==0.18.*`.

## Building new lectures

Follow [Tools/Slide_template/Styleguide.md](Tools/Slide_template/Styleguide.md) and start from [Tools/Slide_template/Slides.Rmd](Tools/Slide_template/Slides.Rmd).
