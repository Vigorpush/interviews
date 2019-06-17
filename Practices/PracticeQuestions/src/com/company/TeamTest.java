package com.company;

import org.junit.Assert;
import org.junit.Test;

public class TeamTest {

    @Test
    public void getTeamName() {
        Team t1 = new Team("Test", 1);
        Assert.assertEquals("Test", t1.getTeamName());
    }

    @Test
    public void setTeamName() {
        Team t1 = new Team("Test", 1);
        t1.setTeamName("Test1");
        Assert.assertEquals("Test1", t1.getTeamName());
    }

    @Test
    public void getTeamId() {
        Team t1 = new Team("Test", 1);
        Assert.assertEquals(1, t1.getTeamId());
    }

    @Test
    public void setTeamId() {
        Team t1 = new Team("Test", 1);
        t1.setTeamId(2);
        Assert.assertEquals(2, t1.getTeamId());
    }

    @Test
    public void getCoach() {
        Team t1 = new Team("Test", 1);
        Coach coach = new Coach("Tom", 123);
        t1.setCoach(coach);
        Assert.assertEquals(123, t1.getCoach().getId());
    }

    @Test
    public void setCoach() {
        Team t1 = new Team("Test", 1);
        Coach coach = new Coach("Tom", 123);
        t1.setCoach(coach);
        Coach coach1 = new Coach("Jenny", 1234);
        t1.setCoach(coach1);
        Assert.assertEquals(1234, t1.getCoach().getId());
    }

    @Test
    public void addNewPlayer() {
        Team t1 = new Team("Test", 1);
        Player player1 = new Player("Vigor", 1);
        t1.addNewPlayer(player1);
        Assert.assertEquals(1, t1.getPlayers().size());
        Player player2 = new Player("Selina", 2);
        t1.addNewPlayer(player2);
        Assert.assertEquals(2, t1.getPlayers().size());
    }

    @Test
    public void addDuplicatePlayer() {
        Team t1 = new Team("Test", 1);
        Player player1 = new Player("Vigor", 1);
        t1.addNewPlayer(player1);
        Assert.assertEquals(1, t1.getPlayers().size());
        Player player2 = new Player("Selina", 1);
        t1.addNewPlayer(player2);
        Assert.assertEquals(1, t1.getPlayers().size());
    }
}