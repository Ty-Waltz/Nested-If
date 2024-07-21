attendees = int(input("Enter number of attendees: "))
venue = "Room: Large Hall" if attendees  > 100 else "Room: Conference Room"
audio_system = "Audio: Large System" if attendees > 100 else "Audio: Small System"
projector = "Projector: Large" if attendees > 100 else "Projector: Small"
vegitarian= input("Would you like vegetarian food?")
food = "We reccomend Veggie Delight Caterers" if vegitarian == "yes" else "We reccomend Gourmet Meals Caterers"
print(venue, audio_system, projector)
print(food)
