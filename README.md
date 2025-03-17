# Experiments with Memcached

Memcached is one of the most popular caching applications. It's fast, it's simple and can be scaled.

I want to test what RPS I get expect from a small node (1GB ram).

I also want to see what impact a cluster of nodes would have on performance.

## Exploring existing materials online

- Analysis of Memcached performance
https://pages.cs.wisc.edu/~vijayc/papers/memcached.pdf

(I assume it was writen back in Nov 2009 - https://github.com/memcached/memcached/wiki/ReleaseNotes143)
"We look at tuning the e1000 network driver for memcached - Interrupt blanking, where the system is nonresponsive to interrupts for a period of time; Opportunistic
polling, which switches between polling and interrupts for
I/O based on the load; We look at modifying the number of
buffers for transmitting and receiving packets and the delays
associated with transmitting and receiving packets."

1-4GB RAM

- Example of a benchmark on a larger machine
https://memcached.org/blog/persistent-memory/

2x Xeon Cascade Lake CPUs (24 cores, 48 hyperthreads each)
12 x 16GB (192GB) of DDR4 RAM

- How to benchmark the performance of memcached on ubuntu
https://medium.com/swlh/the-complete-guide-to-benchmark-the-performance-of-memcached-on-ubuntu-16-04-71edeaf6e740

- Example looking at different caching application within Laravel
https://www.georgebuckingham.com/articles/laravel-cache-driver-performance/

1GB RAM / 1 CPU

This is more on the lines of what I want to do with Django.

- Example of a benefit that caching brings 

https://stackoverflow.com/a/829260