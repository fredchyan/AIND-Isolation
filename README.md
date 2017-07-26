
# Build a Game-playing Agent

![Example game of isolation](viz.gif)

## Synopsis

In this project, students will develop an adversarial search agent to play the game "Isolation".  Isolation is a deterministic, two-player game of perfect information in which the players alternate turns moving a single piece from one cell to another on a board.  Whenever either player occupies a cell, that cell becomes blocked for the remainder of the game.  The first player with no remaining legal moves loses, and the opponent is declared the winner.  These rules are implemented in the `isolation.Board` class provided in the repository. 

This project uses a version of Isolation where each agent is restricted to L-shaped movements (like a knight in chess) on a rectangular grid (like a chess or checkerboard).  The agents can move to any open cell on the board that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board. Movements are blocked at the edges of the board (the board does not wrap around), however, the player can "jump" blocked or occupied spaces (just like a knight in chess).

Additionally, agents will have a fixed time limit each turn to search for the best move and respond.  If the time limit expires during a player's turn, that player forfeits the match, and the opponent wins.

Students only need to modify code in the `game_agent.py` file to complete the project.  Additional files include example Player and evaluation functions, the game board class, and a template to develop local unit tests.  


## Instructions

In order to complete the Isolation project, students must submit code that passes all test cases for the required functions in `game_agent.py` and complete a report as specified in the rubric.  Students can submit using the [Udacity Project Assistant]() command line utility.  Students will receive feedback on test case success/failure after each submission.

Students must implement the following functions:

- `MinimaxPlayer.minimax()`: implement minimax search
- `AlphaBetaPlayer.alphabeta()`: implement minimax search with alpha-beta pruning
- `AlphaBetaPlayer.get_move()`: implement iterative deepening search
- `custom_score()`: implement your own best position evaluation heuristic
- `custom_score_2()`: implement your own alternate position evaluation heuristic
- `custom_score_3()`: implement your own alternate position evaluation heuristic

You may write or modify code within each file (but you must maintain compatibility with the function signatures provided).  You may add other classes, functions, etc., as needed, but it is not required.

The Project Assistant sandbox for this project places some restrictions on the modules available and blocks calls to some of the standard library functions.  In general, standard library functions that introspect code running in the sandbox are blocked, and the PA only allows the following modules `random`, `numpy`, `scipy`, `sklearn`, `itertools`, `math`, `heapq`, `collections`, `array`, `copy`, and `operator`. (Modules within these packages are also allowed, e.g., `numpy.random`.)


### Quickstart Guide

The following example creates a game and illustrates the basic API.  You can run this example by activating your aind anaconda environment and executing the command `python sample_players.py`

    from isolation import Board
    from sample_players import RandomPlayer
    from sample_players import GreedyPlayer

    # create an isolation board (by default 7x7)
    player1 = RandomPlayer()
    player2 = GreedyPlayer()
    game = Board(player1, player2)

    # place player 1 on the board at row 2, column 3, then place player 2 on
    # the board at row 0, column 5; display the resulting board state.  Note
    # that the .apply_move() method changes the calling object in-place.
    game.apply_move((2, 3))
    game.apply_move((0, 5))
    print(game.to_string())

    # players take turns moving on the board, so player1 should be next to move
    assert(player1 == game.active_player)

    # get a list of the legal moves available to the active player
    print(game.get_legal_moves())

    # get a successor of the current state by making a copy of the board and
    # applying a move. Notice that this does NOT change the calling object
    # (unlike .apply_move()).
    new_game = game.forecast_move((1, 1))
    assert(new_game.to_string() != game.to_string())
    print("\nOld state:\n{}".format(game.to_string()))
    print("\nNew state:\n{}".format(new_game.to_string()))

    # play the remainder of the game automatically -- outcome can be "illegal
    # move", "timeout", or "forfeit"
    winner, history, outcome = game.play()
    print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
    print(game.to_string())
    print("Move history:\n{!s}".format(history))


### Coding

