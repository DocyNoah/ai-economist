import matplotlib.pyplot as plt
from numpy import iterable
from ai_economist import foundation
from utils.utils import *
from utils.plotting import *
import grpc_server


def main(env_config, plot_every):
    print()

    env = foundation.make_env_instance(**env_config)
    obs = env.reset(force_dense_logging=False)
    for t in range(100):
        actions = sample_random_actions(env, obs)
        obs, rew, done, info = env.step(actions)
    grpc_server.serve(port=50051, env=env)

    np.set_printoptions(threshold=100000, linewidth=100)
    data = get_visualize_data(env)
    agent_locs, world_size, stone_map, wood_map, water_map, house_maps = data
    print("agent_locs:")
    print(type(agent_locs))
    print(agent_locs.dtype)
    print(agent_locs)
    print()

    print("world_size:")
    print(type(world_size))
    print(world_size)
    print()
    print("stone_map:")
    print(type(stone_map))
    print(stone_map.dtype)
    print(stone_map.shape)
    print(stone_map)
    print()
    print("wood_map:")
    print(type(wood_map))
    print(wood_map.dtype)
    print(wood_map.shape)
    print(wood_map)
    print()
    print("water_map:")
    print(type(water_map))
    print(water_map.dtype)
    print(water_map.shape)
    print(water_map)
    print()
    print("house_maps:")
    print(type(house_maps))
    print(house_maps.dtype)
    print(house_maps.shape)
    print(house_maps)
    print()

    # fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    # do_plot(env, ax, fig, t, show=True, save=True)

    # print_attr(env)
    # print_attr(env.world)
    # print_attr(env.world.maps)

    # print(env.n_agents)
    # print(env.all_agents[0])
    # print(env.get_agent(0))
    # print(env.world.agents[0])
    # print()

    ########################################################

    # maps = env.world.maps
    # locs = [agent.loc for agent in env.world.agents]
    #
    # world_size = np.array(maps.get("Wood")).shape
    # max_health = {"Wood": 1, "Stone": 1, "House": 1}
    #
    # n_agents = len(locs)
    #
    # tmp = np.zeros((3, world_size[0], world_size[1]))
    #
    # scenario_entities = [k for k in maps.keys() if "source" not in k.lower()]
    # """
    # maps.keys()
    # ['Stone', 'Wood', 'House', 'Water', 'StoneSourceBlock', 'WoodSourceBlock']
    #
    # scenario_entities
    # ['Stone', 'Wood', 'House', 'Water']
    # """
    # for entity in scenario_entities:
    #     if entity == "House":
    #         continue
    #     elif resources.has(entity):  # Stone, Wood
    #         if resources.get(entity).collectible:
    #             """
    #             None index는 단순히 차원 늘리는 용도, squeez와 용도가 같음
    #             resources.get(entity).color                 | (3,)
    #             resources.get(entity).color[:, None, None]  | (3, 1, 1)
    #             np.array(maps.get(entity))                  | (25, 25)
    #             np.array(maps.get(entity))[None]            | (1, 25, 25)
    #             map_ = (3, 1, 1) * (1, 25, 25)              | (3, 25, 25)
    #             """
    #             map_ = (
    #                 resources.get(entity).color[:, None, None]
    #                 * np.array(maps.get(entity))[None]
    #             )
    #             map_ /= max_health[entity]
    #             tmp += map_
    #             print("resources.get(entity).collectible")
    #             print(entity)
    #             print("resources.get(entity).color.shape:", resources.get(entity).color.shape)
    #             print("resources.get(entity).color[:, None, None].shape:", resources.get(entity).color[:, None, None].shape)
    #             print("np.array(maps.get(entity)).shape:", np.array(maps.get(entity)).shape)
    #             print("np.array(maps.get(entity))[None].shape:", np.array(maps.get(entity))[None].shape)
    #             print("map_.shape:", map_.shape)
    #             print("type(maps.get(entity)):", type(maps.get(entity)))
    #             print()
    #     elif landmarks.has(entity):
    #         map_ = (
    #             landmarks.get(entity).color[:, None, None]
    #             * np.array(maps.get(entity))[None]
    #         )
    #         tmp += map_
    #         print("landmarks.has(entity)")
    #         print(entity)
    #         print("landmarks.get(entity).color.shape:", landmarks.get(entity).color.shape)
    #         print("landmarks.get(entity).color[:, None, None].shape:", landmarks.get(entity).color[:, None, None].shape)
    #         print()
    #     else:
    #         continue
    #
    # """type(maps): Maps class"""
    # if isinstance(maps, dict):
    #     house_idx = np.array(maps.get("House")["owner"])
    #     house_health = np.array(maps.get("House")["health"])
    # else:
    #     house_idx = maps.get("House", owner=True)
    #     house_health = maps.get("House")
    # print("type(house_idx):", type(house_idx))
    # print("house_idx.shape:", house_idx.shape)
    # print()
    #
    # cmap = plt.get_cmap("jet", n_agents)
    # cmap_order = list(range(n_agents))
    # for i in range(n_agents):
    #     houses = house_health * (house_idx == cmap_order[i])
    #     print("houses.shape:", houses.shape)
    #     agent = np.zeros_like(houses)
    #     agent += houses
    #     print("agent.shape:", agent.shape)
    #     print("agent[None].shape:", agent[None].shape)
    #     print(cmap(i))
    #     col = np.array(cmap(i)[:3])
    #     map_ = col[:, None, None] * agent[None]
    #     tmp += map_
    #     print()


