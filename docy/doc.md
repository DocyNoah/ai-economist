## Class Hierarchy
- BaseEnvironment
  - LayoutFromFile
  - SplitLayout
  - Uniform
    - Quadrant
    - MultiZone
  - OneStepEconomy
  - CovidAndEconomyEnvironment
- BaseComponent
  - Build
  - Gather
  - ContinuousDoubleAuction
- BaseAgent
  - BasicMobileAgent
  - BasicPlanner
- Entities(not class)
  - Endogenous
    - Labor
  - Landmark
    - House
    - Water
    - WoodSourceBlock
    - StoneSourceBlock
  - Resource
    - Stone
    - Wood
    - Coin


## Class Member
- BaseEnvironment
  - world_size: tuple
  - n_agents: int
  - num_agents: int - n_agents + n_planners
  - episode_length: int
  - multi_action_mode_agents: bool
  - multi_action_mode_planner: bool
  - components: list[Component]
  - resources: list[str]
  - landmarks: list[str]
  - endogenous: list[str]
  - all_agents: list[BaseAgent]
  - world: World
    - world_size: tuple
    - n_agents: int
    - multi_action_mode_agents: bool
    - multi_action_mode_planner: bool
    - resources: list[str]
    - landmarks: list[str]
    - agents: list[BasicMobileAgent]
    - maps: Maps
      - _map: dict[Entity: ndarray]
      - _map: dict[Entity: dict["owner": ndarray, "health": ndarray]]
      - size: list
      - n_agents: int
      - resources: list[str]
      - landmarks: list[str]
      - entities: resources + landmarks
      - _blocked: list[str(Landmark)]
      - _private: list[str(Landmark)]
      - _public: list[str(Landmark)]
      - _private_landmark_types == _private
    - planner: BasicPlanner
    - loc_map: ndarray
  - dense_log
  - replay_log
  - previous_episode_dense_log
  - previous_episode_replay_log

- LayoutFromFile
  - layout_specs
  - starting_agent_coin
  - isoelastic_eta
  - energy_cost
  - agent_starting_pos

- BaseAgent
  - action: dict
  - action_dim: dict
  - state: dict(loc=[0, 0], inventory={}, escrow={}, endogenous={})
  - idx: int or str
  - action_spaces: int or ndarray
  - loc: list
  - endogenous: dict
  - inventory: dict
    - i.e. {"Wood": 3, "Stone": 20, "Coin": 1002.83}
  - escrow: dict

- Component
  - reset: func
  - obs: func
  - generate_masks: func
  - component_step: func
  - world: World
  - episode_length: int
  - n_agents: int
  - resources: list[Resource]
  - landmarks: list[Landmark]

- Build
  - n_actions: int = 1
  - skill_dist: str ["none", "pareto", "lognormal"]
  - build_labor: float
  - resource_cost = {"Wood": 1, "Stone": 1}

- Gather
  - n_actions: int = 4
  - skill_dist: str ["none", "pareto", "lognormal"]
  - move_labor: float
  - collect_labor: float

- ContinuousDoubleAuction   - 이 객체를 agent마다 따로따로 가지고 있는지 확인
  - n_actions: list[(str, int)]
  - order_labor: float
  - max_bid_ask: int
  - price_floor: int
  - price_ceiling: int
  - order_duration: int
  - max_num_orders: int
  - commodities: list[Resource]
  - asks: dict[Resource: dict[str: int]]
  - bids: dict[Resource: dict[str: int]]
  - n_orders: dict[Resource: dict[int(agent_idx): int]]
  - price_history: dict[Resource: dict[int(agent_idx): ndarray]]
  - bid_hists
  - ask_hists

- Resource(Wood, Stone, Coin): static class
  - name: str
  - color
  - collectible: bool

- Landmark
  - name: str
  - color
  - ownable: bool
  - solid: bool
  - blocking: bool(solid and not ownable)
    - i.e. Water
  - private: bool(solid and ownable)
    - i.e. House
  - public: bool(not solid and not ownable)
    - i.e. WoodSourceBlock
    - i.e. StoneSourceBlock


## Function
### Env Config

docy.env_config.py


### Make Env

```pycon
from ai_economist import foundation
env = foundation.make_env_instance(**env_config)
```
- ```from ai_economist import foundation```
  - foundation/\__init\__.py
    - ```from ai_economist.foundation.scenarios import scenario_registry as scenarios```
  - foundation/scenarios\__init\__.py
    - ```from ai_economist.foundation.base.base_env import scenario_registry```
  - from ai_economist.foundation.base.base_env.py
    - ```scenario_registry = Registry(BaseEnvironment)```
  - foundation/scenarios\__init\__.py
    - ```from .simple_wood_and_stone import dynamic_layout, layout_from_file```
  - foundation/scenarios/simple_wood_and_stone/layout_from_file.py
    - ```pycon
      @scenario_registry.add
      class LayoutFromFile(BaseEnvironment):
      ```
      == ```scenario_registry.add(LayoutFromFile)```
  - foundation/\__init\__.py
    - ```def make_env_instance(scenario_name, **kwargs):```

- ```env = foundation.make_env_instance(**env_config)```
  - env_config['scenario_name'] == 'layout_from_file/simple_wood_and_stone'
  - foundation/\__init\__.py
    - ```pycon
      def make_env_instance(scenario_name, **kwargs):
          scenario_class = scenarios.get(scenario_name)
          return scenario_class(**kwargs)
      ```
    - scenario_class == foundation.scenarios.simple_wood_and_stone.layout_from_file.LayoutFromFile
  - env == LayoutFromFile()

***

```pycon
env_config['scenario_name'] == 'layout_from_file/simple_wood_and_stone'
from ai_economist import foundation
env = foundation.make_env_instance(**env_config)
```
==
```pycon
env_config['scenario_name'] == 'layout_from_file/simple_wood_and_stone'
scenario_name, **kwargs = **env_config
env = foundation.scenarios.simple_wood_and_stone.layout_from_file.LayoutFromFile(**kwargs)
```


### env.reset()
```pycon
obs = env.reset()
```
foundation.base.base_env.BaseEnvironment.reset()

- self.reset_starting_layout() - abstract
  - i.e. resource & landmark layout
  - implement at layout_from_file.py
- self.reset_agent_states() - abstract
  - i.e. inventory, locations, etc.
  - implement at layout_from_file.py
- self.additional_reset_steps() - optional
  - implement at layout_from_file.py
- self.components.reset()
  - ............................................................................
- self.all_agents.reset()
  - ............................................................................
- obs = self._generate_observations()
  - obs = {'0': {}, '1': {}, '2': {}, '3': {}, 'p': {}}
  - self.generate_observations()
    - implement at layout_from_file.py
    - 


### env.step()
```pycon
obs = env.step(actions)
```

- self.all_agents.parse_actions(agent_actions)
- self.components.step()
- self.scenario_step()
- obs = self._generate_observations()
- rew = self._generate_rewards()
- done = {"\__all\__": self.world.timestep >= self._episode_length}
- info = {k: {} for k in obs.keys()}
- self.all_agents.reset_actions()