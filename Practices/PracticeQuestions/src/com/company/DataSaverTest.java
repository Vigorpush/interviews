package com.company;


import org.junit.After;
import org.junit.Assert;
import org.junit.Test;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class DataSaverTest {

    @After
    public void tearDown() throws IOException {
        Path currentRelativePath = Paths.get("");
        Files.list(currentRelativePath).filter(p -> p.toString().contains("out.txt")).forEach((p) -> {
            try {
                Files.deleteIfExists(p);
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }

    @Test
    public void saveData() throws IOException {
        Path currentRelativePath = Paths.get("");
        int count = (int) Files.list(currentRelativePath).count();
        int afterCount = 0;
        DataSaver dataSaver = new DataSaver();
        dataSaver.saveData("Test");
        afterCount = (int) Files.list(currentRelativePath).count();
        Assert.assertEquals(1, (afterCount - count));
    }
}