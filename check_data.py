import numpy as np
import os

bin_file = "/home/lars/T7/Masterarbeit/Datasets/oxford-spires-dataset/oxford_spires_scans/bin/sequences/01/velodyne/00000.bin"
poses_file = "/home/lars/T7/Masterarbeit/Datasets/oxford-spires-dataset/oxford_spires_scans/bin/sequences/01/poses.txt"

print(f"Checking {bin_file}...")
try:
    data = np.fromfile(bin_file, dtype=np.float32)
    print(f"Total floats: {len(data)}")
    data = data.reshape(-1, 4)
    print(f"Total points: {data.shape[0]}")
    print(f"First point: {data[0]}")
    print(f"Has NaNs: {np.isnan(data).any()}")
    print(f"Max values:\n{np.max(data, axis=0)}")
    print(f"Min values:\n{np.min(data, axis=0)}")
except Exception as e:
    print(f"Error reading bin: {e}")

print(f"\nChecking {poses_file}...")
try:
    poses = np.loadtxt(poses_file)
    print(f"Total poses: {poses.shape[0]}")
    print(f"First pose:\n{poses[0]}")
except Exception as e:
    print(f"Error reading poses: {e}")
