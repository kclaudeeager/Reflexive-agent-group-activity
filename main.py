
from reflexive_agent.reflexive_agent import Room, ReflexiveAgent

if __name__ == '__main__':
    room_names = ["A", "B", "C", "D"]
    rooms = [Room("Room " + room_name) for room_name in room_names]
    reflexive_agent = ReflexiveAgent(rooms)
    reflexive_agent.start_activities()
