from locust import task, events
from locust_plugins.users.grpc import GrpcUser
import olap_pb2

def main():
    request = olap_pb2.GetDnsRttAggregatedEventsRequest(network_id=1, start_time=1746531548, end_time=1749209948)
    print(request)

main()