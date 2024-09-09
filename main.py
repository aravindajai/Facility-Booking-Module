from datetime import datetime

class Facility:
    def __init__(self, name, rates):
        self.name = name
        self.rates = rates
        self.bookings = []

    def book(self, start_time, end_time):
        # Check for overlapping bookings
        for booking in self.bookings:
            if start_time < booking['end_time'] and end_time > booking['start_time']:
                return False, 'Booking Failed, Already Booked'

        booking_amount = 0
        # Calculate the booking amount based on rates
        for rate in self.rates:
            if start_time >= rate['start_time'] and end_time <= rate['end_time']:
                booking_amount += (end_time - start_time).total_seconds() / 3600 * rate['rate']
                break
            elif start_time >= rate['start_time'] and end_time > rate['end_time']:
                booking_amount += (rate['end_time'] - start_time).total_seconds() / 3600 * rate['rate']
                start_time = rate['end_time']
            elif start_time < rate['start_time'] and end_time <= rate['end_time']:
                booking_amount += (end_time - rate['start_time']).total_seconds() / 3600 * rate['rate']
                end_time = rate['start_time']

        # Append the new booking
        self.bookings.append({
            'start_time': start_time,
            'end_time': end_time
        })

        return True, booking_amount


class FacilityBookingModule:
    def __init__(self):
        self.facilities = []

    def add_facility(self, facility):
        self.facilities.append(facility)

    def book_facility(self, facility_name, date, start_time, end_time):
        for facility in self.facilities:
            if facility.name.lower() == facility_name.lower():
                # Parse the date and time into datetime objects
                formatted_start_time = datetime.strptime(f"{date} {start_time}", "%d-%m-%Y %H:%M")
                formatted_end_time = datetime.strptime(f"{date} {end_time}", "%d-%m-%Y %H:%M")
                return facility.book(formatted_start_time, formatted_end_time)

        return False, 'Facility not found'


# Create facilities and their rates
clubhouse_rates = [
    {'start_time': datetime.strptime('26-10-2020 10:00', '%d-%m-%Y %H:%M'), 'end_time': datetime.strptime('26-10-2020 16:00', '%d-%m-%Y %H:%M'), 'rate': 100},
    {'start_time': datetime.strptime('26-10-2020 16:00', '%d-%m-%Y %H:%M'), 'end_time': datetime.strptime('26-10-2020 22:00', '%d-%m-%Y %H:%M'), 'rate': 500}
]
clubhouse = Facility('Clubhouse', clubhouse_rates)

tennis_court_rates = [
    {'start_time': datetime.strptime('26-10-2020 00:00', '%d-%m-%Y %H:%M'), 'end_time': datetime.strptime('26-10-2020 23:59', '%d-%m-%Y %H:%M'), 'rate': 50}
]
tennis_court = Facility('Tennis Court', tennis_court_rates)

# Create the booking module and add facilities
booking_module = FacilityBookingModule()
booking_module.add_facility(clubhouse)
booking_module.add_facility(tennis_court)

# Perform bookings
print(booking_module.book_facility('Clubhouse', '26-10-2020', '16:00', '22:00'))  # Output: (True, 3000.0)
print(booking_module.book_facility('Tennis Court', '26-10-2020', '16:00', '20:00'))  # Output: (True, 200.0)
print(booking_module.book_facility('Clubhouse', '26-10-2020', '16:00', '22:00'))  # Output: (False, 'Booking Failed, Already Booked')
print(booking_module.book_facility('Tennis Court', '26-10-2020', '17:00', '21:00'))  # Output: (False, 'Booking Failed, Already Booked')
