# Slide styleguide (Statistics 2026)

This document defines how future lecture slides should be built in this course.

It is written for both humans and machines and is based on the existing slide decks in the course folders.

---

## Conformance checklist

> **Claude Code instruction:** Whenever the user asks whether slides conform to the styleguide, or asks you to update slides to match the styleguide, load this checklist into a `TodoWrite` task list and work through every item. Mark each item done as you verify or fix it. Do not skip items.

### A) Technical setup (§2)
- [ ] Output format is `xaringan::moon_reader`
- [ ] Ratio is `16:9`
- [ ] `insert-logo.html` included via `after_body`
- [ ] `self_contained: false` and `lib_dir: libs`
- [ ] xaringanExtra chunks present: `use_panelset()`, `use_tile_view()`, `use_progress_bar(color = "#808080", location = "top")`
- [ ] All CSS utility classes defined: `.pull-left/right`, `.pull-left/right-wide`, `.pull-left/right-narrow`, `.tiny123`, `.small123`, `.large123`, `.red`, `.orange`, `.green`

### B) Title slide (§3)
- [ ] Slide class is `class: center, inverse, middle`
- [ ] Heading hierarchy: `# Statistics` / `## <topic>` / `### (Chapter X)`
- [ ] Lecturer name is **Christian Vedel**, Department of Economics, University of Southern Denmark
- [ ] Email is **christian-vs@sam.sdu.dk** as a clickable `mailto:` link
- [ ] Date line: `` ### Updated `r Sys.Date()` ``
- [ ] No placeholder or previous lecturer name/email remains

### C) Deck structure (§3)
- [ ] Agenda slide (`# Today's lecture`, `class: middle`) is the **first slide after** the title slide
- [ ] Agenda uses `.pull-left-wide[]` for bullets and `.pull-right-narrow[]` for `Figures/Trees1.jpg`
- [ ] Agenda has a one-line framing sentence in bold, followed by section bullets
- [ ] Total slide count does not exceed 35 (for a 90-minute lecture)
- [ ] Section divider slides (`class: inverse, middle, center`) are present for major transitions, or have been intentionally removed to meet the slide-count target
- [ ] Deck ends with `# Before next time` slide using `.pull-left[]` + `.pull-right[]` (Trees image)
- [ ] No placeholder text remains anywhere (e.g. `[Topic]`, `Chapter X`)

### D) Slide layout (§4)
- [ ] Default body layout uses `.pull-left-wide[]`
- [ ] Visual support (image, key note) paired in `.pull-right-narrow[]`
- [ ] Comparison slides use balanced `.pull-left[]` + `.pull-right[]`
- [ ] All body content is inside `.pull-left-wide[]` blocks (not bare top-level bullets)
- [ ] `--` reveals are only at the **top level** between `.pull-left-wide[]` blocks — never inside a div
- [ ] Each `.pull-left-wide[]` block contains only the *new* content for that step (xaringan accumulates previous blocks automatically)
- [ ] Overflowing slides are shortened or split — not left to overflow

### E) Content and pedagogy (§5)
- [ ] Terms bolded on first introduction
- [ ] Formal definitions and key statements in blockquotes (`> ...`)
- [ ] At least one `# .red[Practice N: ...]` slide per major section/concept
- [ ] Practice slides numbered consecutively within the deck
- [ ] Every practice slide has a hidden answer chunk (`eval=FALSE, include=FALSE`)
- [ ] At least one `# .red[Raise your hand N: ...]` slide (typically before a practice slide or at section end)
- [ ] Every raise-your-hand slide has `countdown(0, 20, top=TRUE)` at the top
- [ ] Raise-your-hand questions (2–3 per slide) are inside `.pull-left-wide[]`
- [ ] Every raise-your-hand wrong option is genuinely plausible (targets a specific, named misconception with a coherent student argument)
- [ ] Correct letters assigned via `shuf -e A B C` (run before writing each slide) — no systematic positional pattern
- [ ] Questions with multiple correct answers explicitly say so in the stem ("Select all that apply")
- [ ] Each question is in its own `.pull-left-wide[]` block with `--` between questions at the top level
- [ ] All raise-your-hand answers are in a hidden chunk only (`eval=FALSE, include=FALSE`) — never in the slide body

