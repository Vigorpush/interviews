package com.company;

import javafx.util.Pair;

import java.util.LinkedList;
import java.util.Scanner;

/**
 * Tournament Class
 */
public class Tournament {

    private LinkedList<Game> gameResult = new LinkedList<Game>();
    private LinkedList<Team> teams = new LinkedList<Team>();
    private Scanner sc = new Scanner(System.in);

    /**
     * Get Teams in linkedlist
     *
     * @return teams Linkedlist
     */
    public LinkedList<Team> getTeams() {
        return teams;
    }

    /**
     * Report all game results from a tournament
     *
     * @return game result String
     */
    public String getGameResult() {
        StringBuilder sb = new StringBuilder("");
        if (this.gameResult.size() < 1) {
            return "No Match Result";
        }
        for (Game g : this.gameResult) {
            sb.append("Team - ")
                    .append(g.getOpponents().getKey().getTeamName())
                    .append(" VS  Team - ")
                    .append(g.getOpponents().getValue().getTeamName())
                    .append(" : The Winner is : ")
                    .append(g.getWinner().getTeamName());
        }
        return sb.toString();
    }

    /**
     * Print all game results from a tournament on console
     */
    public void printResults() {
        System.out.println(this.getGameResult());
    }

    /**
     * Helper function which shows the existing team
     */
    public String getAllTeamsInformation() {
        StringBuilder sb = new StringBuilder("");
        if (this.teams.size() < 1) {
            System.out.println("No team to show");
            return "There is no team to show";
        }
        sb.append("Existing Team are(is) : \n");
        for (Team t : this.teams) {
            sb.append("Team Name : ").append(t.getTeamName())
                    .append(" Team id  : ")
                    .append(t.getTeamId())
                    .append("\n");
        }
        return sb.toString();
    }

    /**
     * Method which allow user to add a player to a team
     *
     * @param input string It should be empty "" by default, it only use for testing
     */
    public void addPlayer(String input) {
        if (this.teams == null || this.teams.size() < 1) {
            System.out.println("Please add Team first ! ");
            return;
        }
        String playerName;
        int playerId;
        int teamId;
        if (!input.isEmpty()) {
            // add this block for testing purpose
            String[] array = input.split("\\|");
            if (array.length < 2) return;
            playerName = array[0];
            playerId = Integer.parseInt(array[1]);
            teamId = Integer.parseInt(array[2]);
        } else {
            System.out.println("Please enter player's name : ");
            playerName = sc.next(); // get string
            System.out.println("Please enter player's id : ");
            playerId = sc.nextInt(); // get integer
            System.out.println("Please enter the team id : \n" + this.getAllTeamsInformation());
            teamId = sc.nextInt(); // get integer
        }
        for (Team team : this.teams) {
            if (team.getTeamId() == teamId) {
                Player player = new Player(playerName, playerId);
                team.addNewPlayer(player);
                System.out.println("Player created! ");
                return;
            }
        }
        System.out.println("Player creation failed. Can not find the team");
    }
    /**
     * Method which allow user to add a coach to a team
     *
     * @param input string It should be empty "" by default, it only use for testing
     */
    public void addCoach(String input) {
        if (this.teams == null || this.teams.size() < 1) {
            System.out.println("Please add Team first ! ");
            return;
        }
        String coachName;
        int coachId;
        int teamId;
        if (!input.isEmpty()) {
            // add this block for testing purpose
            String[] array = input.split("\\|");
            if (array.length < 2) return;
            coachName = array[0];
            coachId = Integer.parseInt(array[1]);
            teamId = Integer.parseInt(array[2]);
        } else {
            System.out.println("Please enter coach's name : ");
            coachName = sc.next();
            System.out.println("Please enter coach's id : ");
            coachId = sc.nextInt();
            System.out.println("Please enter the team id : \n" + this.getAllTeamsInformation());
            teamId = sc.nextInt();
        }
        for (Team team : this.teams) {
            if (team.getTeamId() == teamId) {
                Coach coach = new Coach(coachName, coachId);
                team.setCoach(coach);//when we add coach, it will replace the original coach to new one
                System.out.println("Coach Created ! ");
                return;
            }
        }
        System.out.println("Coach creation failed. Can not find the team");
    }

