package com.company;

import org.junit.Assert;
import org.junit.Test;

public class TournamentTest {

    @Test
    public void getResults() {
        Tournament t = new Tournament();
        t.addTeam("Team1|1");
        Assert.assertEquals(1, t.getTeams().size());
        t.addTeam("Team2|2");
        Assert.assertEquals(2, t.getTeams().size());
        t.addGame("1|2");
        Assert.assertEquals("Team - Team1 VS  Team - Team2 : The Winner is : Team1", t.getGameResult());
        t.addTeam("Team3|3");
        Assert.assertEquals(3, t.getTeams().size());
        t.addTeam("Team4|4");
        Assert.assertEquals(4, t.getTeams().size());
        t.addGame("3|4");
        Assert.assertEquals("Team - Team1 VS  Team - Team2 : The Winner is : Team1Team - Team3 VS  Team - Team4 : The Winner is : Team3", t.getGameResult());
    }

    @Test
    public void getAllTeamsInformation() {
        Tournament t = new Tournament();
        Assert.assertEquals(0, t.getTeams().size());
        t.addTeam("Team|1");
        Assert.assertEquals(1, t.getTeams().size());
        t.addPlayer("Tom|1|1");
        Assert.assertEquals(1, t.getTeams().size());
        Assert.assertEquals("Existing Team are(is) : \n" +
                "Team Name : Team Team id  : 1\n", t.getAllTeamsInformation());
    }

    @Test
    public void addPlayer() {
        Tournament t = new Tournament();
        t.addTeam("Team|1");
        Assert.assertEquals(1, t.getTeams().size());
        t.addPlayer("Tom|1|1");
        Assert.assertEquals("Tom", t.getTeams().get(0).getPlayers().get(0).getName());
        t.addPlayer("Jerry|2|1");
        Assert.assertEquals("Jerry", t.getTeams().get(0).getPlayers().get(1).getName());
    }

    @Test
    public void addCoach() {
        Tournament t = new Tournament();
        t.addTeam("Team|1");
        Assert.assertEquals(1, t.getTeams().size());
        t.addCoach("Tom|11|1");
        Assert.assertEquals("Tom", t.getTeams().get(0).getCoach().getName());
        t.addCoach("Jerry|11|1");
        Assert.assertEquals("Jerry", t.getTeams().get(0).getCoach().getName());
    }

    @Test
    public void addTeam() {
        Tournament t = new Tournament();
        t.addTeam("Team|1");
        Assert.assertEquals(1, t.getTeams().size());
        t.addTeam("Team2|1");
        Assert.assertEquals(1, t.getTeams().size());
        t.addTeam("Team2|2");
        Assert.assertEquals(2, t.getTeams().size());
    }

    @Test
    public void addGame() {
        Tournament t = new Tournament();
        t.addTeam("Team1|1");
        Assert.assertEquals(1, t.getTeams().size());
        t.addTeam("Team2|2");
        Assert.assertEquals(2, t.getTeams().size());
        t.addGame("1|2");
        Assert.assertEquals("Team - Team1 VS  Team - Team2 : The Winner is : Team1", t.getGameResult());
    }
}