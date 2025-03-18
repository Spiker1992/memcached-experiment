import os

# Step 1: Reset Memcached statistics
os.system('python3 reset_memcached_stats.py')

# Step 2: Run Apache Benchmark (ab) test
ab_command = 'ab -n 1000 -c 10 http://localhost:8000/api/cached-data/?format=json'
os.system(ab_command)

# Step 3: Get average latency from Memcached
os.system('python3 get_memcached_latency.py')
