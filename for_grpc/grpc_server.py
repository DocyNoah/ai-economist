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
import logging

import grpc
from protos import world_data_pb2
from protos import world_data_pb2_grpc

import numpy as np


class WorldMapServicer(world_data_pb2_grpc.WorldMapServicer):
    def __init__(self):
        self.call_count = 0
        print("Initialize the server")

    def GetWorldMap(self, request, context):
        self.call_count += 1
        print("call_count: {}".format(self.call_count))

        # agent_locs
        agent_locs = self._get_agnet_locs()

        # world_size
        world_size = world_data_pb2.Pair(row=25, col=25)

        # map
        stone_map = world_data_pb2.Map1DArray(f=self._get_map())
        wood_map = world_data_pb2.Map1DArray(f=self._get_map())
        water_map = world_data_pb2.Map1DArray(f=self._get_map())
        house_maps = world_data_pb2.Map1DArray(f=self._get_map())

        map_data = world_data_pb2.MapData(
            agent_locs=agent_locs,
            world_size=world_size,
            stone_map=stone_map,
            wood_map=wood_map,
            water_map=water_map,
            house_maps=house_maps
        )
        return map_data

    def _get_agnet_locs(self):
        agent_locs = [[11, 12], [21, 22]]
        for agent_loc in agent_locs:
            yield world_data_pb2.Pair(row=agent_loc[0], col=agent_loc[1])

    def _get_map(self, _map: np.ndarray = None):
        _map = np.array(
            [[11, 12, 13],
             [21, 22, 23],
             [31, 32, 33]]
        )
        map_1d_array = _map.flatten()
        for num in map_1d_array:
            yield num


def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    world_data_pb2_grpc.add_WorldMapServicer_to_server(WorldMapServicer(), server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve(port=50051)
