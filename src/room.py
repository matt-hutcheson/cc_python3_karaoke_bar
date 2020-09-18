class Room():
    def __init__(self, name, capacity):
        self.name = name
        self.guest_list = []
        self.song_list = []
        self.capacity = capacity

    def check_in_guest(self, guest_to_add):
        check = self.capacity_check()
        if check:
            self.guest_list.append(guest_to_add)

    def check_out_guest(self, guest_to_remove):
        self.guest_list.remove(guest_to_remove)

    def add_song(self, song_to_add):
        self.song_list.append(song_to_add)

    def reset_room(self):
        self.song_list.clear()
        self.guest_list.clear()

    def capacity_check(self):
        if len(self.guest_list) < self.capacity:
            return True
        else:
            return False
        
    