package com.company;


import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        DataSaverTest.class,
        GameTest.class,
        HumanTest.class,
        TeamTest.class,
        TournamentTest.class
})

public class TestRunner {
    // the class remains empty,
    // used only as a holder for the above annotations
}