### F) Math and notation (§6, §11)
- [ ] LaTeX math used consistently (`$...$`, `$$...$$`)
- [ ] Random variables uppercase (`X`, `Y`), realizations lowercase (`x`, `y`)
- [ ] No bare `P(X = x)` in slide bodies — use `f(x)` instead
- [ ] No bare `P(X ≤ x)` in slide bodies — use `F(x)` instead
- [ ] `P(·)` appears only when explicitly defining or deriving a relationship
- [ ] Important formulas on separate `$$...$$` lines
- [ ] No multi-line `$$...$$` blocks — every display equation is on a single source line (use `\begin{cases}...\end{cases}` etc. collapsed to one line)
- [ ] No `\\[Xpt]` vertical-spacing modifiers inside equations — use bare `\\`
- [ ] No `$...$` inline math inside CSS class spans (`.small123[...]`, `.red[...]`, etc.)
- [ ] No bold markers (`**`) immediately adjacent to math delimiters — `**$k$**` does not render; write `$k$**-th**` or restructure

### G) Figures and code (§7, §8)
- [ ] All figure assets stored in the lecture's `Figures/` folder
- [ ] Figure paths are relative (e.g. `Figures/filename.png`)
- [ ] Image captions (if any) follow immediately after the image line
- [ ] Setup/helper chunks use `echo=FALSE`
- [ ] Chunk names are descriptive
- [ ] No verbose R output visible on slides

---

## 0) Basic info

Here is the basic information of the course. Please reference this, when needed.

1. **Name of course:** `Statistics`
4. **Name of lecturer:** Christian Vedel
5. **Lecturer affiliation:** Department of Economics
6. **Lecturer contact email:** christian-vs@sam.sdu.dk

---

## 1) Design goals (always apply)

1. **Avoid clutter**: one core idea per slide.
2. **Prioritize clarity over density**: short bullets, clear headings, enough whitespace.
3. **Teach progressively**: introduce difficult concepts step by step.
4. **Be consistent**: same structure, classes, and notation across all lectures.
5. **Keep slides practical**: include examples and mandatory practice prompts.

---

## 2) Required technical setup (MUST)

Every lecture deck should follow the same technical scaffold:

- Output format: `xaringan::moon_reader`
- 16:9 ratio
- `insert-logo.html` included via `after_body`
- `self_contained: false`
- `lib_dir: libs`
- xaringan extras enabled:
	- panelset
	- tile view
	- progress bar (`#808080`, top)
- CSS utility classes included:
	- `.pull-left`, `.pull-right`
	- `.pull-left-wide`, `.pull-right-wide`
	- `.pull-left-narrow`, `.pull-right-narrow`
	- `.tiny123`, `.small123`, `.large123`
	- `.red`, `.orange`, `.green`

Use [Statistics/XX_Template/Slides.Rmd](../XX_Template/Slides.Rmd) as the base template.

---

## 3) Deck-level structure

### Title slide (MUST)
The opening slide should include:

- Course name (`# Statistics`)
- Lecture topic title (`## ...`)
- Optional chapter reference (`### (Chapter X)` where relevant)
- Lecturer name + affiliation
- Email as clickable mailto link
- `### Updated `r Sys.Date()``

Title slide class should be:

- `class: center, inverse, middle`

### Agenda / roadmap slide (MUST)

- Always include a "This lecture" slide immediately after the title slide.
- Use `.pull-left-wide[]` for agenda bullets and `.pull-right-narrow[]` for the Trees image:

```rmd
---
class: middle
# Today's lecture
.pull-left-wide[
**[One-line framing sentence]**

- **Section 1:** ...
- **Section 2:** ...
]

.pull-right-narrow[
![Trees](Figures/Trees1.jpg)
]
```

### Closing slide (MUST)

- Always end the deck with a "Before next time" slide using the same Trees image:

```rmd
---
# Before next time
.pull-left[
- Read the assigned reading
- Next time: [Topic] $\rightarrow$ Chapter X
]

.pull-right[
![Trees](Figures/Trees1.jpg)
]
```

### Section divider slides (RECOMMENDED)

Use this class for major transitions:

- `class: inverse, middle, center`

Keep divider content short (typically one section title).

Section dividers improve pacing in longer decks but add slides without content. They are the **first thing to cut** when trimming slide count.

### Target slide count

- **Maximum: 35 slides** for a 90-minute lecture. The minimum is not binding — a shorter deck is fine if all the material is covered.
- Above 35: the deck needs trimming — merge closely related slides, absorb proof steps as `--` reveals, and remove section dividers first.

---

## 4) Slide composition rules

