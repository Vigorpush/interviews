package com.company;

import javafx.util.Pair;
import org.junit.Assert;
import org.junit.Test;

public class GameTest {

    @Test
    public void getOpponents() {
        Team team1 = new Team("Team1", 1);
        Team team2 = new Team("Team2", 2);
        Pair<Team, Team> opponents = new Pair<>(team1, team2);
        Game game = new Game(opponents, team1);
        Assert.assertEquals(game.getOpponents().getKey().getTeamName(), "Team1");
        Assert.assertEquals(game.getOpponents().getValue().getTeamName(), "Team2");
    }

    @Test
    public void setOpponents() {
        Team team1 = new Team("Team1", 1);
        Team team2 = new Team("Team2", 2);
        Pair<Team, Team> opponents = new Pair<>(team1, team2);
        Game game = new Game(opponents, team1);
        Assert.assertEquals(game.getOpponents().getKey().getTeamName(), "Team1");
        Assert.assertEquals(game.getOpponents().getValue().getTeamName(), "Team2");
        team1 = new Team("Team11", 1);
        team2 = new Team("Team22", 2);
        opponents = new Pair<>(team1, team2);
        game = new Game(opponents, team1);
        Assert.assertEquals(game.getOpponents().getKey().getTeamName(), "Team11");
        Assert.assertEquals(game.getOpponents().getValue().getTeamName(), "Team22");
    }

    @Test
    public void getWinner() {
        Team team1 = new Team("Team1", 1);
        Team team2 = new Team("Team2", 2);
        Pair<Team, Team> opponents = new Pair<>(team1, team2);
        Game game = new Game(opponents, team1);
        Assert.assertEquals(game.getWinner().getTeamName(), "Team1");
    }

    @Test
    public void setWinner() {
        Team team1 = new Team("Team1", 1);
        Team team2 = new Team("Team2", 2);
        Pair<Team, Team> opponents = new Pair<>(team1, team2);
        Game game = new Game(opponents, team1);
        game.setWinner(team2);
        Assert.assertEquals(game.getWinner().getTeamName(), "Team2");
    }
}