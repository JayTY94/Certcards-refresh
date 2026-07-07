Diagnostic Method — Study Notes
Root-cause analysis & hypothesis-driven debugging, in flashcard form. Names for the moves you already make.

Your focus five (the Round 4 gaps): Delta debugging · Swiss cheese model · Fishbone/Ishikawa · Counterfactual (but-for) test · Schrödinbug.

The Core Loop




Root cause analysis (RCA). A structured investigation that traces a problem back to its origin so the fix prevents recurrence — not just the first change that makes the error disappear. The whole discipline these notes describe.

• • •

Symptom fix vs. root-cause fix. A symptom fix silences the error; a root-cause fix removes the thing that produced it. The tell you only patched a symptom: the bug comes back later, often wearing a different mask.

• • •

Hypothesis-driven debugging. Applying the scientific method to a bug: observe, form explicit hypotheses, design a test that discriminates, run it, converge on evidence — before writing a fix. Beats fix-and-retry because you rank fixes by falsifiable evidence, not by gut prior.

• • •

Scientific debugging (Zeller). The formal name for the above, from Andreas Zeller's work: observe failure → form a falsifiable hypothesis → design an experiment that could disprove it → refine. "Debugging as a science, not a craft."

• • •

Competing hypotheses. Generate several explanations (3–5) before touching the code. One hypothesis means you rank fixes by your first hunch; multiple forces you to rank by evidence. This is a control-group partition applied to ideas.

• • •

Falsifiable hypothesis. A hypothesis that names a specific test whose result could prove it wrong. "It's probably a caching thing" isn't falsifiable; "if it's the cache, clearing it makes the error vanish" is. Designing the test that would refute your own theory is what keeps you honest.

• • •

Minimal reproduction. The smallest case that still triggers the failure. Every element you remove that keeps the bug alive is a confounder eliminated — turning "sometimes it breaks" into a sharp, testable signal.

• • •

Instrument before you patch / test the unifying variable before documenting. When several symptoms look like they share one cause, prove that shared cause empirically before writing the RCA. A plausible-but-wrong postmortem is worse than none — it stops the team from looking.

• • •

Change one variable at a time (controlled experiment). Alter a single factor per test, holding everything else constant, so any change in outcome is attributable. Change several at once and the result is uninterpretable.

• • •

Confounding variable. A hidden factor that correlates with the outcome but isn't the cause — e.g., answer length correlating with "correct" on a badly written quiz. Good experiments hold confounders constant so they can't masquerade as the cause.



Narrowing & Localization



Bisection / binary search. Repeatedly halve the suspect space and test the midpoint; each test eliminates half. Turns a linear hunt through N candidates into ~log₂(N) steps.

• • •

Delta debugging (Zeller, 1999). An algorithm that automatically trims a failure-inducing input or change-set down to the minimal piece that still triggers the bug — halving and re-testing until only the essential trigger remains. It's minimal reproduction, mechanized. From the paper "Yesterday, my program worked. Today, it does not. Why?"

• • •

git bisect. Delta debugging applied to commit history: mark a known-good and known-bad commit, and it binary-searches the range to find the bug-inducing commit. Watch out — a flaky test can give a false "fail" and send it down the wrong half.

• • •

Fault isolation / boundary instrumentation. In a multi-stage system (API → service → cache → DB), log what enters and exits each boundary to localize where the data breaks before investigating why. Isolate the failing component first; don't guess.

• • •

Bug-inducing commit (BIC). The specific commit that introduced a regression — the thing git bisect is hunting for.




Cause-Analysis Tools



Five Whys. Ask "why" iteratively, each answer feeding the next question, until you reach a systemic gap you can actually change. Five is a rule of thumb — stop when a fix would prevent recurrence, not at the first satisfying "someone forgot."

• • •

Differential diagnosis. From medicine: enumerate all plausible causes, rank by likelihood, then run the test that discriminates between them — ruling candidates out rather than chasing your favorite. The power move is the single test that eliminates the most candidates at once.

• • •

Fishbone / Ishikawa diagram. A cause-and-effect diagram (named for Kaoru Ishikawa) with the problem at the "head" and candidate causes branching off a spine, grouped into the 6 M's: Method, Machine, Material, Manpower, Measurement, Milieu (environment). The visual, group-friendly counterpart to differential diagnosis — lay causes out by category so none get missed, then test.

• • •

Fault tree analysis (FTA). A top-down diagram that starts from the failure and branches downward through the combinations of conditions (AND/OR gates) that could produce it. Good for "how many ways could this happen."

• • •

Pareto principle ("vital few"). Most failures trace back to a small minority of causes — the 80/20 rule applied to defects. Tells you where to spend investigation effort first.

• • •

Swiss cheese model (Reason). Each safeguard is a slice of cheese with holes; an incident only gets through when the holes in every layer momentarily line up. Reframes "the one root cause" as "why did all our defenses fail at once." The backbone of blameless postmortems and defense-in-depth.





Cause Vocabulary — the Confused Pairs



Proximate cause vs. root cause. Proximate = the immediate, surface trigger ("someone forgot the step"). Root = the systemic gap that let it happen ("no automated check enforced the step"). Five Whys is the walk from one to the other.

• • •

Necessary vs. sufficient cause. Necessary = the failure can't happen without it. Sufficient = it alone can produce the failure. The root causes you usually want are necessary; the strongest are both.

• • •

Counterfactual (but-for) test. "But for this factor, would the failure still have happened?" If removing it removes the failure, it's a necessary cause. Don't confuse with the null hypothesis — that's the default "no effect" assumption you try to reject in a statistical test, a different tool.

• • •

Latent vs. active failure (Reason). Active = the unsafe act directly linked to the incident (the navigation error). Latent = a dormant weakness sitting in the system long before it contributes (the missing safeguard). Latent failures are the holes already in the cheese.

• • •

Correlation vs. unifying variable. Two things moving together (both metrics dropped at 2 AM) is correlation. A unifying variable is a proven common cause — established only by showing one change drives both. Verify before you name it in the writeup.

• • •

Occam's razor vs. Hickam's dictum. Occam: prefer the single simplest explanation. Hickam: "a patient can have as many diseases as they please" — sometimes there are two independent defects. When a fix kills one symptom but not the other, suspect Hickam.




Bug Taxonomy (folklore, but useful)


Bohrbug. A solid, deterministic bug that reproduces reliably under the same conditions — the easy kind. Named after the stable Bohr atom model.


• • •

Mandelbug. A bug whose causes are so complex or chaotic that its behavior looks nondeterministic. Named after the Mandelbrot fractal.

• • •

Schrödinbug. A bug that never misbehaved until someone read the code, realized it couldn't have worked, and then it started failing. Contrast the Heisenbug: a Heisenbug hides when observed; a Schrödinbug is revealed by observation.





Cognitive Hazards & Anti-Patterns


Confirmation bias. Once you have a first guess, you notice evidence that fits it and discount evidence that doesn't. Antidotes: form competing hypotheses, and design tests to refute rather than confirm.

• • •

Shotgun debugging. Making many undirected changes and hoping one accidentally fixes the bug — no hypothesis, just poke and pray. Even when it "works," you learn nothing and may bury new bugs. The opposite of hypothesis-driven debugging.


• • •

Regression. A previously-working behavior that breaks after a change. The prompt for delta debugging / git bisect and the first question: what changed?

