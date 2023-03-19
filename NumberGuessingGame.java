import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {
    public static void main(String[] args) {
        Random random = new Random();
        int hiddenNumber = random.nextInt(20) + 1; // Generate a random number between 1 and 20
        Scanner scanner = new Scanner(System.in);
        int guess;
        int numGuesses = 0;
        System.out.println(" The number guessing game ");
        do {
            System.out.print("Enter your guess (1-20): ");
            guess = scanner.nextInt();
            numGuesses++;
            if (guess < hiddenNumber) {
                System.out.println("Low!");
            } else if (guess > hiddenNumber) {
                System.out.println("High!");
            }
        } while (guess != hiddenNumber);
        System.out.println("Congratulations, you guessed the number in " + numGuesses + " guesses");
    }
}
