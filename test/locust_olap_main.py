from locust import events, task

import gevent
import grpc_user
import olap_pb2
import olap_pb2_grpc
from hello_server import start_server


# Start the dummy server. This is not something you would do in a real test.
@events.init.add_listener
def run_grpc_server(environment, **_kwargs):
    gevent.spawn(start_server)


class HelloGrpcUser(grpc_user.GrpcUser):
    host = "localhost:9000"
    stub_class = olap_pb2_grpc.OLAPServiceStub

    @task
    def sayHello(self):
        self.stub.GetDnsRttAggregatedEvents(olap_pb2.GetDnsRttAggregatedEventsRequest(network_id=877721, start_time=1746531548, end_time=1749209948))