import time


class Room:
    def __init__(self, room_name, is_dirty=True):
        self.room_name = room_name
        self.is_dirty = is_dirty
        self.last_clean_time = None


    def change_state(self):
        self.is_dirty = not self.is_dirty

    def should_reset_dirtiness(self):
        if not self.is_dirty and self.last_cleaned_time is not None:
            return time.time() - self.last_cleaned_time >= 30 # Assuming that after cleaning the room, in 30 secs it gets dirty again
        return False

    def reset_dirtiness(self):
        if self.should_reset_dirtiness():
            print(f"Room {self.room_name} has become dirty again!")
            self.change_state()



class ReflexiveAgent:
    def __init__(self, rooms: [Room]):
        self.rooms = rooms


    def _clean_room(self,room:Room):
        print(f"Cleaning room {room.room_name} ......................", end='', flush=True)
        total_time = 10  # Total cleaning time in seconds
        for progress in range(101):
            time.sleep(total_time / 100)  # Sleep for a fraction of the total time
            print(f"\rCleaning room {room.room_name} ... {progress}% complete", end='', flush=True)
        print()  # Print a newline to clear the progress line
        room.change_state()
        room.last_cleaned_time = time.time()


    def sense(self, room: Room):
        if not room.is_dirty:
            print(f"Room {room.room_name} is clean!")
        else:
            print(f"Room {room.room_name} is dirty!")
            self._clean_room(room)

    def start_activities(self):
        start_time = time.time()
        elapsed_time = 0
        while True:
            if elapsed_time >= 300:  # Assuming time for an agent to stop working e.g. after 5 min
                print(f"The {elapsed_time} secs time for the work has been exhousted")
                break
            for room in self.rooms:
                self.sense(room)
                room.reset_dirtiness()
            elapsed_time = time.time() - start_time
