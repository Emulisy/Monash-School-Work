
/**
 * FIT1051 Assignment two: Student class
 * @ author Ian Zhang (Zhang Yueling) 35545534
 */
public class Student {
    private String fullName;
    private String email;
    private int studentID;
    private String passWord;

    //constructors
    public Student()
    {
        fullName = "";
        email = "";
        studentID = 1000;
        passWord = "";
    }

    public Student(String fullName, String email, int studentID, String passWord)
    {
        this.fullName = fullName;
        this.email = email;
        this.studentID = studentID;
        this.passWord = passWord;
    }

    public String getFullName()
    {
        return fullName;
    }

    //getters and setters for each field
    public void setFullName(String fullName)
    {
        this.fullName = fullName;
    }

    public String getEmail()
    {
        return email;
    }

    public void setEmail(String email)
    {
        this.email = email;
    }

    public int getStudentID()
    {
        return studentID;
    }

    public void setStudentID(int studentID)
    {
        this.studentID = studentID;
    }

    public String getPassWord()
    {
        return passWord;
    }

    public void setPassWord(String passWord)
    {
        this.passWord = passWord;
    }

    //display method
    public String toString()
    {
        String string = ("Student ID: " + studentID
                + "\n" + "Name: " + fullName
                + "\n" + "Email address: " + email);
        return string;
    }
}
