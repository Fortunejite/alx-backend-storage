import redis

# Import the Cache class from the exercise module
Cache = __import__('exercise').Cache

# Create a Cache instance
cache = Cache()

# Data to store in Redis
data = b"hello"
# Call the store method to store the data and get the key
key = cache.store(data)
print(key)

# Use the same Redis instance to retrieve the data
result = cache._redis.get(key)
print(result)