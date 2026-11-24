import gc
import sys

# Function to create some objects
def create_objects():
    objects = []
    for i in range(1000):
        objects.append([i] * 100)
    return objects

# Function to display memory usage
def display_memory():
    print("Memory usage:", sys.getsizeof(objects), "bytes")

# Display initial memory usage
print("Initial Garbage Collection Status:", gc.isenabled())

# Create objects
objects = create_objects()
print("Objects created successfully")

# Display memory usage
print("Memory before garbage collection:",
      sys.getsizeof(objects), "bytes")

# Enable garbage collection debugging
gc.set_debug(gc.DEBUG_STATS)

# Collect garbage
collected = gc.collect()

print("Garbage collected:", collected, "objects")

# Display memory usage after collection
print("Memory after garbage collection:",
      sys.getsizeof(objects), "bytes")

# Disable garbage collection debugging
gc.set_debug(0)

print("Garbage Collection Completed")