if __name__ == "__main__":
    # Define the configuration of the environment that will be built

    env_config = {
        # ===== SCENARIO CLASS =====
        # Which Scenario class to use: the class's name in the Scenario Registry (foundation.scenarios).
        # The environment object will be an instance of the Scenario class.
        'scenario_name': 'layout_from_file/simple_wood_and_stone',

        # ===== COMPONENTS =====
        # Which components to use (specified as list of ("component_name", {component_kwargs}) tuples).
        #   "component_name" refers to the Component class's name in the Component Registry (foundation.components)
        #   {component_kwargs} is a dictionary of kwargs passed to the Component class
        # The order in which components reset, step, and generate obs follows their listed order below.
        'components': [
            # (1) Building houses
            ('Build', {'skill_dist': "pareto", 'payment_max_skill_multiplier': 3}),
            # (2) Trading collectible resources
            ('ContinuousDoubleAuction', {'max_num_orders': 5}),
            # (3) Movement and resource collection
            ('Gather', {}),
        ],

        # ===== SCENARIO CLASS ARGUMENTS =====
        # (optional) kwargs that are added by the Scenario class (i.e. not defined in BaseEnvironment)
        'env_layout_file': 'quadrant_25x25_20each_30clump.txt',
        'starting_agent_coin': 10,
        'fixed_four_skill_and_loc': True,

        # ===== STANDARD ARGUMENTS ======
        # kwargs that are used by every Scenario class (i.e. defined in BaseEnvironment)
        'n_agents': 4,  # Number of non-planner agents (must be > 1)
        'world_size': [25, 25],  # [Height, Width] of the env world
        'episode_length': 1000,  # Number of timesteps per episode

        # In multi-action-mode, the policy selects an action for each action subspace (defined in component code).
        # Otherwise, the policy selects only 1 action.
        'multi_action_mode_agents': False,
        'multi_action_mode_planner': True,

        # When flattening observations, concatenate scalar & vector observations before output.
        # Otherwise, return observations with minimal processing.
        'flatten_observations': False,
        # When Flattening masks, concatenate each action subspace mask into a single array.
        # Note: flatten_masks = True is required for masking action logits in the code below.
        'flatten_masks': True,
    }

    plot_every = 100

    main(env_config, plot_every)
