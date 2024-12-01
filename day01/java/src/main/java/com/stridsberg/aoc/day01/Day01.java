package com.stridsberg.aoc.day01;

import org.apache.commons.io.Charsets;
import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day01 {

    private record SortedLists(List<Integer> left, List<Integer> right) {

    }

    private SortedLists getSortedLists(String input) throws IOException {
        String s = FileUtils.readFileToString(new File(input), StandardCharsets.UTF_8);
        String t = s.replace("   ", " ");
        List<Integer> ll = new ArrayList<>();
        List<Integer> rl = new ArrayList<>();
        for (String line : t.split("\n")) {
            String[] nums =line.split(" ");
            ll.add(Integer.parseInt(nums[0]));
            rl.add(Integer.parseInt(nums[1]));
        }
        return new SortedLists(ll.stream().sorted().toList(), rl.stream().sorted().toList());
    }


    public void part1(String input) throws IOException {
     SortedLists sortedLists = getSortedLists(input);
     List<Integer> distances = new ArrayList<>();
     for (int i = 0; i < sortedLists.left().size(); i++) {
         int distance;
         if(sortedLists.left().get(i) > sortedLists.right().get(i)) {
             distance = sortedLists.left().get(i) - sortedLists.right().get(i);
         } else {
             distance = sortedLists.right().get(i) - sortedLists.left().get(i);
         }
         distances.add(distance);
     }
        System.out.println(distances.stream().reduce(0, Integer::sum));

    }

    public void part2(String input) throws IOException {
        SortedLists sortedLists = getSortedLists(input);
        List<Integer> scoreList = new ArrayList<>();
        for (int i = 0; i < sortedLists.left().size(); i++) {
            int currNum = sortedLists.left().get(i);
            int occurrences = Collections.frequency(sortedLists.right(), currNum);
            scoreList.add(currNum * occurrences);
        }
        System.out.println(scoreList.stream().reduce(0, Integer::sum));
    }
}
