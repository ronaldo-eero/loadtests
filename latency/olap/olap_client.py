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