The steps below outline a suggested process for completing the project -- however, this is just a suggestion to help you get started.  A stub for writing unit tests is provided in the `agent_test.py` file (no local test cases are provided). (See the [unittest](https://docs.python.org/3/library/unittest.html#basic-example) module for information on getting started.)

The primary mechanism for testing your code will be the Udacity Project Assistant command line utility.  You can install the Udacity-PA tool by activating your aind anaconda environment, then running `pip install udacity-pa`.  You can submit your code for scoring by running `udacity submit isolation`.  The project assistant server has a collection of unit tests that it will execute on your code, and it will provide feedback on any successes or failures.  You must pass all test cases in the project assistant before you can complete the project by submitting your report for review.

0. Verify that the Udacity-PA tool is installed properly by submitting the project. Run `udacity submit isolation`. (You should see a list of test cases that failed -- that's expected because you haven't implemented any code yet.)

0. Modify the `MinimaxPlayer.minimax()` method to return any legal move for the active player.  Resubmit your code to the project assistant and the minimax interface test should pass.

0. Further modify the `MinimaxPlayer.minimax()` method to implement the full recursive search procedure described in lecture (ref. [AIMA Minimax Decision](https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md)).  Resubmit your code to the project assistant and both the minimax interface and functional test cases will pass.

0. Start on the alpha beta test cases. Modify the `AlphaBetaPlayer.alphabeta()` method to return any legal move for the active player.  Resubmit your code to the project assistant and the alphabeta interface test should pass.

0. Further modify the `AlphaBetaPlayer.alphabeta()` method to implement the full recursive search procedure described in lecture (ref. [AIMA Alpha-Beta Search](https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md)).  Resubmit your code to the project assistant and both the alphabeta interface and functional test cases will pass.

0. You can pass the interface test for the `AlphaBetaPlayer.get_move()` function by copying the code from `MinimaxPlayer.get_move()`.  Resubmit your code to the project assistant to see that the `get_move()` interface test case passes.

0. Pass the test_get_move test by modifying `AlphaBetaPlayer.get_move()` to implement Iterative Deepening.  See Also [AIMA Iterative Deepening Search](https://github.com/aimacode/aima-pseudocode/blob/master/md/Iterative-Deepening-Search.md)

0. Finally, pass the heuristic tests by implementing any heuristic in `custom_score()`, `custom_score_2()`, and `custom_score_3()`.  (These test cases only validate the return value type -- it does not check for "correctness" of your heuristic.)  You can see example heuristics in the `sample_players.py` file.


### Tournament

The `tournament.py` script is used to evaluate the effectiveness of your custom heuristics.  The script measures relative performance of your agent (named "Student" in the tournament) in a round-robin tournament against several other pre-defined agents.  The Student agent uses time-limited Iterative Deepening along with your custom heuristics.

The performance of time-limited iterative deepening search is hardware dependent (faster hardware is expected to search deeper than slower hardware in the same amount of time).  The script controls for these effects by also measuring the baseline performance of an agent called "ID_Improved" that uses Iterative Deepening and the improved_score heuristic defined in `sample_players.py`.  Your goal is to develop a heuristic such that Student outperforms ID_Improved. (NOTE: This can be _very_ challenging!)

The tournament opponents are listed below. (See also: sample heuristics and players defined in sample_players.py)

- Random: An agent that randomly chooses a move each turn.
- MM_Open: MinimaxPlayer agent using the open_move_score heuristic with search depth 3
- MM_Center: MinimaxPlayer agent using the center_score heuristic with search depth 3
- MM_Improved: MinimaxPlayer agent using the improved_score heuristic with search depth 3
- AB_Open: AlphaBetaPlayer using iterative deepening alpha-beta search and the open_move_score heuristic
- AB_Center: AlphaBetaPlayer using iterative deepening alpha-beta search and the center_score heuristic
- AB_Improved: AlphaBetaPlayer using iterative deepening alpha-beta search and the improved_score heuristic

## Submission

Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.

Please see the instructions in the [AIND-Sudoku](https://github.com/udacity/AIND-Sudoku#submission) project repository for installation and setup instructions. 

To submit your code to the project assistant, run `udacity submit isolation` from within the top-level directory of this project. You will be prompted for a username and password. If you login using google or facebook, follow the [instructions for using a jwt](https://project-assistant.udacity.com/faq).

This process will create a zipfile in your top-level directory named `isolation-<id>.zip`. This is the file that you should submit to the Udacity reviews system.


## Game Visualization

The `isoviz` folder contains a modified version of chessboard.js that can animate games played on a 7x7 board.  In order to use the board, you must run a local webserver by running `python -m http.server 8000` from your project directory (you can replace 8000 with another port number if that one is unavailable), then open your browser to `http://localhost:8000` and navigate to the `/isoviz/display.html` page.  Enter the move history of an isolation match (i.e., the array returned by the Board.play() method) into the text area and run the match.  Refresh the page to run a different game.  (Feel free to submit pull requests with improvements to isoviz.)


## PvP Competition

Once your project has been reviewed and accepted by meeting all requirements of the rubric, you are invited to complete the `competition_agent.py` file using any combination of techniques and improvements from lectures or online, and then submit it to compete in a tournament against other students from your cohort and past cohort champions.  Additional details (official rules, submission deadline, etc.) will be provided separately.

The competition agent can be submitted using the Udacity project assistant:

    udacity submit isolation-pvp

# Heuristic Analysis
__Frederick Chyan__

Friday, July 21, 2017

The purpose of this project is to find a heuristic that consistently outperforms AB_Improved, which is player's available moves minus opponent's available moves. The heuristic design iteration begins with selecting three custom heuristic functions. The first heuristic penalizes number of opponent's available moves. The second heuristic, rewards number of player's available moves. The third heuristic adds the center score to first heuristic, which is the Euclidean distance between player's position and the center of the board.
Followings are the three preliminary heuristic.

```
h1 = own_moves - 2 * opp_moves
h2 = 2 * own_moves - opp_moves
h3 = own_center_score + (own_moves - 2 * opp_moves)
```
Below are the result.

```
                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent    AB_Improved     AB_h1        AB_h2        AB_h3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random       8  |   2     6  |   4     6  |   4    10  |   0
    2       MM_Open      5  |   5     6  |   4     5  |   5     6  |   4
    3      MM_Center     9  |   1     8  |   2     6  |   4     8  |   2
    4     MM_Improved    6  |   4     6  |   4     6  |   4     7  |   3
    5       AB_Open      6  |   4     4  |   6     4  |   6     5  |   5
    6      AB_Center     6  |   4     4  |   6     7  |   3     6  |   4
    7     AB_Improved    4  |   6     4  |   6     4  |   6     4  |   6
--------------------------------------------------------------------------
           Win Rate:      62.9%        54.3%        54.3%        65.7%
```
First, notice that AB\_h3 seem to perform better than the other two heuristic. However, it still does not outperform AB\_Improved. In fact, all three preliminary heuristics score the same against AB\_Imrpoved. This result, however, suggest one should further improve upon AB\_h3.
Since h1 and h2 performs about the same, one wonder whether lowering the penalty to opponent's moves might make any difference as to not amplify prediction error.


```
h4 = own_center_score + (own_moves - 1.414 * opp_moves)
                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent       AB_h4
                        Won | Lost
    1     AB_Improved   21  |  19
--------------------------------------------------------------------------
           Win Rate:      52.5%
```

This is better, however, it's only slightly above 50%. Looking at center score, it was arbitrarily added to the heuristic. There are some problems with this approach. First, it's a different measurement. Second, it does not even have a negative value like own\_moves - opp\_moves does. Is there a way to map both of them to a same scale and aggregate them? Well it's too much trouble to linearize both measurements at every search level, so it's better to look for an easier way. Here a new scaling factor called *distance boost* is introduced. It amplifies player's own moves by a factor proportional to the ratio of player's center score against opponent's center score. Intuitively, it *encourages movement that will place player further from the center than the opponent is*.

```
distance_boost = own_center_score / (opp_center_score + own_center_score)
h5 = float((1+distance_boost) * own_moves - 1.414 * opp_moves)

                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent    AB_Custom_3
                        Won | Lost
    1     AB_Improved   25  |  15
--------------------------------------------------------------------------
           Win Rate:      62.5%


```
The result indeed looks promising, play the game 800 times to ensure this heuristic indeed outperforms AB\_Improved consistently. The trials are parallelized by playing 20\*2=40 matches on 4 processor cores 5 times.

```

                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent     AB_Custom    AB_Custom    AB_Custom    AB_Custom
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1     AB_Improved   26  |  14    31  |   9    30  |  10    29  |  11
--------------------------------------------------------------------------
           Win Rate:      65.0%        77.5%        75.0%        72.5%


 Match #   Opponent     AB_Custom    AB_Custom    AB_Custom    AB_Custom
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1     AB_Improved   25  |  15    23  |  17    26  |  14    23  |  17
--------------------------------------------------------------------------
           Win Rate:      62.5%        57.5%        65.0%        57.5%


 Match #   Opponent     AB_Custom    AB_Custom    AB_Custom    AB_Custom
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1     AB_Improved   29  |  11    23  |  17    25  |  15    29  |  11
--------------------------------------------------------------------------
           Win Rate:      72.5%        57.5%        62.5%        72.5%


 Match #   Opponent     AB_Custom    AB_Custom    AB_Custom    AB_Custom
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1     AB_Improved   29  |  11    27  |  13    25  |  15    26  |  14
--------------------------------------------------------------------------
           Win Rate:      72.5%        67.5%        62.5%        65.0%


 Match #   Opponent     AB_Custom    AB_Custom    AB_Custom    AB_Custom
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1     AB_Improved   26  |  14    24  |  16    29  |  11    26  |  14
--------------------------------------------------------------------------
           Win Rate:      65.0%        60.0%        72.5%        65.0%
```

Here almost all matches are above 60%. Since the outcome is either win or loss, the result follows a binomial distribution (win with probability p). To test whether the agent can beat AB\_Improved with 60% certainty. Use a one-tailed test with null and alternative hypotheses.

```
H0: p ≤ 0.6
H1: p > 0.6

```

The total number of winning trials is calculated by summing all won counters, which is 531. Then calculate the cumulative probability of winning at most 530 times, testing at threshold  α = 0.05. The p-value is 0.000116 which is less than α, the null hypothesis can be rejected.


```
26+31+30+29+25+23+26+23+29+23+25+29+29+27+25+26+26+24+29+26 = 531
p-value = 1–BINOM.DIST(530, 800, 0.6, TRUE) = 0.000116736 < .05 = α
```
so the design iteration concludes with 95% confidence that the new heuristic shows a significant improvement over AB\_Improved.

Summary
==
The best evaulation function is ```float((1+distance_boost) * own_moves - 1.414 * opp_moves)```. This is supported by three facts. Firstly, it beats AB\_Improve consistenly with at least 60% win rate (p-value < 0.05). Secondly, it is tuned from a prilimiary function that has very high win rate against random moves while the other two heuristics only won about half of the time aginst random, meaning the selected heuristic is guarded against random moves. Lastly, the first two other preliminary heuristics had lower win rates. 

# Research Review
*Frederick Chyan*

July 23, 2017

Selected Game Paper: [AlphaGo](https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf) by the DeepMind Team.

## Introduction
Just like the game of Isolation, Go is also finite, deterministic, and perfect information. However, unlike Isolation, Go has much larger search space which makes designing an optimal value function by hand very difficult. The AlphaGo paper is selected to understand how state of the art AI tackles games that's previous thought impossible for a machine to beat expert human player. AlphaGo uses novel approaches to combine neural networks and Monte Carlo tree search to achieve this.

## Techniques
Policy function p(a|s) estimates the utility of selecting action a in game state s. Value function v(s) estimates the outcome of the game under perfect play by both players. The greater the value the better. AlphaGo first uses deep convolutional neural networks to estimate the policy and value network. Deep convolutional neural networks were used to in visual domains such as image classification and face recognitions, here it passes the board positions as 19 x 19 image, and use convolutional layers to construct a representation of the position. Next, it uses policy and value networks to carry out Monte Carlo tree search by evaluating the position using value network and sampling actions using policy network.

### Policy Network and Value Network
AlphaGo's training pipeline works as follows. First, a 13 layer network is trained from 30 million positions from the KGS Go Server, this is the Supervised Learning policy network p\_sigma, it has 55.7% accuracy and 3ms to select an action. Also trained is a fast rollout policy network which has lower accuracy of 24.2% but only 2us to select an action. Next a Reinforcement Learning policy network, p\_rho is trained by making it play against a randomly select previous iteration of the policy network. Finally, the value network v\_theta is trained from the self-play data from RL policy network regressing on (state, outcome) pair. The reason why the value network is trained this way rather than using available data of complete games is because of overfitting due to successive positions are strongly correlated.

### Combining Neural Networks in Monte Carlo Tree Search (MCTS)
Perhaps the most interesting and powerful technique in AlphaGo is using Monte Carlo tree search to improve the prediction. It simulates and sample matches by rolling out searches in state spaces. It is highly parallelizable, and can be stopped at any time to achieve a balance of speed and accuracy. It introduces a random element in selecting next action, and constantly updates the parameters in estimation function, effectively making the AI smarter continuously and asynchronously. At every edge of the tree, there is an action value Q(s, a), visit count N(s,a), and prior probability P(s,a). The prior probability is based on SL policy network p\_sigma.
The MCTS is carried out in four steps. It first selects a node to expand, based on the bonus function u(s,a) which is proportional to the prior probability over the visit count. This ensures other actions will also be explored if this node gets expanded too much. When it reaches a leaf node at step L, it then expand the node and process it using SL policy network, now the output probability will be stored as the prior. Next, the leaf node will be evaluated using two different ways. 1. the value network v\_theta and 2. playing the game until termination using fast roll out policy network p\_pi. The resulting score are then weighted and summed together. Finally, the result will back propagate to the root node updating the visit count N, and action value Q. The AI then chooses the most visited node as the action to take.

## Key Result
Utilizing deep learning, Monte Carlo tree search, and reinforcement learning, AlphaGo studied and learned from professional players, then it evolves by playing and simulating countless number of games continuously, updating itself while the game in progress. Using just the value network, Alpha Go achieves a rating that places it in the Amateur dan. Also, it's also able to beat the strongest AI at the time by allowing 4 free moves. With Rollouts, Value Network and Policy network, AlphaGo can win >95% against other players. Meaning the search mechanism successfully combines the strong but impractical reinforcement learning policy network and weaker but faster rollout policy network. Winning several world champions AlphaGo achieved what was thought to be impossible previously. 
