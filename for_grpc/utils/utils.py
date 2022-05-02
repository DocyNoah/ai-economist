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


def get_visualize_data(env):
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
    # return 1: agent_locs
    agent_locs = np.array([agent.loc for agent in env.world.agents])
    n_agents = len(agent_locs)

    maps = env.world.maps
    # return 2: world_size
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

    house_idx = maps.get("House", owner=True)
    agent_idx = tuple(range(n_agents))

    # return 6: house_maps
    house_maps = np.zeros(shape=(n_agents, *world_size))
    for i in range(n_agents):
        house_maps[i][house_idx == i] = 1

    return (
        agent_locs,
        world_size,
        stone_map,
        wood_map,
        water_map,
        house_maps,
    )
