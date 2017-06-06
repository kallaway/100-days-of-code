# Code

## Day 1

import javax.naming.Context;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

/**
 * Created by dawid on 06.06.17.
 *
 * Project created for #100DaysOfCode challenge.
 */
 
 
 
 public class Main{
    public static void main(String[] args) {

        //ARRAYS

        //initialize
        Character[] ChallengeName = {'1','0','0','D','a','y','s',' ','O','f',' ','C','o','d','e'};
        String[] ChallengeName2 = {"100", "Days", "Of", "Code"};
        //traverse
        for(char znak : ChallengeName){
            System.out.println("Next char is: " + znak);
        }
        //traverse ascending
        Arrays.sort(ChallengeName);
        System.out.println("Ascending");
        for(char znak : ChallengeName){
            System.out.println("Next char is: " + znak);
        }
        //traverse descending
        Arrays.sort(ChallengeName, Collections.reverseOrder());
        System.out.println("Ascending");
        for(char znak : ChallengeName){
            System.out.println("Next char is: " + znak);
        }
        for(String slowo : ChallengeName2){
            System.out.println("Next word is: " + slowo);
        }
    }

}
