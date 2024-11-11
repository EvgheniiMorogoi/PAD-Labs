import grpc
import broker_pb2
import broker_pb2_grpc

def subscribe_to_topic(topic):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = broker_pb2_grpc.BrokerServiceStub(channel)
        request = broker_pb2.SubscriptionRequest(topic=topic)
        response_stream = stub.Subscribe(request)
        
        for message in response_stream:
            print(f"Received message on topic '{message.topic}': {message.data}")

if __name__ == "__main__":
    topic = "Topic2"
    subscribe_to_topic(topic)
