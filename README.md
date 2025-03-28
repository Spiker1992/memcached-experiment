# Experiments with Memcached

Memcached is one of the most popular caching applications. It's fast, it's simple and can be scaled easily.

What I want to do:
- test what RPS I can expect from a small node (1GB RAM).
- see impact a cluster of nodes has on performance.
- how performance differs between Memcached and Django

When running tests I will track two things: RPS and average latency.

## How to run this project

- Have docker running
- Within CLI go to the root directory
- Within root dir run `docker-compose up -d --build`
- Once docker is up and running, test endpoint can be accessed using `http://localhost:8000/api/cached-data/?format=json`
- Install Apache Benchmark (refer to the next section)
- Run `python3 run_ab_test.py` to run the test
- Pass in `-n` for number of requests and `-c` for concurrency

### Load Testing with Apache Benchmark (ab)

To perform load testing using Apache Benchmark (ab), follow these steps:

1. Install Apache Benchmark (ab) if it's not already installed:

```sh
sudo apt-get install apache2-utils
```

2. Run the load test against the test endpoint:

```sh
ab -n 1000 -c 10 http://localhost:8000/api/cached-data/?format=json
```

- `-n 1000` is the number of requests to perform for the benchmarking session.
- `-c 10` is the number of multiple requests to perform at a time.


## Exploring existing materials online

### Analysis of Memcached performance

https://pages.cs.wisc.edu/~vijayc/papers/memcached.pdf

(I assume it was writen back in Nov 2009 - https://github.com/memcached/memcached/wiki/ReleaseNotes143)

"We look at tuning the e1000 network driver for memcached - Interrupt blanking, where the system is nonresponsive to interrupts for a period of time; Opportunistic
polling, which switches between polling and interrupts for
I/O based on the load; We look at modifying the number of
buffers for transmitting and receiving packets and the delays
associated with transmitting and receiving packets."

This was tested on 1-4GB RAM machines

### Example of a benchmark on a larger machine

https://memcached.org/blog/persistent-memory/

2x Xeon Cascade Lake CPUs (24 cores, 48 hyperthreads each)
12 x 16GB (192GB) of DDR4 RAM

Very nice example of a performance article on this subject

### How to benchmark the performance of memcached on ubuntu

https://medium.com/swlh/the-complete-guide-to-benchmark-the-performance-of-memcached-on-ubuntu-16-04-71edeaf6e740

Article shares what tools to use to benchmark Memcached performance on Ubunutu

### Example looking at different caching application within Laravel

https://www.georgebuckingham.com/articles/laravel-cache-driver-performance/

Tests were run on 1GB RAM / 1 CPU machines.

This is more on the lines of what I want to do but with Django.

I may borrow authors test setup when I get to simulating traffic.

### Example of a benefit that caching brings 

https://stackoverflow.com/a/829260

This comment highlights the benefit of caching really nicely.

"The difference was like 150 requests/second to 30000 requests/second and the database queries dropped to 1-2 per page."

## Journal

### Getting a feel for running tests

I run several tests to see what performance is like. I did multiple tests with different number and concurrency. 

Quickly I saw that the bottleneck is Gunicorn, which is struggling to handle more than 500rps. Whilst memcached RAM didnt shift, however CPU did hit 30%. Memcached latency was at under 0.15ms in all tests that I run.

For the next step I want to break memcached. Be it by increasing RPS that gunicorn can handle or decreasing Memcached performance by adding larger and different data to the memory.