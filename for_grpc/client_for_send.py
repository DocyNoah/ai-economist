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

from __future__ import print_function

import logging

import grpc
from protos import world_data_pb2
from protos import world_data_pb2_grpc

import numpy as np


class EcoClient:
    def __init__(self, server_ip, server_port):
        self.server_ip_port = "{}:{}".format(server_ip, server_port)
        self.channel = grpc.insecure_channel(self.server_ip_port)
        self.stub = world_data_pb2_grpc.AIEconomistStub(self.channel)

    def send_data(self, data):
        decomposed_data = self._decompose(data)
        self.stub.SendWorldMap(decomposed_data)

    def _decompose(self, data):
        _agent_locs, _world_size, _stone_map, _wood_map, _water_map, _house_maps = data

        # agent_locs
        agent_locs = self._get_agnet_locs(_agent_locs)

        # world_size
        world_size = world_data_pb2.Pair(row=25, col=25)

        # map
        stone_map = self._get_map_1d_array(_stone_map)
        wood_map = self._get_map_1d_array(_wood_map)
        water_map = self._get_map_1d_array(_water_map)
        house_maps = self._get_maps_1d_array(_house_maps)

        map_data = world_data_pb2.MapData(
            agent_locs=agent_locs,
            world_size=world_size,
            stone_map=stone_map,
            wood_map=wood_map,
            water_map=water_map,
            house_maps=house_maps
        )
        return map_data

    def _get_agnet_locs(self, agent_locs):
        for agent_loc in agent_locs:
            yield world_data_pb2.Pair(row=agent_loc[0], col=agent_loc[1])

    def _get_map_1d_array(self, _map: np.ndarray):
        return world_data_pb2.Map1DArray(f=self._get_map(_map))

    def _get_map(self, _map: np.ndarray):
        map_1d_array = _map.flatten()
        for num in map_1d_array:
            yield num

    def _get_maps_1d_array(self, _maps: np.ndarray):
        for _map in _maps:
            yield world_data_pb2.Map1DArray(f=self._get_map(_map))
