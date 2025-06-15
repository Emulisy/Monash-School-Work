import java.util.Scanner;
import java.time.LocalDate;

//utility class that contains methods for getting and validating user inputs
public class Validation
{
    private static final Scanner scanner = new Scanner(System.in);

    //get a string input
    public static String getString(){
        String inputString;
        do {
            inputString =  scanner.nextLine();
            if(inputString.isBlank()){
                System.out.println("Invalid input, please try again");
            }
        }while(inputString.isBlank());
        return inputString;
    }

    //get an integer input and validate
    public static int getInt() {
        boolean validInput = false;
        int number = 0;

        while (!validInput) {
            try {
                number = Integer.parseInt(scanner.nextLine());
                validInput = true;
            } catch (Exception e) {
                System.out.println("Invalid input. Please enter a valid number.");
            }
        }
        return number;
    }

    //get double input
    public static double getDouble() {
        double number = 0.0;
        boolean validInput = false;

        while (!validInput) {
            try {
                number = Double.parseDouble(scanner.nextLine());
                validInput = true;
            } catch (Exception e) {
                System.out.println("Invalid input. Please enter a valid number: ");
            }
        }
        return number;
    }

    //get a valid date input
    public static String getDate(){
        String date = "";
        boolean validDate = false;

        while(!validDate) {
            System.out.println("Please enter a month");
            int month = Validation.getInt();
            System.out.println("Please enter a day");
            int day = Validation.getInt();
            try {
                LocalDate.of(2000, month, day); //raise an exception if the date is invalid
                date = month + "-" + day;
                validDate = true;
            } catch (Exception e) {
                System.out.println("Invalid input. Please enter a valid date.");
            }
        }
        return date;
    }

    //validate email input
    public static boolean validateEmail(String email) {
        boolean isValid;
        String[] parts = email.split("@");
        //there should be only one "@" and there should be letters before and after the "@"
        isValid = parts.length == 2 && !parts[0].isEmpty() && !parts[1].isEmpty();
        return isValid;
    }

}
