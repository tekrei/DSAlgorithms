package net.tekrei;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Utilities {

    private static Random randomGenerator = new Random();

    @SuppressWarnings("unchecked")
    public static List<Integer> cloneList(List<Integer> list) {
        return (List<Integer>) ((ArrayList<Integer>) list).clone();
    }

    public static List<Integer> generateIntegerList(int size) {
        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < size; i++) {
            list.add(randomInt(size * size));
        }
        return list;
    }

    public static Integer randomInt(int upper) {
        return randomGenerator.nextInt(upper);
    }

}