import java.util.Scanner;

public class LoginAttemptControlSystem {

    private static final String USERNAME = "admin";
    private static final String PASSWORD = "Secure123";
    private static final int MAX_ATTEMPTS = 3;
    private static final int LOCK_TIME = 30; // seconds

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int attempts = 0;

        while (true) {

            System.out.print("Enter Username: ");
            String username = sc.nextLine();

            System.out.print("Enter Password: ");
            String password = sc.nextLine();

            if (username.equals(USERNAME) && password.equals(PASSWORD)) {
                System.out.println("\nLogin Successful!");
                System.out.println("Welcome, " + username + "!");
                break;
            } else {
                attempts++;
                System.out.println("Incorrect Username or Password.");

                int remaining = MAX_ATTEMPTS - attempts;

                if (remaining > 0) {
                    System.out.println("Remaining Attempts: " + remaining);
                }

                if (attempts >= MAX_ATTEMPTS) {
                    System.out.println("\nToo many failed attempts!");
                    System.out.println("Account Locked for " + LOCK_TIME + " seconds.");

                    try {
                        for (int i = LOCK_TIME; i > 0; i--) {
                            System.out.print("\rTry again in: " + i + " seconds ");
                            Thread.sleep(1000);
                        }
                    } catch (InterruptedException e) {
                        System.out.println("\nTimer Interrupted.");
                    }

                    System.out.println("\n\nAccount Unlocked. Please Login Again.");
                    attempts = 0;
                }
            }
        }

        sc.close();
    }
}
