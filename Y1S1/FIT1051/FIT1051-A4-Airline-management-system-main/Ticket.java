//abstract class of tickets
public abstract class Ticket {
    protected ClassType classType;
    protected String ticketID;
    protected Customer customer;
    protected double price;
    protected Flight flight;

    public Ticket(ClassType classType, Customer customer, Flight flight)
    {
        this.classType = classType;
        this.customer = customer;
        this.flight = flight;
        AirlineSystem.addTickets(this);//every time a ticket is created it is added to customer and system
        customer.addTickets(this);
    }

    //return the tickets information
    public String toString(){
        return "Flight: " + flight.getFlightID() + "\nClass type: " + this.classType;
    }


}
