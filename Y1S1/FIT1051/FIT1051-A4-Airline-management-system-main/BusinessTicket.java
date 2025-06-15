//Business class tickets
public class BusinessTicket extends Ticket
{
    public BusinessTicket(ClassType classType, Customer customer, Flight flight)
    {
        super(classType, customer, flight);
        this.price = flight.getStandardFare() * 2;
        this.ticketID = flight.getFlightID() + "B" + (flight.getTotalEconomySeats() - flight.getAvailableEconomySeats());
        customer.setLoyaltyPoints(30);
        flight.addTotalFare(this.price);
    }
}
