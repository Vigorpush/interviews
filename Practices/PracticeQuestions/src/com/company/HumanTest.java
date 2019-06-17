package com.company;

import org.junit.Assert;
import org.junit.Test;

public class HumanTest {

    @Test
    public void getName() {
        Human human = new Human("Tom", 1);
        Assert.assertEquals("Tom", human.getName());
    }

    @Test
    public void setName() {
        Human human = new Human("Tom", 1);
        Assert.assertEquals("Tom", human.getName());
        human.setName("Jerry");
        Assert.assertEquals("Jerry", human.getName());
    }

    @Test
    public void getId() {
        Human human = new Human("Tom", 1);
        Assert.assertEquals(1, human.getId());
    }

    @Test
    public void setId() {
        Human human = new Human("Tom", 1);
        Assert.assertEquals(1, human.getId());
        human.setId(2);
        Assert.assertEquals(2, human.getId());
    }
}