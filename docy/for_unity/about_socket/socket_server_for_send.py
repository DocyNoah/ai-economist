import socket


class ServerSocket:
    def __init__(self, port: int):
        # socket()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind()
        self.server_socket.bind(('127.0.0.1', port))

        # listen()
        self.server_socket.listen()
        print("Listening...")

        # accept()
        self.client_socket, self.address = self.server_socket.accept()
        print('Connected by', self.address)

    def __del__(self):
        self.client_socket.close()
        self.server_socket.close()

    def send(self, msg: str, verbose=False):
        self.client_socket.sendall(msg.encode())
        if verbose:
            print("send:", msg)


def map_data_to_msg(map_data):
    """
    agents_locs : ndarray (2, 4) int32
    world_size : tuple (2,)
    stone_map : ndarray (25, 25) float64
    wood_map : ndarray (25, 25) float64
    water_map : ndarray (25, 25) float64
    house_maps : ndarray (4, 25, 25) float64
    """
    agent_locs, world_size, stone_map, wood_map, water_map, house_maps = map_data

    str_list = []

    # agent_locs
    agent_locs_str = twodarray_to_str_list(agent_locs)
    str_list.extend(agent_locs_str)
    str_list.append("|")

    # world_size
    world_size_str = onedarray_to_str_list(world_size)
    str_list.extend(world_size_str)
    str_list.append("|")

    # stone_map
    stone_map_str = twodarray_to_str_list(stone_map)
    str_list.extend(stone_map_str)
    str_list.append("|")

    # wood_map
    wood_map_str = twodarray_to_str_list(wood_map)
    str_list.extend(wood_map_str)
    str_list.append("|")

    # water_map
    water_map_str = twodarray_to_str_list(water_map)
    str_list.extend(water_map_str)
    str_list.append("|")

    # house_maps
    for house_map in house_maps:
        house_map_str = twodarray_to_str_list(house_map)
        str_list.extend(house_map_str)
        str_list.append("|")

    str_list.pop()
    msg = "".join(str_list)
    return msg


def onedarray_to_str_list(onedarray):
    str_list = []
    for element in onedarray:
        str_list.append(str(int(element)))
        str_list.append(",")
    str_list.pop()

    return str_list


def twodarray_to_str_list(twodarray):
    str_list = []
    for onedarray in twodarray:
        for element in onedarray:
            str_list.append(str(int(element)))
            str_list.append(",")
        str_list.pop()
        str_list.append("/")
    str_list.pop()

    return str_list
