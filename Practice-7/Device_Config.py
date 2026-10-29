def create_device_config(device_id, **kwargs):
    config = {"device_id": device_id}

    for key, value in kwargs.items():
        if key == "baud_rate" or key == "parity" or key == "timeout_ms" or key == "debug":
            config[key] = value
        else:
            print("Unsupported key:", key)
            return None

    return config

result = create_device_config("D01", baud_rate=115200, parity="N", timeout_ms=500)
print(result)