1. **Default body layout**: put main content in `.pull-left-wide[]`.
2. **When adding visual support**: pair with `.pull-right-narrow[]` (image, key note, reminder).
3. **Comparison slides**: use `.pull-left[]` + `.pull-right[]` (balanced columns).
4. **Figure-only emphasis**: use `.center[]` around image where useful.
5. **Footnotes / side notes**: use `.small123[]`, optionally inside `.footnote[]`.
6. **When a slide overflows**, fix it in this priority order:
	1. **Shorten** — reduce wordiness, combine related points (e.g. merge a verbal description with its formula into one bullet).
	2. **Split** — break into two consecutive slides with the same or similar title.
	3. **Side-by-side** — use `.pull-left[]` + `.pull-right[]` only when the content is naturally parallel (e.g. definition vs. example).

---

## 5) Content style and pedagogy

### Text style

- Prefer concise bullets over long paragraphs.
- Bold terms on first introduction.
- Use blockquotes (`> ...`) for formal definitions and key statements.

### Progressive reveal

- Use `--` to reveal content step by step.
- **CRITICAL LIMITATION**: `--` only works at the **top level** of a slide. It does **not** work inside CSS class containers such as `.pull-left-wide[]`, `.pull-left[]`, `.pull-right[]`, etc. — it will render as literal text `--` instead of triggering a reveal.
- **Correct pattern**: place each chunk of content in its own `.pull-left-wide[]` block, with `--` between blocks at the top level. xaringan accumulates previous blocks, so each new block only needs to contain the *new* content for that step:

```rmd
.pull-left-wide[
- First point
]

--

.pull-left-wide[
- Second point (first block remains visible above)
]

--

.pull-left-wide[
- Third point
]
```

- Group closely related content (e.g. an introductory sentence + its formula) into a single block rather than splitting every line into its own reveal step.
- Definition slides: show the full blockquote in the first block (no leading `--`), then reveal explanatory bullets with subsequent `--` blocks.
- Figure slides: use `.center[]` with no reveal — show the figure immediately.

### Practice slides

- Practice prompts are **mandatory**.
- Include practice slides throughout the lecture.
- As a default rule, add at least one practice slide per major concept/section.
- Existing pattern: red heading label with sequential number, e.g. `# .red[Practice 1: ...]`, `# .red[Practice 2: ...]`. Number practice slides consecutively within each deck.
- Always include a hidden teacher answer chunk:
	- `eval=FALSE, include=FALSE`
- Answers must **never** appear in the rendered slides — always hidden in code chunks.

### Raise your hand slides

Use `# .red[Raise your hand N: ...]` slides for in-class multiple choice discussion (where N is a sequential number within the deck, e.g. `# .red[Raise your hand 1: ...]`). These differ from practice slides in that they are designed to provoke debate, not just compute.

**Design principle — all wrong answers must be genuinely plausible:**
- Every option (A, B, C) must reflect a coherent line of reasoning a student could actually follow — not a straw man.
- Wrong options should target specific, named misconceptions and include a brief label that makes them sound equally credible at first read.
- The correct answer must be unambiguous to someone who knows the statistics.
- Teacher notes in the hidden chunk must explain *why* each wrong answer is tempting and, for questions where multiple options are partially true, why the correct answer is the *most* complete explanation.

**Randomise which letter is correct:**
- There must be no systematic pattern in which letter (A, B, or C) is the right answer — students should not be able to guess by position.
- Before writing each RYH slide, run the following bash snippet to get a random assignment of correct letters (one per question, no repeats within the slide):

```bash
shuf -e A B C
```

  The output is a random permutation, e.g. `C / A / B` — assign Q1 → C, Q2 → A, Q3 → B, then construct options so the correct answer lands on that letter.

**Multiple correct answers (use sparingly):**
- For philosophical, interpretive, or practical questions — and occasionally for maths questions where more than one statement is genuinely true — it is acceptable to have two correct answers.
- When a question has multiple correct answers, make this explicit in the question stem (e.g. *"Which of the following are true? Select all that apply."*).
- Multiple-correct-answer questions should be the exception, not the default. Use them only when the ambiguity itself is pedagogically useful (e.g. to show that two seemingly different statements are both valid).

**Sequential reveal — always use `--` between questions:**
- Questions are revealed one at a time so the class can discuss Q1 before Q2 appears.
- Because `--` does not work inside CSS containers, each question must be in its own `.pull-left-wide[]` block at the top level, with `--` between blocks.

**Layout:**

