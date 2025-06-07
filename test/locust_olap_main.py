from locust import task

import grpc_user
import olap_pb2
import olap_pb2_grpc


class HelloGrpcUser(grpc_user.GrpcUser):
    host = "localhost:9000"
    stub_class = olap_pb2_grpc.OLAPServiceStub

    @task
    def sayHello(self):
        self.stub.GetDnsRttAggregatedEvents(olap_pb2.GetDnsRttAggregatedEventsRequest(network_id=877721, start_time=1746531548, end_time=1749209948))