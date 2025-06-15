public class FirstClassTicket extends Ticket
{
    public FirstClassTicket(ClassType classType, Customer customer, Flight flight)
    {
        super(classType, customer, flight);
        this.price = flight.getStandardFare() * 4;
        this.ticketID = flight.getFlightID() + "F" + (flight.getTotalEconomySeats() - flight.getAvailableEconomySeats());
        customer.setLoyaltyPoints(50);
        flight.addTotalFare(this.price);
    }
}
