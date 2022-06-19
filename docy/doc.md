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
    - Stone (also is one of the commodities)
    - Wood (also is one of the commodities)
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
  - components_dim: dict[str: Component]
  - resources: list[str]
  - landmarks: list[str]
  - endogenous: list[str]
  - all_agents: list[BaseAgent]
  - dense_log
  - replay_log
  - previous_episode_dense_log
  - previous_episode_replay_log
  - world: World
    - world_size: tuple
    - n_agents: int
    - multi_action_mode_agents: bool
    - multi_action_mode_planner: bool
    - resources: list[str]
    - landmarks: list[str]
    - agents: list[BasicMobileAgent]
    - planner: BasicPlanner
    - loc_map: ndarray
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

- LayoutFromFile
  - layout_specs
  - starting_agent_coin
  - isoelastic_eta
  - energy_cost
  - agent_starting_pos

- BaseAgent
  - action: dict[str(component_name): action_n]
  - action_dim: dict[str(component_name): n_actions]
  - single_action_map: dict[int: list(str(component_name): action_n)]
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

- ContinuousDoubleAuction
  - n_actions: list[tuple(str, int)]
  - order_labor: float
  - max_bid_ask: int
  - price_floor: int
  - price_ceiling: int
  - order_duration: int
  - max_num_orders: int
  - commodities: list[Resource]
  - asks: dict[Resource: list[dict{"seller": agent.idx, "ask": int(min_income), "ask_lifetime": 0}]]
    - ask 호가 instances
  - bids: dict[Resource: list[dict{"buyer": agent.idx, "bid": int(max_payment), "bid_lifetime": 0}]]
    - bid 호가 instances
  - n_orders: dict[Resource: dict[int(agent_idx): int]]
  - price_history: dict[Resource: dict[int(agent_idx): ndarray]]
    - 상한가부터 하한가 내에서 가격별로 자신이 판매한 횟수
  - ask_hists: dict[Resource: dict[int(agent_idx): ndarray]]
    - resouce별 agent별 ask 호가 현황
  - bid_hists: dict[Resource: dict[int(agent_idx): ndarray]]
    - resouce별 agent별 bid 호가 현황

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


### env.\__init\__()
foundation.base.base_env.BaseEnvironment.reset()

- Initialize members
- agent.register_*()
  - agent.register_components()
    - agent._incorporate_component()


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
  - component.additional_reset_steps()
- self.all_agents.reset_actions()
- obs = self._generate_observations()
  - obs = {'0': {}, '1': {}, '2': {}, '3': {}, 'p': {}}
  - self.generate_observations()
    - implement at layout_from_file.py
  - components.obs()
    - components.generate_observations()


### env.step()
```pycon
obs = env.step(actions)
```

- self.all_agents.parse_actions(agent_actions)
  - set actions
- self.components.step()
  - take actions
- self.scenario_step()
  - spawn resources
- obs = self._generate_observations()
- rew = self._generate_rewards()
- done = {"\__all\__": self.world.timestep >= self._episode_length}
- info = {k: {} for k in obs.keys()}
- self.all_agents.reset_actions()