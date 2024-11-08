from locust import HttpUser, task

class LoadTest(HttpUser):

    @task
    def post_request(self):

        headers={
            'X-TLS-Client-CN': 'CHANGE_IT',
            'X-Firmware-Version': 'v7.6.1-9'
        }
        payload= {
            "udp_download": [],
            "udp_upload": [],
            "tcp_download": [],
            "tcp_upload": [],
            "jitter": [  # -> list(SamKnowsDataMapping.jitterMapping)
                {
                    'timestamp': 1729520133002,  # -> optional(epochInstantSeconds),
                    'result': 'OK',  # -> optional(text),
                    'hostname': 'test',  # '-> optional(text),
                    "ip": '104.30.129.50',  # -> optional(NetworkingMappings.ip4),
                    "packet_size": 1,  # -> optional(number),
                    "stream_rate": 64000,  # -> optional(number),
                    # "duration" #-> optional(microseconds),
                    "tx_upstream": 500,  # -> optional(number),
                    "tx_downstream": 500,  # -> optional(number),
                    "rx_upstream": 1,  # -> optional(number),
                    "rx_downstream": 500,  # -> optional(number),
                    "up_jitter": 1,  # -> optional(microseconds),
                    "down_jitter": 0,  # -> optional(microseconds),
                    'latency': 148,  # -> optional(microseconds),
                    "mos": 4.320000171661377,  # -> optional(of(doubleFormat)),
                    "error_code": 0  # -> optional(text),
                    # "eero_code_label" #-> optional(text)
                }
            ]
        }
        with self.client.post("/speedtest_experiments/results", headers=headers, json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status code: {response.status_code}")
