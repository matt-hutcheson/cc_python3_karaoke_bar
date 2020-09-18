class Room():
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []

    def check_in_guest(self, guest_to_add):
        self.guest_list.append(guest_to_add)

    def check_out_guest(self, guest_to_remove):
        self.guest_list.remove(guest_to_remove)