```rmd
---
# .red[Raise your hand N: <topic>]

` `` `{r echo=FALSE}
library(countdown)
countdown(0, 20, top=TRUE)
` `` `

.pull-left-wide[
**Q1.** <question text>

- **A)** <option> — <brief label>
- **B)** <option> — <brief label>
- **C)** <option> — <brief label>
]

--

.pull-left-wide[
**Q2.** <question text>

- **A)** <option> — <brief label>
- **B)** <option> — <brief label>
- **C)** <option> — <brief label>
]

` `` `{r <chunk-name>, eval=FALSE, include=FALSE}
# ANSWERS
#
# Q1: Answer X — <one-line summary>
#   A: <why this option is tempting / what misconception it reflects>
#   B: <why this option is tempting / what misconception it reflects>
#   C: <why this option is tempting / what misconception it reflects>
#
# Q2: Answer X — <one-line summary>
#   A: ...
#   B: ...
#   C: ...
` `` `
```

**Rules:**
- Include a `countdown(0, 20, top=TRUE)` timer (20 seconds) at the top of every raise-your-hand slide.
- Always place each question in its own `.pull-left-wide[]` block with `--` between blocks — never put two questions inside the same container.
- Answers and teacher reasoning go **only** in the hidden chunk — never in the slide body.
- Place raise-your-hand slides at natural concept checkpoints, typically just before a practice slide or at the end of a section. When both fit the same checkpoint, raise-your-hand comes first.

### Tone

- Professional, direct, and student-friendly.
- Pragmatic focus: explain why concepts matter and how to use them.

---

## 6) Math, notation, and equations

1. Use LaTeX math consistently (`$...$`, `$$...$$`).
2. Keep notation consistent with course conventions:
	 - Random variables uppercase (`X`, `Y`)
	 - Realizations lowercase (`x`, `y`)
3. Display important formulas on separate lines.
4. Prefer one major equation block per teaching step.

### xaringan math rendering rules (MUST)

These are hard constraints — violating any of them causes equations to display as raw LaTeX:

- **Single-line display math**: every `$$...$$` block must be on one source line. remarkjs splits multi-line blocks into separate paragraphs before MathJax runs. Multi-line environments (`\begin{cases}`, `\begin{aligned}`, etc.) must be collapsed to a single line:
  ```
  $$\hat{q}_p = \begin{cases} X_{(np+1)}, & \text{if } [np] \neq np \\ \dfrac{X_{(np)}+X_{(np+1)}}{2}, & \text{if } [np] = np \end{cases}$$
  ```

- **No `\\[Xpt]` spacing modifiers**: `\\[4pt]` and `\\[6pt]` are misread by the markdown renderer — `\\` becomes a line break, then `[4pt]` looks like a link reference. Use bare `\\` instead.

- **No math inside CSS class spans**: `.small123[$...$]`, `.red[$...$]`, `.tiny123[$...$]` etc. all break MathJax. If you need smaller math, use `\scriptstyle` inside the math itself, or restructure the sentence so the math is outside the span.

- **No `**` immediately adjacent to `$`**: `**$k$**` does not render — the bold boundary interferes with MathJax delimiter scanning. Keep math delimiters away from `**` boundaries, e.g. `$k$**-th order statistic**`.

---

## 7) Figures and media

1. Store lecture assets in the lecture's `Figures/` folder.
2. Use relative paths (e.g., `Figures/filename.png`).
3. Prefer markdown image syntax for normal use.
4. Use HTML `<img ...>` only when explicit size control is needed.
5. Ensure each visual has a pedagogical purpose (not decorative only).
6. When placing a caption directly below an image, add **two trailing spaces** after the image line to force a markdown line break. Without them the caption may render inline or misaligned:

```rmd
![Alt text](Figures/filename.png)
.small123[*Caption text*]
```

---

## 8) Code chunks and reproducibility

1. Use code only when it supports the concept.
2. Keep setup/helper chunks silent (`echo=FALSE` when appropriate).
3. For hidden instructor notes/solutions, use `eval=FALSE, include=FALSE`.
4. Keep chunk names descriptive.
5. Avoid verbose output on slides.

---

## 9) Consistency checklist before publishing

Before finalizing a deck, verify:

1. Title slide fields are updated (title, lecturer, email, date).
2. Section divider slides are in place.
3. Layout classes are used consistently.
4. Notation is consistent throughout.
5. Figures render and paths work.
6. No placeholder text remains.
7. Slides knit successfully to HTML.
8. Practice slides are included for each major section/concept.
9. Raise-your-hand slides have a countdown timer and all answers are hidden in `eval=FALSE, include=FALSE` chunks.

---

