package com.company;

import java.io.BufferedWriter;
import java.io.FileWriter;

/**
 * This class will persist date by given information
 */
public class DataSaver {
    /**
     * Save given string information into a file.
     *
     * @param dataToSave string
     *                   It will output a out.txt file which contains given information
     */
    public void saveData(String dataToSave) {
        try {
            FileWriter fstream = new FileWriter(System.currentTimeMillis() + "out.txt");
            BufferedWriter out = new BufferedWriter(fstream);
            out.write(dataToSave);
            out.close();
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
