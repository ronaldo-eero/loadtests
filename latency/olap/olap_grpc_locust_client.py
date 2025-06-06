
from datetime import time
from locust import events, User, between, task, constant_throughput

import grpc
import olap_pb2
import olap_pb2_grpc

class OlapClient:
    def __init__(self, host="localhost", port=9000):
        channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = olap_pb2_grpc.OLAPServiceStub(channel)

    def getDnsEvents(self, network_id, start, end):
        request = olap_pb2.GetDnsEventsRequest(network_id=network_id, start=start, end=end)
        response = self.stub.GetDnsRttAggregatedEvents(request)
        return response


class OlapGrpcLocustClient:
    def __init__(self):
        self.client = OlapClient()
    def get_dns_events(self, network_id, start, end):
        start_time = time.time()
        try:
            response = self.client.getDnsEvents(network_id, start, end)
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(
                request_type="grpc", name="GetDnsRttAggregatedEvents", response_time=total_time, response_length=len(response)
            )
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="grpc", name="GetDnsRttAggregatedEvents", response_time=total_time, exception=e)

class OlapGrpcLocustUser(User):
    wait_time = constant_throughput(1)

    def on_start(self):
        self.client = OlapGrpcLocustClient()

    @task
    def get_dns_events(self):
        self.client.get_dns_events(network_id=908110, start=1746533620, end=1749212020)