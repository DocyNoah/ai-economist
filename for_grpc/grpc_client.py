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


def run(server_ip="localhost", server_port=50051):
    server_ip_port = "{}:{}".format(server_ip, server_port)

    with grpc.insecure_channel(server_ip_port) as channel:
        stub = world_data_pb2_grpc.WorldMapStub(channel)
        map_data = stub.GetWorldMap(world_data_pb2.Time(step=10))

    ################
    #  agent_locs  #
    ################
    # print(map_data.agent_locs)
    agent_locs = []
    for agent_loc in map_data.agent_locs:
        agent_locs.append([agent_loc.row, agent_loc.col])
    print(agent_locs)

    ################
    #  world_size  #
    ################
    # print(map_data.world_size)
    world_size = (map_data.world_size.row, map_data.world_size.col)
    print(world_size)

    ###############
    #  stone_map  #
    ###############
    # print(map_data.stone_map)
    stone_map = []
    for i in map_data.stone_map.f:
        stone_map.append(i)
    stone_map = np.array(stone_map)
    stone_map = stone_map.reshape((25, 25))
    print(stone_map.shape)

    ##############
    #  wood_map  #
    ##############
    # print(map_data.wood_map)
    wood_map = []
    for i in map_data.wood_map.f:
        wood_map.append(i)
    wood_map = np.array(wood_map)
    wood_map = wood_map.reshape((25, 25))
    print(wood_map.shape)

    ###############
    #  water_map  #
    ###############
    # print(map_data.water_map)
    water_map = []
    for i in map_data.water_map.f:
        water_map.append(i)
    water_map = np.array(water_map)
    water_map = water_map.reshape((25, 25))
    print(water_map.shape)

    ###############
    #  house_map  #
    ###############
    # print(map_data.house_maps)
    house_maps = []
    for house_map in map_data.house_maps:
        for i in house_map.f:
            house_maps.append(i)
    house_maps = np.array(house_maps)
    house_maps = house_maps.reshape((4, 25, 25))
    print(house_maps.shape)


if __name__ == '__main__':
    logging.basicConfig()
    run(server_ip="localhost", server_port=50051)