## 10) Default instruction block for future slide generation (machine-readable)

When generating a new lecture deck, follow these rules in order:

1. Start from [Statistics/XX_Template/Slides.Rmd](../XX_Template/Slides.Rmd).
2. Keep all xaringan/xaringanExtra setup chunks and CSS utility classes.
3. Build title slide with course/topic/lecturer/email/date.
4. Add one agenda slide.
5. Structure lecture into sections separated by inverse divider slides.
6. Put normal slide content in `.pull-left-wide[]` unless comparison layout is needed.
7. Use `--` for incremental reveal when concepts are multi-step.
8. Use blockquotes for definitions and theorem-like statements.
9. Add mandatory practice slides for each major concept/section. Always include a hidden answer chunk (`eval=FALSE, include=FALSE`).
10. Add raise-your-hand slides at concept checkpoints (typically just before a practice slide, or at section end — raise-your-hand before practice when both fit the same checkpoint). Each slide: countdown timer, 2–3 A/B/C questions in `.pull-left-wide[]`, all answers in a hidden chunk. Wrong options must target specific misconceptions — never use implausible distractors. Vary the correct letter (A/B/C) across questions — no systematic pattern. For philosophical, interpretive, or multi-statement questions, two correct answers are permitted; make this explicit in the question stem.
11. Keep visual design minimal and consistent with this styleguide.

---

## 11) Course-specific conventions (Statistics)

This section documents notation and conventions specific to the Statistics course. All slides must be consistent with the notation established in the earlier lecture decks.

### Notation reference lectures

- **Lecture 02** (`02_Uncertainty_and_probability/Slides.Rmd`): probability, events, sample space
- **Lecture 03** (`03_Random_variables/Slides.Rmd`): random variables, probability functions, densities, CDFs

### Random variables and realizations

- **Random variables**: always uppercase — $X$, $Y$, $Z$
- **Realizations** (observed values): always lowercase — $x$, $y$, $z$
- A random variable is a function: $X : \Omega \to \mathbb{R}$

### Probability function (discrete random variables)

The probability function uses $f(\cdot)$, **not** $P(X = x)$ directly on its own:

> $f(x) = P(X = x)$

- Use $f(x)$ or $f_X(x)$ (subscript when multiple RVs are in play)
- Properties: $0 \leq f(x) \leq 1$; $\sum_i f(x_i) = 1$
- CDF: $F(x) = P(X \leq x) = \sum_{x_i \leq x} f(x_i)$
- **Do not** write bare $P(X = x)$ in slide body — use $f(x)$ instead

### Probability density function (continuous random variables)

For continuous random variables (e.g. income, wages), $P(X = x) = 0$ always. Use $f(\cdot)$:

> $f(x) = \dfrac{dF(x)}{dx}$

- $f(x)$ is the **density**, not a probability — it can exceed 1
- Probabilities are areas: $P(a < X \leq b) = \int_a^b f(x) \, dx$
- Expected value (continuous): $E(X) = \int_{-\infty}^\infty x \, f(x) \, dx$
- Expected value (discrete): $E(X) = \sum_i x_i \, f(x_i)$
- **Never** write $P(X = x)$ for a continuous random variable — use $f(x)$ for the density value

### Joint, marginal, and conditional distributions

| Concept | Discrete | Continuous |
|---------|----------|------------|
| Joint | $f(x, y) = P(X=x, Y=y)$ | $f(x, y)$ (joint density) |
| Marginal | $f_X(x) = \sum_j f(x, y_j)$ | $f_X(x) = \int_{-\infty}^\infty f(x,y)\,dy$ |
| Conditional | $f_{X\|Y}(x\|y) = f(x,y)/f_Y(y)$ | same form |
| Independence | $f(x,y) = f_X(x) \cdot f_Y(y)$ | same form |

### Other notation

- CDF always: $F(x) = P(X \leq x)$
- **Default**: use $F$ and $f$ notation rather than $P$ in slide bodies. Write $F(7)$ not $P(Y \leq 7)$; write $F(9) - F(3)$ not $P(3 \leq Y \leq 9)$. Reserve $P(\cdot)$ only when explicitly defining or deriving a relationship (e.g. $F(x) = P(X \leq x)$).
- Independence of events: $A \perp B$
- Conditional probability of events: $P(A \mid B) = P(A \cap B) / P(B)$
- Sample space: $\Omega$; impossible event: $\varnothing$
- Distribution shorthand (where applicable): $X \sim U[a, b]$, $X \sim N(\mu, \sigma^2)$

