# ================================================================
# HOTEL ENQUIRY CHATBOT - S KAVINKUMAR
# ================================================================

hotels = {
    "bangalore": {
        "name": "Grand Palace Bangalore",
        "city": "Bangalore", "state": "Karnataka",
        "address": "MG Road, Bangalore",
        "airport": "Kempegowda International Airport",
        "railway": "KSR Bangalore Railway Station",
        "rooms": {
            "standard": {"price": 2200, "guests": 2},
            "deluxe": {"price": 3200, "guests": 2},
            "premium": {"price": 4200, "guests": 3},
            "family": {"price": 5200, "guests": 4},
            "suite": {"price": 7000, "guests": 4},
            "presidential": {"price": 12000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Free Parking", "Restaurant",
                       "Swimming Pool", "Gym", "Breakfast", "Room Service"]
    },

    "chennai": {
        "name": "Marina Grand Hotel",
        "city": "Chennai", "state": "Tamil Nadu",
        "address": "Anna Salai, Chennai",
        "airport": "Chennai International Airport",
        "railway": "Chennai Central Railway Station",
        "rooms": {
            "standard": {"price": 2000, "guests": 2},
            "deluxe": {"price": 3000, "guests": 2},
            "premium": {"price": 4000, "guests": 3},
            "family": {"price": 5000, "guests": 4},
            "suite": {"price": 6800, "guests": 4},
            "presidential": {"price": 11000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Restaurant", "Parking",
                       "Gym", "Breakfast", "Laundry Service"]
    },

    "mumbai": {
        "name": "Royal Mumbai Hotel",
        "city": "Mumbai", "state": "Maharashtra",
        "address": "Andheri West, Mumbai",
        "airport": "Chhatrapati Shivaji Maharaj International Airport",
        "railway": "Mumbai Central Railway Station",
        "rooms": {
            "standard": {"price": 3000, "guests": 2},
            "deluxe": {"price": 4500, "guests": 2},
            "premium": {"price": 6000, "guests": 3},
            "family": {"price": 7500, "guests": 4},
            "suite": {"price": 10000, "guests": 4},
            "presidential": {"price": 18000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Swimming Pool", "Gym",
                       "Restaurant", "Breakfast", "Parking", "Spa"]
    },

    "delhi": {
        "name": "Capital Grand Hotel",
        "city": "New Delhi", "state": "Delhi",
        "address": "Connaught Place, New Delhi",
        "airport": "Indira Gandhi International Airport",
        "railway": "New Delhi Railway Station",
        "rooms": {
            "standard": {"price": 2500, "guests": 2},
            "deluxe": {"price": 3800, "guests": 2},
            "premium": {"price": 5000, "guests": 3},
            "family": {"price": 6200, "guests": 4},
            "suite": {"price": 8500, "guests": 4},
            "presidential": {"price": 15000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Restaurant", "Parking",
                       "Gym", "Swimming Pool", "Breakfast"]
    },

    "hyderabad": {
        "name": "Deccan Grand Hotel",
        "city": "Hyderabad", "state": "Telangana",
        "address": "Banjara Hills, Hyderabad",
        "airport": "Rajiv Gandhi International Airport",
        "railway": "Secunderabad Railway Station",
        "rooms": {
            "standard": {"price": 1900, "guests": 2},
            "deluxe": {"price": 2900, "guests": 2},
            "premium": {"price": 3900, "guests": 3},
            "family": {"price": 4900, "guests": 4},
            "suite": {"price": 6500, "guests": 4},
            "presidential": {"price": 10000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Breakfast", "Restaurant",
                       "Parking", "Gym", "Room Service"]
    },

    "kochi": {
        "name": "Cochin Bay Hotel",
        "city": "Kochi", "state": "Kerala",
        "address": "Marine Drive, Kochi",
        "airport": "Cochin International Airport",
        "railway": "Ernakulam Junction",
        "rooms": {
            "standard": {"price": 1800, "guests": 2},
            "deluxe": {"price": 2800, "guests": 2},
            "premium": {"price": 3800, "guests": 3},
            "family": {"price": 4800, "guests": 4},
            "suite": {"price": 6500, "guests": 4},
            "presidential": {"price": 9500, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Swimming Pool", "Restaurant",
                       "Breakfast", "Parking", "Gym"]
    },

    "goa": {
        "name": "Goa Beach Resort",
        "city": "Goa", "state": "Goa",
        "address": "Calangute, Goa",
        "airport": "Manohar International Airport",
        "railway": "Madgaon Railway Station",
        "rooms": {
            "standard": {"price": 2500, "guests": 2},
            "deluxe": {"price": 4000, "guests": 2},
            "premium": {"price": 5500, "guests": 3},
            "family": {"price": 7000, "guests": 4},
            "suite": {"price": 9500, "guests": 4},
            "presidential": {"price": 16000, "guests": 6}
        },
        "facilities": ["Beach Access", "Free Wi-Fi", "Swimming Pool",
                       "Restaurant", "Breakfast", "Parking", "Spa"]
    },

    "jaipur": {
        "name": "Pink City Palace Hotel",
        "city": "Jaipur", "state": "Rajasthan",
        "address": "C-Scheme, Jaipur",
        "airport": "Jaipur International Airport",
        "railway": "Jaipur Railway Station",
        "rooms": {
            "standard": {"price": 1800, "guests": 2},
            "deluxe": {"price": 2700, "guests": 2},
            "premium": {"price": 3600, "guests": 3},
            "family": {"price": 4500, "guests": 4},
            "suite": {"price": 6000, "guests": 4},
            "presidential": {"price": 9000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Restaurant", "Swimming Pool",
                       "Parking", "Breakfast"]
    },

    "kolkata": {
        "name": "City of Joy Hotel",
        "city": "Kolkata", "state": "West Bengal",
        "address": "Park Street, Kolkata",
        "airport": "Netaji Subhas Chandra Bose International Airport",
        "railway": "Howrah Railway Station",
        "rooms": {
            "standard": {"price": 2000, "guests": 2},
            "deluxe": {"price": 3000, "guests": 2},
            "premium": {"price": 4000, "guests": 3},
            "family": {"price": 5000, "guests": 4},
            "suite": {"price": 7000, "guests": 4},
            "presidential": {"price": 11000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Restaurant", "Breakfast",
                       "Parking", "Gym", "Room Service"]
    },

    "pune": {
        "name": "Pune Central Hotel",
        "city": "Pune", "state": "Maharashtra",
        "address": "Hinjewadi, Pune",
        "airport": "Pune International Airport",
        "railway": "Pune Railway Station",
        "rooms": {
            "standard": {"price": 1900, "guests": 2},
            "deluxe": {"price": 2900, "guests": 2},
            "premium": {"price": 3900, "guests": 3},
            "family": {"price": 4900, "guests": 4},
            "suite": {"price": 6500, "guests": 4},
            "presidential": {"price": 10000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Gym", "Restaurant",
                       "Breakfast", "Parking"]
    },

    "ahmedabad": {
        "name": "Sabarmati Grand Hotel",
        "city": "Ahmedabad", "state": "Gujarat",
        "address": "Navrangpura, Ahmedabad",
        "airport": "Sardar Vallabhbhai Patel International Airport",
        "railway": "Ahmedabad Railway Station",
        "rooms": {
            "standard": {"price": 1700, "guests": 2},
            "deluxe": {"price": 2600, "guests": 2},
            "premium": {"price": 3500, "guests": 3},
            "family": {"price": 4500, "guests": 4},
            "suite": {"price": 6000, "guests": 4},
            "presidential": {"price": 8500, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Restaurant", "Breakfast",
                       "Parking", "Gym"]
    },

    "lucknow": {
        "name": "Nawab Palace Hotel",
        "city": "Lucknow", "state": "Uttar Pradesh",
        "address": "Hazratganj, Lucknow",
        "airport": "Chaudhary Charan Singh International Airport",
        "railway": "Lucknow Railway Station",
        "rooms": {
            "standard": {"price": 1600, "guests": 2},
            "deluxe": {"price": 2500, "guests": 2},
            "premium": {"price": 3400, "guests": 3},
            "family": {"price": 4300, "guests": 4},
            "suite": {"price": 5800, "guests": 4},
            "presidential": {"price": 8500, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Restaurant", "Breakfast",
                       "Parking", "Room Service"]
    },

    "chandigarh": {
        "name": "Chandigarh Grand Hotel",
        "city": "Chandigarh", "state": "Chandigarh",
        "address": "Sector 17, Chandigarh",
        "airport": "Chandigarh International Airport",
        "railway": "Chandigarh Railway Station",
        "rooms": {
            "standard": {"price": 1800, "guests": 2},
            "deluxe": {"price": 2800, "guests": 2},
            "premium": {"price": 3700, "guests": 3},
            "family": {"price": 4700, "guests": 4},
            "suite": {"price": 6200, "guests": 4},
            "presidential": {"price": 9000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Parking", "Restaurant",
                       "Breakfast", "Swimming Pool", "Gym"]
    },

    "varanasi": {
        "name": "Ganga View Hotel",
        "city": "Varanasi", "state": "Uttar Pradesh",
        "address": "Near Ganges, Varanasi",
        "airport": "Lal Bahadur Shastri International Airport",
        "railway": "Varanasi Junction",
        "rooms": {
            "standard": {"price": 1500, "guests": 2},
            "deluxe": {"price": 2300, "guests": 2},
            "premium": {"price": 3200, "guests": 3},
            "family": {"price": 4200, "guests": 4},
            "suite": {"price": 5500, "guests": 4},
            "presidential": {"price": 8000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Restaurant", "Breakfast",
                       "Parking", "River View"]
    },

    "ooty": {
        "name": "Blue Hills Resort",
        "city": "Ooty", "state": "Tamil Nadu",
        "address": "Coonoor Road, Ooty",
        "airport": "Coimbatore International Airport",
        "railway": "Mettupalayam Railway Station",
        "rooms": {
            "standard": {"price": 2200, "guests": 2},
            "deluxe": {"price": 3200, "guests": 2},
            "premium": {"price": 4200, "guests": 3},
            "family": {"price": 5200, "guests": 4},
            "suite": {"price": 7000, "guests": 4},
            "presidential": {"price": 10000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Mountain View", "Restaurant",
                       "Breakfast", "Parking", "Bonfire"]
    },

    "mysore": {
        "name": "Mysore Heritage Hotel",
        "city": "Mysore", "state": "Karnataka",
        "address": "Sayyaji Rao Road, Mysore",
        "airport": "Mysore Airport",
        "railway": "Mysore Junction",
        "rooms": {
            "standard": {"price": 1800, "guests": 2},
            "deluxe": {"price": 2700, "guests": 2},
            "premium": {"price": 3600, "guests": 3},
            "family": {"price": 4600, "guests": 4},
            "suite": {"price": 6000, "guests": 4},
            "presidential": {"price": 9000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Restaurant", "Breakfast",
                       "Parking", "Swimming Pool"]
    },

    "coimbatore": {
        "name": "Coimbatore Comfort Hotel",
        "city": "Coimbatore", "state": "Tamil Nadu",
        "address": "Avinashi Road, Coimbatore",
        "airport": "Coimbatore International Airport",
        "railway": "Coimbatore Junction",
        "rooms": {
            "standard": {"price": 1700, "guests": 2},
            "deluxe": {"price": 2600, "guests": 2},
            "premium": {"price": 3500, "guests": 3},
            "family": {"price": 4500, "guests": 4},
            "suite": {"price": 5900, "guests": 4},
            "presidential": {"price": 8500, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "Restaurant", "Breakfast",
                       "Parking", "Gym"]
    },

    "rishikesh": {
        "name": "Ganga Riverside Resort",
        "city": "Rishikesh", "state": "Uttarakhand",
        "address": "Tapovan, Rishikesh",
        "airport": "Jolly Grant Airport",
        "railway": "Rishikesh Railway Station",
        "rooms": {
            "standard": {"price": 2000, "guests": 2},
            "deluxe": {"price": 3000, "guests": 2},
            "premium": {"price": 4200, "guests": 3},
            "family": {"price": 5200, "guests": 4},
            "suite": {"price": 7000, "guests": 4},
            "presidential": {"price": 10000, "guests": 6}
        },
        "facilities": ["Free Wi-Fi", "River View", "Restaurant",
                       "Breakfast", "Parking", "Yoga Area"]
    }
}


# ================================================================
# CITY ALIASES
# ================================================================

city_aliases = {
    "bangalore": "bangalore",
    "bengaluru": "bangalore",
    "chennai": "chennai",
    "madras": "chennai",
    "mumbai": "mumbai",
    "bombay": "mumbai",
    "delhi": "delhi",
    "new delhi": "delhi",
    "hyderabad": "hyderabad",
    "kochi": "kochi",
    "cochin": "kochi",
    "goa": "goa",
    "jaipur": "jaipur",
    "kolkata": "kolkata",
    "calcutta": "kolkata",
    "pune": "pune",
    "ahmedabad": "ahmedabad",
    "lucknow": "lucknow",
    "chandigarh": "chandigarh",
    "varanasi": "varanasi",
    "banaras": "varanasi",
    "ooty": "ooty",
    "mysore": "mysore",
    "mysuru": "mysore",
    "coimbatore": "coimbatore",
    "rishikesh": "rishikesh"
}


# ================================================================
# INTENT DETECTION
# ================================================================

def detect_intent(message):

    text = message.lower().strip()

    if any(x in text for x in [
        "hello", "hi", "hey", "hai",
        "good morning", "good afternoon",
        "good evening"
    ]):
        return "GREETING"

    if any(x in text for x in [
        "cancel", "cancellation", "refund",
        "cancel booking"
    ]):
        return "CANCELLATION"

    if any(x in text for x in [
        "check in", "check-in",
        "check out", "check-out",
        "checkout", "early check",
        "late check"
    ]):
        return "CHECK_IN"

    if any(x in text for x in [
        "facility", "facilities", "amenities",
        "wifi", "wi-fi", "parking",
        "breakfast", "pool", "swimming",
        "gym", "restaurant", "spa",
        "beach", "mountain", "river",
        "yoga", "bonfire"
    ]):
        return "FACILITIES"

    if any(x in text for x in [
        "location", "address", "where",
        "located", "airport", "railway",
        "station", "near"
    ]):
        return "LOCATION"

    if any(x in text for x in [
        "price", "prices", "cost", "rate",
        "tariff", "how much", "amount",
        "budget", "cheap", "expensive"
    ]):
        return "PRICE"

    if any(x in text for x in [
        "room", "rooms", "stay",
        "accommodation", "book a room",
        "available room"
    ]):
        return "ROOM_SEARCH"

    if any(x in text for x in [
        "bye", "goodbye", "exit",
        "quit"
    ]):
        return "EXIT"

    return "UNKNOWN"


# ================================================================
# CITY DETECTION
# ================================================================

def detect_city(message):

    text = message.lower()

    for city in sorted(city_aliases, key=len, reverse=True):

        if city in text:
            return city_aliases[city]

    return None


# ================================================================
# ROOM TYPE DETECTION
# ================================================================

def detect_room(message):

    text = message.lower()

    if "presidential" in text:
        return "presidential"

    if "suite" in text:
        return "suite"

    if "family" in text:
        return "family"

    if "premium" in text:
        return "premium"

    if "deluxe" in text:
        return "deluxe"

    if "standard" in text or "single room" in text:
        return "standard"

    return None


# ================================================================
# FACILITY DETECTION
# ================================================================

def detect_facility(message):

    text = message.lower()

    facility_map = {
        "wifi": "Free Wi-Fi",
        "wi-fi": "Free Wi-Fi",
        "parking": "Free Parking",
        "breakfast": "Breakfast",
        "swimming pool": "Swimming Pool",
        "swimming": "Swimming Pool",
        "pool": "Swimming Pool",
        "gym": "Gym",
        "restaurant": "Restaurant",
        "spa": "Spa",
        "beach": "Beach Access",
        "mountain": "Mountain View",
        "river": "River View",
        "yoga": "Yoga Area",
        "bonfire": "Bonfire"
    }

    for word, facility in facility_map.items():

        if word in text:
            return facility

    return None


# ================================================================
# SHOW LOCATIONS
# ================================================================

def show_locations():

    result = "Available Hotel Locations in India:\n\n"

    for hotel in hotels.values():

        result += (
            f"• {hotel['city']}, {hotel['state']} - "
            f"{hotel['name']}\n"
        )

    return result


# ================================================================
# SHOW ROOMS
# ================================================================

def show_rooms(hotel):

    result = f"Rooms available at {hotel['name']}:\n\n"

    for room, data in hotel["rooms"].items():

        result += (
            f"• {room.title()} Room - "
            f"₹{data['price']} per night - "
            f"Up to {data['guests']} guests\n"
        )

    return result


# ================================================================
# CHATBOT
# ================================================================

def chatbot_response(message, current_city=None, current_room=None):

    intent = detect_intent(message)

    city = detect_city(message)

    room_type = detect_room(message)

    facility = detect_facility(message)

    if city:
        current_city = city

    if room_type:
        current_room = room_type


    # GREETING
    if intent == "GREETING":

        response = (
            "Hello! Welcome to the Hotel Enquiry Chatbot.\n\n"
            "I can help you with rooms, prices, facilities, "
            "locations, check-in and cancellation.\n\n"
            "We have hotels across India."
        )

        return response, current_city, current_room


    # ROOM SEARCH
    if intent == "ROOM_SEARCH":

        if current_city is None:

            return (
                show_locations() +
                "\nWhich city would you like?"
            ), current_city, current_room

        hotel = hotels[current_city]

        if current_room:

            room = hotel["rooms"][current_room]

            return (
                f"{hotel['name']} offers a "
                f"{current_room.title()} Room.\n\n"
                f"Price: ₹{room['price']} per night\n"
                f"Maximum guests: {room['guests']}"
            ), current_city, current_room

        return (
            show_rooms(hotel) +
            "\nWhich room type would you like?"
        ), current_city, current_room


    # PRICE
    if intent == "PRICE":

        if current_city is None:

            return (
                "Please tell me the city first.\n"
                "Example: What is the price of a room in Goa?"
            ), current_city, current_room

        hotel = hotels[current_city]

        if current_room:

            price = hotel["rooms"][current_room]["price"]

            return (
                f"The {current_room.title()} Room at "
                f"{hotel['name']} costs ₹{price} per night."
            ), current_city, current_room

        result = f"Prices at {hotel['name']}:\n\n"

        for room, data in hotel["rooms"].items():

            result += (
                f"• {room.title()}: "
                f"₹{data['price']} per night\n"
            )

        return result, current_city, current_room


    # FACILITIES
    if intent == "FACILITIES":

        if current_city is None:

            return (
                "Please tell me the city first.\n"
                "Example: What facilities are available in Goa?"
            ), current_city, current_room

        hotel = hotels[current_city]

        if facility:

            found = any(
                facility.lower() in item.lower()
                for item in hotel["facilities"]
            )

            if found:

                return (
                    f"Yes, {hotel['name']} provides "
                    f"{facility}."
                ), current_city, current_room

            return (
                f"Sorry, {hotel['name']} does not list "
                f"{facility} among its facilities."
            ), current_city, current_room

        result = f"Facilities at {hotel['name']}:\n\n"

        for item in hotel["facilities"]:

            result += f"• {item}\n"

        return result, current_city, current_room


    # LOCATION
    if intent == "LOCATION":

        if current_city is None:

            return (
                show_locations() +
                "\nWhich city are you interested in?"
            ), current_city, current_room

        hotel = hotels[current_city]

        return (
            f"{hotel['name']}\n\n"
            f"City: {hotel['city']}\n"
            f"State: {hotel['state']}\n"
            f"Address: {hotel['address']}\n"
            f"Airport: {hotel['airport']}\n"
            f"Railway Station: {hotel['railway']}"
        ), current_city, current_room


    # CHECK-IN
    if intent == "CHECK_IN":

        return (
            "Check-in and Check-out Information:\n\n"
            "• Check-in: 2:00 PM\n"
            "• Check-out: 12:00 PM\n"
            "• Early check-in: Subject to availability\n"
            "• Late check-out: Subject to availability\n"
            "• Additional charges may apply."
        ), current_city, current_room


    # CANCELLATION
    if intent == "CANCELLATION":

        return (
            "Cancellation Policy:\n\n"
            "• More than 48 hours before check-in: Full refund\n"
            "• 24 to 48 hours before check-in: 50% refund\n"
            "• Less than 24 hours: No refund\n"
            "• No-show: No refund"
        ), current_city, current_room


    # EXIT
    if intent == "EXIT":

        return (
            "Thank you for using the Hotel Enquiry Chatbot!\n"
            "Have a wonderful day!"
        ), current_city, current_room


    # UNKNOWN
    return (
        "Sorry, I could not understand your question.\n\n"
        "You can ask about:\n"
        "• Rooms\n"
        "• Prices\n"
        "• Facilities\n"
        "• Locations\n"
        "• Check-in / Check-out\n"
        "• Cancellation\n\n"
        "Example: I need a deluxe room in Goa"
    ), current_city, current_room


# ================================================================
# START CHATBOT
# ================================================================

print("=" * 65)
print("                 HOTEL ENQUIRY CHATBOT")
print("                     S KAVINKUMAR")
print("=" * 65)

print("\nBot: Hello! Welcome to the Hotel Enquiry Chatbot.")
print("Bot: Ask me about rooms, prices, facilities, locations,")
print("     check-in or cancellation.")
print("Bot: Type 'bye' to end the conversation.\n")

if __name__ == "__main__":

    current_city = None
    current_room = None

    while True:

        user_message = input("You: ").strip()

        if user_message == "":
            print("Bot: Please enter your question.\n")
            continue

        response, current_city, current_room = chatbot_response(
            user_message,
            current_city,
            current_room
        )

        print("\nBot:", response)
        print()

        if detect_intent(user_message) == "EXIT":
            break
