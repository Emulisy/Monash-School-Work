//stores information and method of a flight
public class Flight {
    private String flightID;
    private String startingPoint;
    private String destination; //route of flight
    private int totalEconomySeats;
    private int totalBusinessSeats;
    private int totalFirstClassSeats;
    private double standardFare; //price of economy class ticket
    private double totalFare; // the total fare is added every time a new ticket is created
    private int availableEconomySeats;
    private int availableBusinessSeats;
    private int availableFirstClassSeats;
    private String date; // M-D format date

    //create a new flight
    public Flight()
    {
        //assign ID
        this.flightID = "BA" + String.format("%04d",AirlineSystem.getNumberOfFlights() + 1);

        //set route
        System.out.println("Please enter the starting point of the flight: ");
        this.startingPoint = Validation.getString();
        System.out.println("Please enter the destination of the flight: ");
        this.destination = Validation.getString();

        //set date
        this.date = Validation.getDate();

        //set the seats for each class, and initialize the available seats to total seats
        System.out.println("Please enter the total number of Economy Seats: ");
        this.totalEconomySeats = Validation.getInt();
        this.availableEconomySeats = this.totalEconomySeats;

        System.out.println("Please enter the total number of Business Seats: ");
        this.totalBusinessSeats = Validation.getInt();
        this.availableBusinessSeats = this.totalBusinessSeats;

        System.out.println("Please enter the total number of First Class Seats: ");
        this.totalFirstClassSeats = Validation.getInt();
        this.availableFirstClassSeats = this.totalFirstClassSeats;

        //set economy class ticket price
        System.out.println("Please enter the price of Standard Fare: ");
        this.standardFare = Validation.getDouble();
        this.totalFare = 0;

        System.out.println("You have created a new flight!");
        System.out.println(this);
    }

//getter and setter
    public int getAvailableFirstClassSeats() {
        return availableFirstClassSeats;
    }

    public void setAvailableFirstClassSeats(int availableFirstClassSeats) {
        this.availableFirstClassSeats = availableFirstClassSeats;
    }

    public int getAvailableBusinessSeats() {
        return availableBusinessSeats;
    }

    public void setAvailableBusinessSeats(int availableBusinessSeats) {
        this.availableBusinessSeats = availableBusinessSeats;
    }

    public int getAvailableEconomySeats() {
        return availableEconomySeats;
    }

    public void setAvailableEconomySeats(int availableEconomySeats) {
        this.availableEconomySeats = availableEconomySeats;
    }

    public double getTotalFare() {
        return totalFare;
    }

    public void addTotalFare(double Fare) {
        this.totalFare += Fare;
    }

    public int getTotalBusinessSeats() {
        return totalBusinessSeats;
    }

    public int getTotalFirstClassSeats() {
        return totalFirstClassSeats;
    }

    public int getTotalEconomySeats() {
        return totalEconomySeats;
    }

    public double getStandardFare() {
        return standardFare;
    }

    public String getFlightID() {
        return flightID;
    }


    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }

    public String getStartingPoint() {
        return startingPoint;
    }

    public void setStartingPoint(String startingPoint) {
        this.startingPoint = startingPoint;
    }

    public String getDate() {
        return date;
    }

    public int getTotalSeats(){
        return totalBusinessSeats + totalEconomySeats + totalFirstClassSeats;
    }

    public int getAvailableSeats(){
        return availableBusinessSeats + availableEconomySeats + availableFirstClassSeats;
    }

    //substitute the available seats by 1
    public void subAvailableEconomySeats(){
        this.availableEconomySeats -= 1;
    }

    public void subAvailableBusinessSeats(){
        this.availableBusinessSeats -= 1;
    }

    public void subAvailableFirstClassSeats(){
        this.availableFirstClassSeats -= 1;
    }

    //return information of the flight
    public String toString(){
        return "FlightID: " + this.flightID + "\nStarting point: " + this.startingPoint + "\nDestination: " + this.destination +
                "\nStandard fare for economy class: " + this.standardFare + "\nDate: " + this.date;
    }
}
