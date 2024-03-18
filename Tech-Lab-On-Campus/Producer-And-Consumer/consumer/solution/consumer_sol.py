import pika
import os

from consumer import consumer_interface
#Inheriting interface
class mqConsumer(consumer_interface):
    def __self__(self, binding_key: str, exchange_name: str, queue_name: str):
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name
    
    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["http://localhost:15672"])
        connection = pika.BlockingConnection(parameters=con_params)
        
        # Establish Channel
        channel = connection.channel()

        # Create Queue if not already present
        channel.queue_declare(queue=self.queue_name)
        # Create the exchange if not already present
        exchange = channel.exchange_declare(exchange="Exchange Name")

        # Bind Binding Key to Queue on the exchange
        channel.queue_bind(
        queue= self.queue_name,
        routing_key= "Routing Key",
        exchange= self.exchange_name,)

        # Set-up Callback function for receiving messages
        channel.basic_consume("Queue Name", Function Name, auto_ack=False)

    def on_message_callback(
    self, channel, method_frame, header_frame, body
    ) -> None:
    # Acknowledge message

    #Print message (The message is contained in the body parameter variable)
    pass

    def startConsuming(self) -> None:
        # Print " [*] Waiting for messages. To exit press CTRL+C"

        # Start consuming messages
        pass
    
    def __del__(self) -> None:
        # Print "Closing RMQ connection on destruction"
        
        # Close Channel

        # Close Connection
        
        pass
