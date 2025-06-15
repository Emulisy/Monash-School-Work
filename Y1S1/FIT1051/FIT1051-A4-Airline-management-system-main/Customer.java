import java.util.ArrayList;

//contains the information and method of a customer
public class Customer
{
    private String name;
    private String customerID;
    private String email;
    private ArrayList<Ticket> tickets;
    private int loyaltyPoints;

    //constructor with email input
    public Customer(String email) {
        System.out.println("Please enter name: ");
        this.name = Validation.getString();
        this.email = email;
        this.customerID = "CID" + (AirlineSystem.getNumberOfCustomers()+1);
        //assign ID automatically according to size of customers in the system
        this.loyaltyPoints = 0;
        this.tickets = new ArrayList<>();
    }

//getters and setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCustomerID() {
        return customerID;
    }

    public void setCustomerID(String customerID) {
        this.customerID = customerID;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getLoyaltyPoints() {
        return loyaltyPoints;
    }

    public void setLoyaltyPoints(int loyaltyPoints)
    {
        this.loyaltyPoints += loyaltyPoints;
    }

    public void addTickets(Ticket ticket){
        this.tickets.add(ticket);
    }

    public ArrayList<Ticket> getTickets() {
        return tickets;
    }

    //book a ticket
    public void bookTickets()
    {
        //if there are no flights in airline system
        if (AirlineSystem.getFlights().isEmpty()) {
            System.out.println("No flights in system.");
        }
        else
        {
            //input flight information
            System.out.println("Please select starting point: ");
            String startingPoint = Validation.getString();
            System.out.println("Please select destination: ");
            String destination = Validation.getString();
            String date = Validation.getDate();
            //search eligible flights
            ArrayList<Flight> selectedFlights = AirlineSystem.getFlight(startingPoint,destination,date);
            //if no flights suffice the requirements
            if(selectedFlights.isEmpty()){
                System.out.println("No flights available");
            }
            //if found available flights
            else{
                System.out.println("Flights found: ");
                int index = 0;
                for (Flight flight : selectedFlights) {
                    index++;
                    System.out.println(index + ". " + flight.getFlightID() + " Standard fare: " + flight.getStandardFare());
                }

                //choose flight
                int flightChoice = 0;
                do {
                    System.out.println("Please select flight(1,2...): ");
                    flightChoice = Validation.getInt();
                    if(flightChoice < 1 && flightChoice >= selectedFlights.size()){
                        System.out.println("Invalid flight choice, please try again");
                    }
                }while(flightChoice < 1 && flightChoice >= selectedFlights.size());
                Flight selectedFlight = selectedFlights.get(flightChoice-1);

                //select class
                boolean validClass = false;
                int classChoice;
                String selectedClass = "";
                while(!validClass){
                    System.out.println("Please select class(1,2,3): ");
                    int classTypeIndex = 0;
                    for(ClassType classType : ClassType.values()){
                        classTypeIndex++;
                        System.out.println(classTypeIndex + ". " + classType);
                    }
                    classChoice = Validation.getInt();
                    switch(classChoice){
                        case 1:
                            selectedClass = "Economy";
                            validClass = true;
                            break;
                        case 2:
                            selectedClass = "Business";
                            validClass = true;
                            break;
                        case 3:
                            selectedClass = "FirstClass";
                            validClass = true;
                            break;
                        default:
                            System.out.println("Invalid class, please try again");
                            break;
                    }
                }
                //create tickets if seat is available
                switch(selectedClass){
                    case "Economy":
                        if(selectedFlight.getAvailableEconomySeats() == 0){
                            System.out.println("No available economy seats, returning to menu...");
                        }
                        else{
                            Ticket e = new EconomyTicket(ClassType.Economy,this,selectedFlight);
                            selectedFlight.subAvailableEconomySeats(); //substitute 1 from available seats
                            System.out.println("You have booked an economy ticket for " + this.name);
                        }
                        break;
                    case "Business":
                        if(selectedFlight.getAvailableBusinessSeats() == 0){
                            System.out.println("No available business seats, returning to menu...");
                        }
                        else {
                            Ticket b = new BusinessTicket(ClassType.Business, this, selectedFlight);
                            selectedFlight.subAvailableBusinessSeats();
                            System.out.println("You have booked a business ticket for " + this.name);
                        }
                        break;
                    case "FirstClass":
                        if(selectedFlight.getAvailableFirstClassSeats() == 0){
                            System.out.println("No available first class seats, returning to menu...");
                        }
                        else {
                            Ticket f = new FirstClassTicket(ClassType.FirstClass, this, selectedFlight);
                            selectedFlight.subAvailableFirstClassSeats();
                            System.out.println("You have booked a first class ticket for " + this.name);
                        }
                        break;
                }
            }
        }
    }
}
