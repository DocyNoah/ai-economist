from ai_economist import foundation
from docy.utils.utils import *
from docy.env_config import env_config
import time

import grpc_server_for_send
from multiprocessing import Queue


def main(env_config):
    print()

    # server
    server_queue = Queue()
    server = grpc_server_for_send.AIEconomistServer(port=50051, queue=server_queue)
    server.start()

    env = foundation.make_env_instance(**env_config)
    obs = env.reset(force_dense_logging=False)
    for t in range(10000):
        actions = sample_random_actions(env, obs)
        obs, rew, done, info = env.step(actions)
        data = get_map_data(env)
        server_queue.put_nowait(data)
        print("send_buffer.add(data)", t)
        time.sleep(1)


if __name__ == "__main__":
    main(env_config)
