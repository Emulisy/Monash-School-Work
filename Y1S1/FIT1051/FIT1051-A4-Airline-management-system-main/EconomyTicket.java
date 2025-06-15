//economy class ticket
public class EconomyTicket extends Ticket
{
    public EconomyTicket(ClassType classType, Customer customer, Flight flight)
    {
        super(classType, customer, flight);
        this.price = flight.getStandardFare();
        this.ticketID = flight.getFlightID() + "E" + (flight.getTotalEconomySeats() - flight.getAvailableEconomySeats());
        customer.setLoyaltyPoints(15);
        flight.addTotalFare(this.price);
    }
}
