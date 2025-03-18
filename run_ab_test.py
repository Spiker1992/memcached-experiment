import os
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Run Apache Benchmark (ab) test and get average latency from Memcached.')
parser.add_argument('-n', type=int, default=1000, help='Number of requests to perform for the benchmarking session')
parser.add_argument('-c', type=int, default=10, help='Number of multiple requests to perform at a time')
args = parser.parse_args()

# Step 1: Reset Memcached statistics
os.system('python3 reset_memcached_stats.py')

# Step 2: Run Apache Benchmark (ab) test
ab_command = f'ab -n {args.n} -c {args.c} http://localhost:8000/api/cached-data/?format=json'
os.system(ab_command)

# Step 3: Get average latency from Memcached
os.system('python3 get_memcached_latency.py')
