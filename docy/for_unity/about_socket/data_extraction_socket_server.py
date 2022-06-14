from ai_economist import foundation
from docy.utils.utils import *
from docy.env_config import env_config
import time

from docy.for_unity.about_socket.socket_server_for_send import ServerSocket, map_data_to_msg


def main(env_config):
    print()

    # socket
    server_socket = ServerSocket(port=8000)

    env = foundation.make_env_instance(**env_config)
    obs = env.reset(force_dense_logging=False)
    for t in range(10000):
        actions = sample_random_actions(env, obs)
        obs, rew, done, info = env.step(actions)

        map_data = get_map_data(env)
        msg = map_data_to_msg(map_data)
        print(str(t) + ": " + str(len(msg)) + ": " + str(msg))

        server_socket.send(msg)

        time.sleep(1)


if __name__ == "__main__":
    main(env_config)
