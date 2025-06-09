import random
from datetime import datetime

from locust import task

import grpc_user
import olap_pb2
import olap_pb2_grpc

network_ids = [
    858560,
    909244,
    692157,
    896948,
    531269,
    880440,
    537964,
    537958,
    537962,
    537960
]

class HelloGrpcUser(grpc_user.GrpcUser):
    host = "localhost:9000"
    stub_class = olap_pb2_grpc.OLAPServiceStub

    @task
    def sayHello(self):
        random_network_id = random.choice(network_ids)
        start_time = datetime.strptime('2025-05-01', "%Y-%m-%d")
        end_time = datetime.strptime('2025-06-01', "%Y-%m-%d")
        self.stub.GetDnsRttAggregatedEvents(olap_pb2.GetDnsRttAggregatedEventsRequest(
            network_id=random_network_id,
            start_time=int(start_time.timestamp()),
            end_time=int(end_time.timestamp())
        ))