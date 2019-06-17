package com.company;

import java.util.LinkedList;

public class Team {

    private String teamName;
    private int teamId;
    private Coach coach;
    private LinkedList<Player> squads = new LinkedList<>();

    /**
     * A Constructor which uses String teamName, int teamId, Coach coach, LinkedList<Player> squads
     * to construct a team object
     *
     * @param teamName String
     * @param teamId   int
     * @param coach    Coach
     * @param squads   LinkedList<Player>
     */
    public Team(String teamName, int teamId, Coach coach, LinkedList<Player> squads) {
        this.teamName = teamName;
        this.teamId = teamId;
        this.coach = coach;
        this.squads = squads;
    }

    /**
     * A Simple Constructor which uses String teamName, int teamId, Coach coach, LinkedList<Player> squads
     *
     * @param teamName String
     * @param teamId   int
     */
    public Team(String teamName, int teamId) {
        this.teamName = teamName;
        this.teamId = teamId;
    }

    /**
     * A method which could Get Team name
     *
     * @return teamName String
     */
    public String getTeamName() {
        return teamName;
    }

    /**
     * A method which could set Team name
     *
     * @param teamName String
     */
    public void setTeamName(String teamName) {
        this.teamName = teamName;
    }

    /**
     * A method which could Get Team ID
     *
     * @return teamId int
     */
    public int getTeamId() {
        return teamId;
    }

    /**
     * A method which could set Team ID
     *
     * @param teamId int
     */
    public void setTeamId(int teamId) {
        this.teamId = teamId;
    }

    /**
     * A method which could Get coach
     *
     * @return coach Coach
     */
    public Coach getCoach() {
        return coach;
    }

    /**
     * A method which could set coach
     *
     * @param coach Coach
     */
    public void setCoach(Coach coach) {
        this.coach = coach;
    }

    /**
     * A method which could add a new player, it will only add when the play id is unique
     *
     * @param player Player
     */
    public void addNewPlayer(Player player) {
        if (this.getPlayers().size() < 1) {
            this.squads.add(player);
            return;
        }
        for (Player p : this.getPlayers()) {
            if (player.getId() == p.getId()) {
                return;
            }
        }
        this.squads.add(player);
    }

    /**
     * A method which could Get Player list
     *
     * @return squads LinkedList<Player>
     */
    public LinkedList<Player> getPlayers() {
        return this.squads;
    }
}