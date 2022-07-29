# Kafka Project
Test Project using Kafka to process a continuous stream of messages generated with Faker, and store them to a remote SQL DB in microbatches (typically either in routine intervals or every `x` messages.)

The Data Producer could be switched out to fetch data from any real-time API that sends a continuous stream of messages.  The Consumer can also be setup to write the messages to some destination besides SQL, like S3 or DynamoDB.
