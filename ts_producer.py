import pandas as pd
from kafka import KafkaProducer
from kafka.errors import KafkaError


def main() -> None:
    producer = KafkaProducer(
        bootstrap_servers="localhost:9093",
        compression_type="gzip",
    )

    df = pd.read_csv("./iot_telemetry_data.csv")

    producer.send("ts-to-analyze", df[:1000].to_csv(index=False).encode())

    producer.flush()


if __name__ == "__main__":
    try:
        main()
    except KafkaError as error:
        print(error)
