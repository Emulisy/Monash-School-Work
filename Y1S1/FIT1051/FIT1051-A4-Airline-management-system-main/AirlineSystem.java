import java.util.ArrayList;
//Airline system class 	Original report by ChatGPT: https://chatgpt.com/share/678dcf98-8eb0-8013-85ff-fc9cab0fa66f
//	Original news item: Medical Device IPOs Could Revive Health Tech Listingsthat stores information of customers, flights and tickets.
public class AirlineSystem
{
    private static ArrayList<Customer> customers = new ArrayList<>();
    private static ArrayList<Flight> flights = new ArrayList<>();
    private static ArrayList<Ticket> tickets = new ArrayList<>();

    //no need to create object of the class
    private AirlineSystem() {}

    //getter and setter
    public static  ArrayList<Customer> getCustomers() {
        return customers;
    }

    public static ArrayList<Flight> getFlights() {
        return flights;
    }

    public static ArrayList<Ticket> getTickets() {
        return tickets;
    }

    public static void addTickets(Ticket ticket) {
        tickets.add(ticket);
    }

    public static void addCustomers(Customer customer) {
        AirlineSystem.customers.add(customer);
    }

    public static void addFlights(Flight flight) {
        AirlineSystem.flights.add(flight);
    }

    //get the number of flights in the system
    public static int getNumberOfFlights()
    {
        int returnInt;
        if (flights == null){
            returnInt = 0;
        }
        else {
            returnInt = flights.size();
        }
        return returnInt;
    }

    //get the number of customers in the system
    public static int getNumberOfCustomers(){
        int returnInt;
        if (customers != null) {
            returnInt = customers.size();
        }
        else{
            returnInt = 0;
        }
        return returnInt;
    }

    //get the specific flights that has the same starting point, destination and date, return an arraylist of eligible flight
    public static ArrayList<Flight> getFlight(String startingPoint, String destination, String date){
        ArrayList<Flight> selectedFlights = new ArrayList<>();
        for(Flight flight:AirlineSystem.flights) {
            if (flight.getStartingPoint().equals(startingPoint) && flight.getDestination().equals(destination) && flight.getDate().equals(date)) {
                selectedFlights.add(flight);
            }
        }
        return selectedFlights;
    }

    //get the specific customer using ID
    public static Customer getCustomerByID(String customerID){
        Customer targetCustomer = null;
        for(Customer customer : customers){
            if (customer.getCustomerID().equals(customerID)){
                targetCustomer = customer;
            }
        }
        return targetCustomer;
    }

    //get the specific customer using email
    public static Customer getCustomerByEmail(String email){
        Customer targetCustomer = null;
        for(Customer customer : customers){
            if (customer.getEmail().equals(email)){
                targetCustomer = customer;
            }
        }
        return targetCustomer;
    }

    //create and add a flight to the system
    public static void addFlight(){
        Flight newFlight = new Flight();
        flights.add(newFlight);
    }

    //create and add a customer to the system
    public static void addCustomer(String email){
        Customer newCustomer = new Customer(email);
        customers.add(newCustomer);
    }

    //generate a daily report of the input date
    public static void dailyReport(){
        if(flights.isEmpty()){
            System.out.println("No flight in system.");
        }
        else {
            String date = Validation.getDate();
            System.out.println("Daily Report");
            int totalBookings = 0;
            double revenue = 0.0;
            int remainingSeats = 0;
            for (Flight flight : flights) {
                if (flight.getDate().equals(date)) {
                    remainingSeats += flight.getAvailableSeats();
                    revenue += flight.getTotalFare();
                    totalBookings += flight.getTotalSeats() - flight.getAvailableSeats();
                }
            }
            System.out.println("Date: " + date + "\nTotal Bookings: " + totalBookings + " tickets.\nRevenue: $" + revenue
                    + "\nRemaining Seats: " + remainingSeats);
        }
    }

    //generate a monthly report of the input month
    public static void monthlyReport(){
        int totalPassengersFlown = 0;
        double totalRevenue = 0;
        if(flights.isEmpty()) {
            System.out.println("No flight in system.");
        }
        else {
            System.out.println("Please input month(1-12): ");
            int month;
            do{
                month = Validation.getInt();
                if (month <= 0 && month > 12) {
                    System.out.println("Invalid month, please try again");
                }
            }while (month <= 0 && month > 12);
                System.out.println("Monthly report");
            for (Flight flight : flights) {
                String[] parts = flight.getDate().split("-");
                int flightMonth = Integer.parseInt(parts[0]);
                if (flights == null) {
                    System.out.println("No flights found");
                } else if (flightMonth == month) {
                    totalPassengersFlown += flight.getTotalSeats() - flight.getAvailableSeats();
                    totalRevenue += flight.getTotalFare();
                }
            }
            System.out.println("Total Passengers: " + totalPassengersFlown + "\nTotal Revenue: $" + totalRevenue);
        }
    }

}
