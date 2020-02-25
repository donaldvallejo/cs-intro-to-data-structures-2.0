# rooms = {"Golden Gate": 70, "Great Hall": 55, "Times Square": 40, "Stonehenge": 19}


# 1
# def heat_up(room):
#     for current_room, temp in rooms.items():
#         print(current_room)
#         print(temp)
#         if current_room == room:
#             rooms[room] = rooms[room] + 5
#         else:
#             return 'Error'

# def heat_up(room):
#     if room in rooms.keys():
#         rooms[room] = rooms[room] + 5
#     else: 
#         return "Error"
#     print(room)
# heat_up("Great Hall")


# 2
# def heat_up(room):
#     for current_room, temp in rooms.items():
#         print(current_room)
#         print(temp)
#         if current_room == room:
#             rooms[room] = rooms[room] - 5
#         else:
#             return 'Error'

# def cool_down(room):
#     if room in rooms.keys():
#         rooms[room] = rooms[room] - 5
#     else: 
#         return "Error"
#     print(room)
# heat_up("Great Hall")


# 3 Keep separate from top half of page/file
class Thermostate:
    def __init__(self, name):
        self.name = name 
        self.rooms = {"Golden Gate": 70, "Great Hall": 55, "Times Square": 40, "Stonehenge": 19}

    def heat_up(self, room):
        for room in self.rooms.keys():
            print(room)
            if room == room:
                self.rooms[room] = self.rooms[room] - 5
            else:
                return 'Error'

    def cool_down(self, room):
        if room in self.rooms.keys():
            self.rooms[room] = self.rooms[room] - 5
        else: 
            return "Error"
        print(room)
my_thermostat = Thermostate("some name")
my_thermostat.heat_up("Great Hall")

# class Nest(Thermostate):
#     def __init__(self, name, cool_extra):
