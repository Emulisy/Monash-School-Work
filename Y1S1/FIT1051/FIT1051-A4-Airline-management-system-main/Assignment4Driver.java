//driver class that shows user interface
public class Assignment4Driver {
    public static void main(String[] args) {
        System.out.println("Welcome to BunnyAirways Airline System!");
        boolean exit = false;
        while (!exit) { //while not select choice 7
            System.out.println("""
                    Menu:\
                    
                    1. Register a new customer.\
                    
                    2. Add a new flight to the system.\
                    
                    3. Book a flight ticket.\
                    
                    4. View all bookings and earned points for a specific customer.\
                    
                    5. Generate daily report.\
                    
                    6. Generate monthly report.\
                    
                    7. Exit the system.\
                    
                    Enter your choice:\s""");
            int choice = Validation.getInt();
            switch (choice) {
                case 1:
                    String email;
                    //validate email
                    do {
                        System.out.println("Please enter email address: ");
                        email = Validation.getString();
                        if (!Validation.validateEmail(email)) {
                            System.out.println("Invalid email address, please try again");
                        }
                    } while (!Validation.validateEmail(email));
                    //check if the email is used
                    if (!AirlineSystem.getCustomers().isEmpty()) {
                        for (Customer customer : AirlineSystem.getCustomers()) {
                            if (customer.getEmail().equals(email)) {
                                System.out.println("Email is already registered, returning to menu...");
                            }
                        }
                    }
                    else {
                        AirlineSystem.addCustomer(email);
                        System.out.println("Customer has been registered successfully");
                    }
                    break;
                case 2:
                    AirlineSystem.addFlight();
                    break;
                case 3:
                    if (AirlineSystem.getCustomers().isEmpty()) {
                        System.out.println("No customer in system, returning to menu...");
                    }
                    else {
                        System.out.println("Please enter your email: ");
                        String email3 = Validation.getString();
                        Customer customer3 = AirlineSystem.getCustomerByEmail(email3);
                        if (customer3 == null) {
                            System.out.println("Customer not found, returning to menu...");
                        }
                        else {
                            customer3.bookTickets();
                        }
                    }
                    break;
                case 4:
                    if (AirlineSystem.getCustomers().isEmpty()) {
                        System.out.println("No customer in system, returning to menu...");
                    }
                    else {
                        System.out.println("Please enter your email: ");
                        String email4 = Validation.getString();
                        Customer customer4 = AirlineSystem.getCustomerByEmail(email4);
                        if (customer4 == null) {
                            System.out.println("Customer not found, returning to menu...");
                        } else {
                            if (customer4.getTickets() != null) {
                                System.out.println("Bookings: ");
                                for (Ticket tickets : customer4.getTickets()) {
                                    System.out.println(tickets);
                                }
                                System.out.println("Earned points: " + customer4.getLoyaltyPoints());
                            } else {
                                System.out.println("No booking records found");
                            }
                        }
                    }
                    break;
                case 5:
                    AirlineSystem.dailyReport();
                    break;
                case 6:
                    AirlineSystem.monthlyReport();
                    break;
                case 7:
                    System.out.println("Thank you for using BunnyAirways Airline System!" + "\nExiting...");
                    exit = true;
                    break;
                default:
                    System.out.println("Invalid choice, please try again");
                    break;
            }
        }
    }
}
