# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from concurrent import futures

import grpc
from docy.for_unity.about_grpc import world_data_pb2_grpc, world_data_pb2

import numpy as np
import time


class AIEconomistDataCenter(world_data_pb2_grpc.AIEconomistServicer):
    def __init__(self, queue):
        self.queue = queue
        self.call_count = 0
        print("Initialize the server")

    def GetWorldMap(self, request, context):
        self.call_count += 1
        print("call_count: {}".format(self.call_count))

        # get data
        while self.queue.empty():
            time.sleep(0.5)

        data = self.queue.get()
        # data = get_visualize_data(self.env)

        _agent_locs, _world_size, _stone_map, _wood_map, _water_map, _house_maps = data

        # agent_locs
        agent_locs = self._get_agent_locs(_agent_locs)

        # world_size
        world_size = world_data_pb2.Pair(row=25, col=25)

        # map
        stone_map  = self.get_map_1d_array(_stone_map)
        wood_map   = self.get_map_1d_array(_wood_map)
        water_map  = self.get_map_1d_array(_water_map)
        house_maps = self.get_maps_1d_array(_house_maps)

        map_data = world_data_pb2.MapData(
            agent_locs=agent_locs,
            world_size=world_size,
            stone_map=stone_map,
            wood_map=wood_map,
            water_map=water_map,
            house_maps=house_maps
        )
        return map_data

    @staticmethod
    def _get_agent_locs(agent_locs):
        for agent_loc in agent_locs:
            yield world_data_pb2.Pair(row=agent_loc[0], col=agent_loc[1])

    def get_map_1d_array(self, _map: np.ndarray):
        return world_data_pb2.Map1DArray(f=self.get_map(_map))

    @staticmethod
    def get_map(_map: np.ndarray):
        map_1d_array = _map.flatten()
        for num in map_1d_array:
            yield num

    def get_maps_1d_array(self, _maps: np.ndarray):
        for _map in _maps:
            yield world_data_pb2.Map1DArray(f=self.get_map(_map))


def serve(port, queue):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    world_data_pb2_grpc.add_AIEconomistServicer_to_server(
        AIEconomistDataCenter(queue), server
    )
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()
    # server.wait_for_termination()


class AIEconomistServer:
    def __init__(self, port, queue):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        world_data_pb2_grpc.add_AIEconomistServicer_to_server(
            AIEconomistDataCenter(queue), self.server
        )
        self.server.add_insecure_port('[::]:{}'.format(port))

    def start(self):
        self.server.start()

    def wait_for_termination(self):
        self.server.wait_for_termination()


# if __name__ == '__main__':
#     # logging.basicConfig()
#     # serve(port=50051, env=None)
#
#     server = AIEconomistServer(port=50051, env=None)
#     server.start()
#     print("server start")
#     server.wait_for_termination()
