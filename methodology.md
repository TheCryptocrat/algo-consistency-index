# Algo Consistency Index — methodology (v0.2, backfill; not yet live)

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
| T2 | Does market state forecast family probe returns out of sample? | See report |
| T3 | Does the banded sizing rule add return at matched drawdown? | See report |
| T4 | Does it hold for three live months? | Starts at the first live print |

## Rules that apply to every number here
Pre-registration before any test; a shift-control twin beside every statistic; day-block statistics; realised drawdown only; costs as published; probe results labelled hypothetical; negatives published; backfill drawn differently from the live record; methodology versioned with 30-day notice and 90-day overlap for major changes.

## Reports
Pre-registrations and reports live in the project repository under `aci/phase0`, `aci/phase1`, `aci/phase2`, `aci/phase3`.
