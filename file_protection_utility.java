import java.io.*;
import java.nio.file.*;
import java.util.Base64;

public class FileProtectionUtility {

    // Protect file by encoding content
    public static void protectFile(String inputFile, String protectedFile) {
        try {
            String content = Files.readString(Paths.get(inputFile));

            String encodedContent =
                    Base64.getEncoder().encodeToString(content.getBytes());

            Files.writeString(Paths.get(protectedFile), encodedContent);

            System.out.println("File protected successfully!");
            System.out.println("Protected file saved as: " + protectedFile);

        } catch (IOException e) {
            System.out.println("Error while protecting file: " + e.getMessage());
        }
    }

    // Restore file by decoding content
    public static void restoreFile(String protectedFile, String restoredFile) {
        try {
            String encodedContent =
                    Files.readString(Paths.get(protectedFile));

            byte[] decodedBytes =
                    Base64.getDecoder().decode(encodedContent);

            String originalContent = new String(decodedBytes);

            Files.writeString(Paths.get(restoredFile), originalContent);

            System.out.println("File restored successfully!");
            System.out.println("Restored file saved as: " + restoredFile);

        } catch (IOException e) {
            System.out.println("Error while restoring file: " + e.getMessage());
        }
    }

    public static void main(String[] args) {

        String inputFile = "input.txt";
        String protectedFile = "protected.txt";
        String restoredFile = "restored.txt";

        protectFile(inputFile, protectedFile);
        restoreFile(protectedFile, restoredFile);
    }
}
