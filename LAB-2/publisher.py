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
    topic = "Echipa baietilor frumosi si Katerina mai frumoasa"
    data = {'Message':'Mesaj pentru Frumosi'}
    publish_message(topic, data)
