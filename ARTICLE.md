# Incorporating fault-tolerance into your microsevice design
Fault-tolerance is an essential trait of every microservice architecture. The reasons are plain simple: After integration points in our system reach a certain number, failures are going to happen on a daily basis. The reasons are simply statistical. As I will show it to the reader, we can't defy the laws of mathematics.

That's why we need to understand the key drivers of failures from a higher perspective. It's required to make strategic decisions effectively. Without these decisions it's impossible to achieve the level of fault-tolerance we aim for. 

# Understanding total system availability
We will look at two simple examples to understand how dependency between each component will affect the whole system's availabilty. In brief, you can connect each one of them either in series or in parallel.

# Serial - e.g. application & database
# Parallel - e.g. load balancer

Not just circuit breakers or service mesh
// TODO GRPC features covering these
// TODO Istio features covering these

# Decomposing your services
## Mesh and star

## CRUD services
https://azure.microsoft.com/en-us/blog/microservices-an-application-revolution-powered-by-the-cloud/
https://www.edureka.co/blog/microservices-design-patterns#Branch

# Some fault-tolerance patterns and their possible effect
## retries
[Cassandra rapid read protection][cassandra-read-protection]
[gRPC retries][grpc-retries]
## fallback
## defaults

# Summary
Each additional integration point has an additional cost, that needs to be mitigated. Here's a checklist on what to evaluate on each of the connections:

- Timeouts
- Retry policy
- Periodic connection validation
-- Connection pool rotation
- Circuit breakers
- ...

# Out of scope
[Traefik]: https://docs.traefik.io/v2.0/middlewares/ratelimit/
[CNCF proxies]: https://landscape.cncf.io/category=service-proxy&format=card-mode&grouping=category&license=open-source


# References
https://eventhelix.com/RealtimeMantra/FaultHandling/system_reliability_availability.htm
https://eventhelix.com/RealtimeMantra/FaultHandling/reliability_availability_basics.htm
https://www.os3.nl/_media/2013-2014/courses/rp1/p17_report.pdf

[cassandra-read-protection]: https://docs.datastax.com/en/archived/cassandra/3.0/cassandra/dml/dmlClientRequestsRead.html
[grpc-retries]: https://github.com/grpc/proposal/blob/master/A6-client-retries.md