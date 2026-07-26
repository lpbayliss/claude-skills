# Notifications RFC

Status: proposed

We will add Kafka so notifications are reliable and fast. Every service publishes messages to Kafka. A worker sends email and push notifications. Failed messages retry a few times. We will monitor the system and roll it out gradually.

Implementation tasks:

1. Add Kafka.
2. Add a worker.
3. Add retries.
4. Add dashboards.
5. Deploy.

Testing: add unit and integration tests.
