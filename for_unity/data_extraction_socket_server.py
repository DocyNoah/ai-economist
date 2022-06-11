from ai_economist import foundation
from for_unity.socket_server_for_send import ServerSocket, map_data_to_msg
from utils.utils import *
from env_config import env_config
import time


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
        print(t, msg)

        server_socket.send(msg)

        time.sleep(1)


if __name__ == "__main__":
    main(env_config)
