from ai_economist import foundation
from docy.utils.utils import *
from docy.env_config import env_config
import time

import grpc_client_for_send


def main(env_config):
    print()

    # client
    server_ip = "localhost"
    server_port = 50051
    client = grpc_client_for_send.EcoClient(server_ip, server_port)

    env = foundation.make_env_instance(**env_config)
    obs = env.reset(force_dense_logging=False)
    for t in range(10000):
        actions = sample_random_actions(env, obs)
        obs, rew, done, info = env.step(actions)
        data = get_map_data(env)
        client.send_data(data)
        print("Send Data", t)
        time.sleep(1)


if __name__ == "__main__":
    main(env_config)
