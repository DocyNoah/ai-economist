from ai_economist import foundation
from utils.utils import *
import time

from docy.env_config import env_config


def main(env_config):
    print()

    env = foundation.make_env_instance(**env_config)
    obs = env.reset(force_dense_logging=False)
    for t in range(10000):
        actions = sample_random_actions(env, obs)
        obs, rew, done, info = env.step(actions)

        # # obs
        # print("obs")
        # print_type(obs)

        # # obs['0']
        # print("obs['0']")
        # print_type(obs['0'])

        # # map_data (for visualizing)
        # map_data = get_map_data(env)
        # print_map_data_shape(map_data)

        # env
        # print("env")
        # print_attr(env)

        time.sleep(100)


if __name__ == "__main__":
    main(env_config)
