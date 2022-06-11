import numpy as np
from numpy import iterable
from ai_economist.foundation.entities import landmark_registry as landmarks
from ai_economist.foundation.entities import resource_registry as resources


def sample_random_action(agent, mask):
    """Sample random UNMASKED action(s) for agent."""
    # Return a list of actions: 1 for each action subspace
    if agent.multi_action_mode:
        split_masks = np.split(mask, agent.action_spaces.cumsum()[:-1])
        return [np.random.choice(np.arange(len(m_)), p=m_/m_.sum()) for m_ in split_masks]

    # Return a single action
    else:
        return np.random.choice(np.arange(agent.action_spaces), p=mask/mask.sum())


def sample_random_actions(env, obs):
    """Samples random UNMASKED actions for each agent in obs."""

    actions = {
        a_idx: sample_random_action(env.get_agent(a_idx), a_obs['action_mask'])
        for a_idx, a_obs in obs.items()
    }

    return actions


def print_attr(cls):
    for element in dir(cls):
        if element.startswith("_"):
            continue
        print(element)
        attr = getattr(cls, element)
        if callable(attr):
            print("'{}' is callable".format(element))
        elif isinstance(attr, np.ndarray) and attr.ndim > 1:
            print("shape:", attr.shape)
            print("dtype:", attr.dtype)
        elif iterable(attr):
            print("len:", len(attr))
        else:
            print(attr)
        print()


def print_type(var, inner=0):
    print_with_tap("type:", type(var), n_tap=inner)
    if isinstance(var, np.ndarray) and var.ndim > 1:
        print_with_tap("shape:", var.shape, n_tap=inner)
        print_with_tap("dtype:", var.dtype, n_tap=inner)
        if var.ndim <= 1:
            print_with_tap("len:", len(var), n_tap=inner)
    elif isinstance(var, dict):
        inner += 1
        for k, v in var.items():
            print_with_tap("key:", k, n_tap=inner)
            print_type(v, inner)
    elif iterable(var):
        print_with_tap("len:", len(var), n_tap=inner)
        print_with_tap("dtype:", type(var[0]), n_tap=inner)
        if len(var) < 20:
            print_with_tap(var, n_tap=inner)
    else:
        print_with_tap(var, n_tap=inner)
    print()


def print_with_tap(*args, n_tap=0):
    print("\t" * n_tap, end="")
    print(*args)


def get_map_data(env):
    """
    Return
    ------
    agents_locs : ndarray (2, 4) int32
    world_size : tuple (2,)
    stone_map : ndarray (25, 25) float64
    wood_map : ndarray (25, 25) float64
    water_map : ndarray (25, 25) float64
    house_maps : ndarray (4, 25, 25) float64
    """
    agent_locs = None
    world_size = None
    stone_map = None
    wood_map = None
    water_map = None
    house_maps = None

    # return 1: agent_locs
    agent_locs = np.array([agent.loc for agent in env.world.agents])

    # return 2: world_size
    maps = env.world.maps
    world_size = np.array(maps.get("Wood")).shape

    scenario_entities = [k for k in maps.keys() if "source" not in k.lower()]
    for entity in scenario_entities:
        if entity == "House":
            continue
        elif resources.has(entity):  # Stone, Wood
            if resources.get(entity).collectible:
                resource_locs = maps.get(entity)
                if entity == "Stone":
                    # return 3: stone_map
                    stone_map = resource_locs
                elif entity == "Wood":
                    # return 4: wood_map
                    wood_map = resource_locs
                else:
                    raise ValueError("Unknown Resource")
        elif landmarks.has(entity):  # Water
            if entity == "Water":
                # return 5: water_map
                water_map = maps.get(entity)
            else:
                raise ValueError("Unknown Landmarks")
        else:
            raise ValueError("Unknown Entity")

    # return 6: house_maps
    house_idx = maps.get("House", owner=True)
    n_agents = len(agent_locs)
    house_maps = np.zeros(shape=(n_agents, *world_size))
    for i in range(n_agents):
        house_maps[i][house_idx == i] = 1

    return (
        agent_locs,
        world_size,
        stone_map,
        wood_map,
        water_map,
        house_maps
    )


def print_map_data_shape(map_data):
    # agents_locs : ndarray (2, 4) int32
    # world_size : tuple (2,)
    # stone_map : ndarray (25, 25) float64
    # wood_map : ndarray (25, 25) float64
    # water_map : ndarray (25, 25) float64
    # house_maps : ndarray (4, 25, 25) float64
    agent_locs, world_size, stone_map, wood_map, water_map, house_maps = map_data
    print("agent_locs")
    print_type(agent_locs)
    print()

    print("world_size")
    print_type(world_size)
    print()

    print("stone_map")
    print_type(stone_map)
    print()

    print("wood_map")
    print_type(wood_map)
    print()

    print("water_map")
    print_type(water_map)
    print()

    print("house_maps")
    print_type(house_maps)
    print()
