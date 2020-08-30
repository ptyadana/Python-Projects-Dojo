ENVIRNOMENT = "dev"


def fetch_data_real():
    print("doing some time intensive operations...")


def fetch_data_fake():
    print("returning fake data...")
    return {
        "name": "Jane Doe",
        "age": 32
    }


fetch_data = fetch_data_real if ENVIRNOMENT == 'prod' else fetch_data_fake
data = fetch_data()
print(data)
