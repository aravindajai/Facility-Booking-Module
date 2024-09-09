## Facility-Booking-Module
# This Python code represents a facility booking module that allows users to book different facilities at specific time slots. 
 Here's an explanation of the code:

The code begins by importing the datetime module from the Python standard library. This module is used for working with dates and times.

The code defines a class called Facility which represents a facility that can be booked. It has the following methods and attributes:

__init__(self, name, rates): This is the constructor method that initializes a Facility object. It takes a facility name and a list of rates as parameters and sets the name, rates, and bookings attributes.
book(self, start_time, end_time): This method allows booking the facility for a given time slot. It checks if the facility is already booked during the specified time slot by iterating through the existing bookings. If the facility is available, it calculates the booking amount based on the rates and updates the bookings list. The method returns a tuple indicating the success of the booking and the booking amount.
The code defines another class called FacilityBookingModule which manages multiple facilities and their bookings. It has the following methods and attributes:

__init__(self): This is the constructor method that initializes a FacilityBookingModule object. It sets the facilities attribute as an empty list.
add_facility(self, facility): This method adds a facility to the list of facilities managed by the module.
book_facility(self, facility_name, date, start_time, end_time): This method allows booking a facility by searching for the facility with a matching name and invoking its book method with the provided time slot. It returns the result of the booking attempt.
The code creates two instances of the Facility class: clubhouse and tennis_court, representing different facilities. Each facility is initialized with a name and a list of rates specifying the available time slots and their corresponding rates.

An instance of the FacilityBookingModule class, named booking_module, is created. The clubhouse and tennis_court facilities are added to the module using the add_facility method.

The code performs several bookings using the book_facility method of the booking_module. Each booking attempt is printed to the console.

The output of the code will depend on the availability and existing bookings of the facilities. The printed output shows whether each booking was successful and, if so, the corresponding booking amount. If a booking fails due to a time slot conflict, the output will indicate the failure reason.
