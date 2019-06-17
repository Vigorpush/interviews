package com.company;

import javafx.util.Pair;

public class Game {
    private Pair<Team, Team> opponents;
    private Team winner;

    /**
     * A Constructor which uses Pair<Team, Team> opponents, Team winner
     * to construct a Game object
     *
     * @param opponents Pair<Team, Team>
     * @param winner    Team
     */
    public Game(Pair<Team, Team> opponents, Team winner) {
        this.opponents = opponents;
        this.winner = winner;
    }

    /**
     * A method which get Opponents
     *
     * @return opponents Pair<Team, Team>
     */
    public Pair<Team, Team> getOpponents() {
        return opponents;
    }

    /**
     * A method which get the Winner
     *
     * @return winner Team
     */
    public Team getWinner() {
        return winner;
    }

    /**
     * A method which set the Winner
     *
     * @param winner Team
     */
    public void setWinner(Team winner) {
        this.winner = winner;
    }

}