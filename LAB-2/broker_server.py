import grpc
from concurrent import futures
import time
import broker_pb2
import broker_pb2_grpc 

class BrokerService(broker_pb2_grpc.BrokerServiceServicer):
    def __init__(self):
        self.subscribers = {}

    def Subscribe(self, request, context):
        topic = request.topic
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(context)
        print(f"New subscriber for topic: {topic}")

        try:
            while True:
                message = context.peer()
                if message is None:
                    break
        except grpc.RpcError:
            print(f"Subscriber disconnected from topic {topic}")

    def Publish(self, request, context):
        topic = request.topic
        data = request.data
        print(f"Received message on topic '{topic}': {data}")

        if topic in self.subscribers:
            for subscriber_context in self.subscribers[topic]:
                try:
                    subscriber_context.send_message(
                        broker_pb2.Message(topic=topic, data=data))
                except Exception as e:
                    print(f"")

        return broker_pb2.PublishResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    broker_pb2_grpc.add_BrokerServiceServicer_to_server(BrokerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Broker gRPC server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
