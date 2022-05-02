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


def run(server_ip="localhost", server_port=50051):
    server_ip_port = "{}:{}".format(server_ip, server_port)

    with grpc.insecure_channel(server_ip_port) as channel:
        stub = world_data_pb2_grpc.WorldMapStub(channel)
        map_data = stub.GetWorldMap(world_data_pb2.Time(step=10))

    print(map_data)


if __name__ == '__main__':
    logging.basicConfig()
    run(server_ip="localhost", server_port=50051)
