import grpc
import broker_pb2
import broker_pb2_grpc

def publish_message(topic, data):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = broker_pb2_grpc.BrokerServiceStub(channel)
        request = broker_pb2.PublishRequest(topic=topic, data=data)
        response = stub.Publish(request)
        print("Message published:", response.success)

if __name__ == "__main__":
    topic = "Topic2"
    data = {'message':'Mesaj pentru Topic2'}
    publish_message(topic, data)
