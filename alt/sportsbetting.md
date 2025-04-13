# Infinite Parlay With Mulligan

(So called because this puzzle will give you a betting strategy with a 50% chance
of winning an infinite parlay that gives you one Mulligan).

## Problem Statement

Suppose we are developing a betting strategy for betting on the over/under
for college basketball games, assuming the over/under line has a 50-50 probability
(and ignoring casino vigorish).

We have a special machine, dubbed the Weizenheimer, which will predict the
game total (total number of points scored) of a basketball game, with the probability
of a correct prediction equal to p.

(For simplicity, we assume the Weizenheimer also has the ability to identify
particular games where its prediction will be correct with probability p,
so that we do not have to treat p as varying from game to game.)

The betting strategy is as follows:

1. Pick a game from a virtually unlimited sequence (the season)
2. Run the game through the Weizenheimer to see whether/how to bet
3. Bet on the game, or skip to one of next two games

The goal of the betting strategy:

1. Create a long-term betting path where you lose at most once

Now, what probability p of correctly identifying game totals would give you
an exactly 50% chance of finding a sequence of bets where you could lose
at most once over an extended period of games/bets?


