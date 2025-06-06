import inspect
import sys
import time

from locust import events, User, between, task, FastHttpUser, constant, constant_throughput

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


def stopwatch(func):
    """To be updated"""

    def wrapper(*args, **kwargs):
        """To be updated"""
        # get task's function name
        previous_frame = inspect.currentframe().f_back
        _, _, task_name, _, _ = inspect.getframeinfo(previous_frame)

        start = time.time()
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            total = int((time.time() - start) * 1000)
            print(f"exception {e}")
            events.request.fire(request_type="TYPE",
                                        name=task_name,
                                        response_time=total,
                                        response_length=0,
                                        exception=e)
        else:
            print("success")
            total = int((time.time() - start) * 1000)
            events.request.fire(request_type="TYPE",
                                        name=task_name,
                                        response_time=total,
                                        response_length=0)
        return result

    return wrapper

class OlapGrpcLocustUser(FastHttpUser):
    host = 'localhost'


    #wait_time = constant(0)
    wait_time = constant_throughput(19)
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task
    @stopwatch
    def grpc_client_task(self):
        """To be updated"""
        network_id = 908110
        start = 1746533620
        end = 1749212020
        try:
            with grpc.insecure_channel("localhost:9000") as channel:
                stub = olap_pb2_grpc.OLAPServiceStub(channel)
                request = olap_pb2.GetDnsRttAggregatedEventsRequest(network_id=network_id, start_time=start, end_time=end)
                response = stub.GetDnsRttAggregatedEvents(request)
                print(response)
        except (KeyboardInterrupt, SystemExit):
            sys.exit(0)