    /**
     * Method which allow user to add a team
     *
     * @param input string It should be empty "" by default, it only use for testing
     */
    public void addTeam(String input) {
        String teamName;
        int teamId;
        if (!input.isEmpty()) {
            // add this block for testing purpose
            String[] array = input.split("\\|");
            if (array.length < 1) return;
            teamName = array[0];
            teamId = Integer.parseInt(array[1]);
        } else {
            System.out.println("Please enter team's name : ");
            teamName = sc.next();
            System.out.println("Please enter the team id : ");
            teamId = sc.nextInt();
        }
        if (this.teams.size() < 1) {
            this.teams.add(new Team(teamName, teamId));
            return;
        }
        for (Team team : this.teams) {
            if (team.getTeamId() == teamId) {
                System.out.println("Failed to add Team, Team id should be Unique");
                return;
            }
        }
        this.teams.add(new Team(teamName, teamId));
        System.out.println("Team created ! ");
    }
    /**
     * Method which allow user to add a game match by given 2 teamId (The first team is winner)
     *
     * @param input string It should be empty "" by default, it only use for testing
     */
    public void addGame(String input) {
        if (this.teams.size() < 2) {
            System.out.println("It should be more 2 teams, currently the amount of teams is " + this.teams.size());
            return;
        }
        int team1Id;
        int team2Id;
        if (!input.isEmpty()) {
            // add this block for testing purpose
            String[] array = input.split("\\|");
            if (array.length < 1) return;
            team1Id = Integer.parseInt(array[0]);
            team2Id = Integer.parseInt(array[1]);
        } else {
            System.out.println("Please enter id of the first (Winner) team : (" + this.getAllTeamsInformation() + ")");
            team1Id = sc.nextInt();
            System.out.println("Please enter id of the second team : ");
            team2Id = sc.nextInt();
        }
        if (team1Id == team2Id) return;
        boolean found = false;
        Team fristTeam = null;
        for (Team team1t : this.teams) {
            if (team1t.getTeamId() == team1Id) {
                fristTeam = team1t;
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("Can not found given team id");
            return;
        }
        found = false;
        Team secondTeam = null;
        for (Team team2t : this.teams) {
            if (team2t.getTeamId() == team2Id) {
                secondTeam = team2t;
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("Can not found given team id");
            return;
        }
        Pair<Team, Team> opponents = new Pair<>(fristTeam, secondTeam);
        Game game = new Game(opponents, fristTeam);
        this.gameResult.add(game);
        System.out.println("Game result created ! ");
    }

    /**
     * A method which run Tournament
     */
    public void run() {
        Scanner sc;
        String line;
        while (true) {
            try {
                System.out.println(
                        "Enter 'e' to exit \n"
                                + "Enter 's' to show game result \n"
                                + "Enter 'addcoach' to add coach \n"
                                + "Enter 'addplayer' to add player \n"
                                + "Enter 'addteam' to add team \n"
                                + "Enter 'addGame' to add a game \n"
                                + "Enter 'save' to save report to a file \n"
                );
                sc = new Scanner(System.in);
                line = sc.next();
                switch (line.toLowerCase()) {
                    case "save":
                        DataSaver dataSaver = new DataSaver();
                        dataSaver.saveData(this.getGameResult());
                        break;
                    case "addplayer":
                        this.addPlayer("");
                        break;
                    case "addcoach":
                        this.addCoach("");
                        break; //when it fail to find the team, it will let user do it over.
                    case "addteam":
                        this.addTeam("");
                        break; //when it fail to find the team, it will let user do it over.
                    case "addgame":
                        this.addGame("");
                        break; //when it fail to find the team, it will let user do it over.
                    case "e":
                        System.out.println("End of the Tournament .... ");
                        return;
                    case "s":
                        this.printResults();
                        break;
                    default:
                        System.out.println("Invalid Command, please try again");
                        break;
                }
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }


    public static void main(String arg[]) {
        Tournament t = new Tournament();
        t.run();
    }
}
