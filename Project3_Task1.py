from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import time
import sys

# Prompt user for path to file and name of file.
file_path = input("Enter a file path to create files of varying size.")
file_name = input("Enter a name for the files.  Example: file")

# Create a 16B (128bits), 1kB, and 3kB file.
file = open(file_path + "16B_" + file_name, "wb")
file.seek(16-1)
file.write(b"\0")
file.close()

file = open(file_path + "1kB_" + file_name, "wb")
file.seek(1000-1)
file.write(b"\0")
file.close()

file = open(file_path + "3kB_" + file_name, "wb")
file.seek(3000-1)
file.write(b"\0")
file.close()

# SHA256 used below.
print("Below is hashed with SHA256.")

# Open 16B file and read contents.
file = open(file_path + "16B_" + file_name, "rb")
message = file.read()
file.close()

print("True size of 16B message is " + str(sys.getsizeof(message)) + "B")

# Start timer.
start_time = time.time()
seconds = 1
counter = 0

# Hash 16B file for 1 second and output number of hashes.
while True:
    # Set timer and counter.
    current_time = time.time()
    elapsed_time = current_time - start_time
    counter += 1

    # Hash
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(message)
    digest.finalize()

    # Write hash to file.
    file = open(file_path + "16B_" + file_name, "wb")
    file.write(message)
    file.close()

    if elapsed_time > seconds:
        # Output number of hashes once 1 second elapsed.
        print("16B hashed " + str(counter) + " times in 1 second.")
        break


# Open 1kB file and read contents.
file = open(file_path + "1kB_" + file_name, "rb")
message = file.read()
file.close()

print("True size of 1kB message is " + str(sys.getsizeof(message)) + "B")

# Start timer.
start_time = time.time()
seconds = 1
counter = 0

# Hash 1kB file for 1 second and output number of hashes.
while True:
    # Set timer and counter.
    current_time = time.time()
    elapsed_time = current_time - start_time
    counter += 1

    # Hash
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(message)
    digest.finalize()

    # Write hash to file.
    file = open(file_path + "1kB_" + file_name, "wb")
    file.write(message)
    file.close()

    if elapsed_time > seconds:
        # Output number of hashes once 1 second elapsed.
        print("1kB hashed " + str(counter) + " times in 1 second.")
        break

# Open 3kB file and read contents.
file = open(file_path + "3kB_" + file_name, "rb")
message = file.read()
file.close()

print("True size of 3kB message is " + str(sys.getsizeof(message)) + "B")

# Start timer.
start_time = time.time()
seconds = 1
counter = 0

# Hash 3kB file for 1 second and output number of hashes.
while True:
    # Set timer and counter.
    current_time = time.time()
    elapsed_time = current_time - start_time
    counter += 1

    # Hash
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(message)
    digest.finalize()

    # Write hash to file.
    file = open(file_path + "3kB_" + file_name, "wb")
    file.write(message)
    file.close()

    if elapsed_time > seconds:
        # Output number of hashes once 1 second elapsed.
        print("3kB hashed " + str(counter) + " times in 1 second.")
        break

# Blake2b hash used below.
print("Below is hashed with BLAKE2b.")

# Open 16B file and read contents.
file = open(file_path + "16B_" + file_name, "rb")
message = file.read()
file.close()

print("True size of 16B message is " + str(sys.getsizeof(message)) + "B")

# Start timer.
start_time = time.time()
seconds = 1
counter = 0

# Hash 16B file for 1 second and output number of hashes.
while True:
    # Set timer and counter.
    current_time = time.time()
    elapsed_time = current_time - start_time
    counter += 1

    # Hash
    digest = hashes.Hash(hashes.BLAKE2b(64), backend=default_backend())
    digest.update(message)
    digest.finalize()

    # Write hash to file.
    file = open(file_path + "16B_" + file_name, "wb")
    file.write(message)
    file.close()

    if elapsed_time > seconds:
        # Output number of hashes once 1 second elapsed.
        print("16B hashed " + str(counter) + " times in 1 second.")
        break


# Open 1kB file and read contents.
file = open(file_path + "1kB_" + file_name, "rb")
message = file.read()
file.close()

print("True size of 1kB message is " + str(sys.getsizeof(message)) + "B")

# Start timer.
start_time = time.time()
seconds = 1
counter = 0

# Hash 1kB file for 1 second and output number of hashes.
while True:
    # Set timer and counter.
    current_time = time.time()
    elapsed_time = current_time - start_time
    counter += 1

    # Hash
    digest = hashes.Hash(hashes.BLAKE2b(64), backend=default_backend())
    digest.update(message)
    digest.finalize()

    # Write hash to file.
    file = open(file_path + "1kB_" + file_name, "wb")
    file.write(message)
    file.close()

    if elapsed_time > seconds:
        # Output number of hashes once 1 second elapsed.
        print("1kB hashed " + str(counter) + " times in 1 second.")
        break

# Open 3kB file and read contents.
file = open(file_path + "3kB_" + file_name, "rb")
message = file.read()
file.close()

print("True size of 3kB message is " + str(sys.getsizeof(message)) + "B")

# Start timer.
start_time = time.time()
seconds = 1
counter = 0

# Hash 3kB file for 1 second and output number of hashes.
while True:
    # Set timer and counter.
    current_time = time.time()
    elapsed_time = current_time - start_time
    counter += 1

    # Hash
    digest = hashes.Hash(hashes.BLAKE2b(64), backend=default_backend())
    digest.update(message)
    digest.finalize()

    # Write hash to file.
    file = open(file_path + "3kB_" + file_name, "wb")
    file.write(message)
    file.close()

    if elapsed_time > seconds:
        # Output number of hashes once 1 second elapsed.
        print("3kB hashed " + str(counter) + " times in 1 second.")
        break
