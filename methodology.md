# Algo Consistency Index — methodology (v0.2, live since 2026-10-26)

## What it is
A daily reading of whether the market is paying the price patterns retail FX/CFD algorithms trade, computed per mechanism family (trend/breakout, mean-reversion, session-clock) from public market data, validated against live algo panels, with every test pre-registered before it ran and every result, including failures, published here.

## Three layers
1. **Probe index (public backbone).** Twelve frozen textbook recipes (Donchian 20/10, opening-range breakout, M15 range break, EMA 20/50 cross, RSI(2), Bollinger fade, prior-day level fade, Asian-range fade, fixed-time London entry, post-fix drift, pre-rollover fade, random-entry control) replayed on raw ticks of seventeen symbols with the broker's published spread, the raw-feed spread excess around rollover and $4 per lot round-turn commission. Reading per probe and symbol: z-score over the trailing two years of the 20-day R per trade minus the random control's R per trade in the same exit geometry. Family index = mean of its legs. Hypothetical, cost-included, never advertised as performance.
2. **Scoreboard (coincident).** Breadth, momentum z, realised drawdown load and SPRT kill count across live production accounts, labelled lagging.
3. **Pattern Integrity (leading candidates).** Fifteen standardised market-state features and a Regime Drift distance per family; descriptive until the nowcast test passes.

## Validation ladder and record
| Test | Question | Status |
|---|---|---|
| T0 | Do market-state features move with live family P&L? | Not passed (power 0.18–0.46); descriptive only |
| T1 | Do the probes experience what live algos experience? | Trend family passes under v0.2 on 7 blocks (rho 0.66, CI 0.32–0.83, twin −0.09); mean-reversion and session-clock do not; external panel pending |
| T2 | Does market state forecast family probe returns out of sample? | Not passed (fold A 2023: 0 of 12 cells; fold B 2024–25: one cell per model; shift twins met the raw bar more often than the real features). Layer 3 withheld |
| T3 | Does the banded sizing rule add return at matched drawdown? | Not run (requires T2) |
| T4 | Does it hold for three live months? | Running since the first live print, 2026-10-26 |

## Rules that apply to every number here
Pre-registration before any test; a shift-control twin beside every statistic; day-block statistics; realised drawdown only; costs as published; probe results labelled hypothetical; negatives published; backfill drawn differently from the live record; methodology versioned with 30-day notice and 90-day overlap for major changes.

## Change notice (posted 2026-10-27)
Decisions taken on 2026-10-27, published here before they take effect, under the 30-day notice and 90-day overlap rule:
- **Scoreboard membership (effective with the 2026-10-27 print):** every Bachelier account with a family tag and at least ten trading days counts as production; the deploy date is the account's first appearance on the Bachelier dashboard. Before this date the Scoreboard read a validated subset (tier P1); the JSON carries the tiers used. An account is active from its first appearance to its last trade plus ten business days, and the Scoreboard reads only days on which the panel is complete (a trailing day with a handful of accounts is dropped until the full daily run lands).
- **Fourth family, carry/overnight (CO), methodology v0.3:** its pre-registration will be published before any CO reading is computed; the three-family index continues to be printed for 90 days alongside the four-family one. Not before 2026-11-27.
- **Layer 2 universe:** the market-state features move from the 17 probe symbols to 25 symbols; the probe basket itself stays at the frozen 17. Dated when the first 25-symbol reading prints.
- **Branding:** the index is published by Prismatic Algos; the page styling changes, the numbers do not.
- **Publication time (effective with the 2026-10-28 print):** the daily print moves from 06:30 ET to 18:30 ET, after the 17:00 ET broker close and the 17:17 ET Bachelier run, so that one print covers the complete broker day and governs the whole following trading day. A print dated D now reads the Scoreboard through day D (before this date it read through D−1). The computation is unchanged.

## Reports
Pre-registrations and reports live in the project repository under `aci/phase0`, `aci/phase1`, `aci/phase2`, `aci/phase3`.
