class mqProducerInterface:
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        # Save parameters to class variables

        # Call setupRMQConnection
        pass

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        
        # Establish Channel

        # Create the exchange if not already present

        pass

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange

        # Close Channel

        # Close Connection
    
        pass