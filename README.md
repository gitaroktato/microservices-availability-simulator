# microservices-availability-simulator
A software that's using Monte Carlo simulation for showing availability of combination of microservices.

# Usage
You need the following libraries installed:
- `networkx`
- `mathplotlib`
- 
See [`main.py`](main.py) as an example on how to use the simulator.
Another detailed example can be found in the [examples](examples/README.md) folder.
I also encourage you to read the [article](https://dzone.com/articles/incorporating-fault-tolerance-into-your-microservi)
I wrote about this topic. It explains everything in detail.

# Screenshots
![screenshot1](docs/service_dependency_graph.png)
![screenshot2](docs/service_dependency_graph_shared_cache.png)

# References

## NxGraph used as a graph library
- https://www.geeksforgeeks.org/python-visualize-graphs-generated-in-networkx-using-matplotlib/


## Whitepapers describing relevant topics
- https://www.csl.cornell.edu/~delimitrou/papers/2019.ispass.qsim.pdf
- https://pdfs.semanticscholar.org/9db6/980f217c4108dc519f35f2d5a1642d3c1421.pdf
- http://perfdynamics.com/Tools/PDQ.html
- https://dzone.com/articles/incorporating-fault-tolerance-into-your-microservi