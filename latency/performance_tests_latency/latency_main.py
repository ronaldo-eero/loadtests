import requests
import latency_pb2
import time

from google.protobuf.wrappers_pb2 import StringValue

def create_latency():
    action_result = latency_pb2.ActionResult()
    action_result.status = latency_pb2.ActionResultStatus.SUCCESS
    print("hey")
    print(action_result.status)
    print("hey")
    result = latency_pb2.LatencyActionResult()
    latency = result.latency.add()

    # prefix = StringValue(value='prefix')
    # latency.prefix.CopyFrom(prefix)
    errorCode = StringValue(value='ERROR_CODE_NO_SERVER_RESPONDING')
    latency.errorCode.CopyFrom(errorCode)
    target = StringValue(value='myawesometest.com')
    latency.target.CopyFrom(target)

    epoch_seconds = str(int(time.time()))
    timestamp_string = StringValue(value=epoch_seconds)
    latency.timestamp.CopyFrom(timestamp_string)

    latency.result.CopyFrom(StringValue(value='FAIL'))

    action_result.latency_action_result.CopyFrom(result)

    return action_result

def main():
    payload = create_latency()
    serialized_payload = payload.SerializeToString()
    print(payload)

    # url = "http://localhost:9000/action/performance_tests/latency_test/01972a25-a126-71e0-af3c-721501e5d642"
    url = "http://localhost:9000/action/performance_tests/latency_test/01971588-78a0-72e9-b690-49daf6e22e9b"
    headers = {
        "Content-Type": "application/protobuf",
        "X-Firmware-Version": "v7.10.0-6631",
        # "X-TLS-Client-CN": "3.ERO0018638409.SES0004134833.CRT01387020450160395447"
        "X-TLS-Client-CN": "3.ERO0023654166.SES0003542721.CRT01379260887513256599"
    }

    try:
        response = requests.post(url, data=serialized_payload, headers=headers)

        # Parse the response
        if response.status_code == 200:
            print("\nServer response success")
        else:
            print(f"\nRequest failed with status code: {response.status_code}")
            print(f"Response content: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

    print(payload)

main()