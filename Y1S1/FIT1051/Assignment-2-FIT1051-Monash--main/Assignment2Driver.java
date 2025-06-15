import java.util.ArrayList;
import java.util.Scanner;

/**
 * FIT1051 Assignment two: online course registration system
 * @ author Ian Zhang (Zhang Yueling) 35545534
 */
public class Assignment2Driver
{
    private static Scanner sc = new Scanner(System.in);
    private static ArrayList<Student> studentList = new ArrayList<>();
    private static int numberOfDeleted = 0;

    //main method
    public static void main(String[] args)
    {
        //main menu
        boolean exitMainMexu = false;
        while (!exitMainMexu)
        {
            System.out.println("""
                    Main Menu
                    1. Register a new student.
                    2. Login as an existing student
                    3. Exit system
                    """);
            System.out.println("Choose an option: ");
            int option = Integer.parseInt(sc.nextLine());
            Student newStudent = new Student();

            if (option == 1) //register new account
            {
                boolean emailIsValid = false;
                while (!emailIsValid) //asking for email address
                {
                    System.out.println("Please enter your email address: ");
                    String email = sc.nextLine();
                    for (Student student : studentList)
                    {
                        if (student.getEmail().equals(email))
                        {
                            System.out.println(student.getEmail() + " has been used, please try again.");
                        }
                    }
                    if (!validateEmail(email))
                    {
                        System.out.println("Invalid email address, please try again.");
                    }
                    else
                    {
                        newStudent.setEmail(email);
                        emailIsValid = true;
                    }
                }

                boolean passwordIsValid = false;
                while (!passwordIsValid) //set password
                {
                    System.out.println("Please set your password: ");
                    String passWord = sc.nextLine();
                    if (!validatePassword(passWord))
                    {
                        System.out.println("Invalid password, please try again.");
                    }
                    else
                    {
                        newStudent.setPassWord(passWord);
                        passwordIsValid = true;
                    }
                }
                System.out.println("Please enter your full name: ");//set name
                String fullName = sc.nextLine();
                newStudent.setFullName(fullName);
                int studentID = 1000 + studentList.size() + numberOfDeleted;//assign ID
                newStudent.setStudentID(studentID);
                studentList.add(newStudent);
                System.out.println("Registered successfully.");
            }

            else if (option == 2) //login in
            {
                if (studentList.isEmpty())
                {
                    System.out.println("No students registered.");
                }
                else
                {
                    boolean threeTimes = false;
                    for (int i = 2; i >= 0 && !threeTimes; i--)
                    {
                        boolean login = false;
                        Student targetStudent = new Student();
                        System.out.println("Please enter your email address: ");
                        String email = sc.nextLine();
                        System.out.println("Please enter your password: ");
                        String passWord = sc.nextLine();
                        for (Student student : studentList)
                        {
                            if (student.getPassWord().equals(passWord) && student.getEmail().equals(email))
                            {
                                String name = student.getFullName();
                                System.out.println("Welcome, " + name + "!");
                                login = true;
                                targetStudent = student;
                            }
                        }
                        if (login)
                        {
                            threeTimes = true;
                            goToStudentMenu(targetStudent);
                        }
                        else
                        {
                            System.out.println("Invalid password or email address. You have " + i + " " + (i == 1 ? "chance" : "chances") + " left.");
                        }
                    }
                    System.out.println("Returning to main menu.");
                }
            }

            else if (option == 3) //exit
            {
                System.out.println("You have exit the system.");
                exitMainMexu = true;
            }
        }
    }

    //execute studentMenu
    public static void goToStudentMenu(Student student)
    {
        boolean exit = false;
        while (!exit)
        {
            System.out.println("""
                    Student Menu:
                    1. View Student details
                    2. Change email address
                    3. Change password
                    4. Register for a course
                    5. Delete account
                    6. Log out
                    """);
            System.out.print("Choose an option: ");
            int option = Integer.parseInt(sc.nextLine());
            if (option == 1)//show account details
            {
                System.out.println(student.toString());
            }
            else if (option == 2)//change email
            {
                boolean emailIsValid = false;
                while (!emailIsValid)
                {
                    System.out.println("Enter your new email address: ");
                    String newEmail = sc.nextLine();
                    if (validateEmail(newEmail))
                    {
                        student.setEmail(newEmail);
                        System.out.println("Email updated");
                        emailIsValid = true;
                    }
                    else
                    {
                        System.out.println("Invalid email address, please try again.");
                    }
                }
            }
            else if (option == 3)//change password
            {
                boolean passwordIsValid = false;
                while (!passwordIsValid)
                {
                    System.out.println("Enter your new password: ");
                    String newPassWord = sc.nextLine();
                    if (validatePassword(newPassWord))
                    {
                        student.setPassWord(newPassWord);
                        System.out.println("Password updated");
                        passwordIsValid = true;
                    }
                    else
                    {
                        System.out.println("Invalid password, please try again.");
                    }
                }
            }
            else if (option == 4)//register course
            {
                    System.out.print("Enter course name to register: ");
                    String courseName = sc.nextLine();
                    System.out.println("Course '" + courseName + "' registered successfully.");
            }
            else if (option == 5)//delete account
            {
                    System.out.print("Delete your account(Y/N): ");
                    if (sc.nextLine().equals("Y"))
                    {
                        studentList.remove(student);
                        numberOfDeleted++;
                        System.out.println("Your account has been deleted.");
                        exit = true;
                    }
                    else
                    {
                        System.out.println("Your account has not been deleted.");
                    }
            }
            else if (option == 6)//log out
            {
                exit = true;
            }
        }
    }

    //check if the email is valid
    public static boolean validateEmail (String email)
    {
        boolean bool = false;
        if (email.contains("@"))
        {
            if(email.indexOf("@") != 0 && email.indexOf("@") != email.length() - 1)
            {
                bool = email.charAt(email.indexOf("@") - 1) != ' ' && email.charAt(email.indexOf("@") + 1) != ' ';
            }
        }
        return bool;
    }

    //check if the password is valid
    public static boolean validatePassword (String passWord)
    {
        boolean bool = false;
        if (passWord.length() >= 7)
        {
            boolean hasLower = false;
            boolean hasUpper = false;
            boolean hasSymbol = false;
            boolean hasNumber = false;
            for (int i = 0; i < passWord.length(); i++)
            {
                char ch = passWord.charAt(i);
                if (Character.isLowerCase(ch))
                {
                    hasLower = true;
                }
                else if (Character.isUpperCase(ch))
                {
                    hasUpper = true;
                }
                else if (Character.isDigit(ch))
                {
                    hasNumber = true;
                }
                else if (!Character.isDigit(ch) && !Character.isLetter(ch))
                {
                    hasSymbol = true;
                }
            }
            bool =  hasLower && hasUpper && hasSymbol && hasNumber;
        }
        return bool;
    }
}
