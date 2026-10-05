import numpy as np


rooms = ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]

np.random.seed(42)
temperatures = 22 + 3 * np.random.randn(4, 48)

print("\n1. Data type inspection and conversion")
print("dtype:", temperatures.dtype)
print("shape:", temperatures.shape)
print("size:", temperatures.size)

temp_int = temperatures.astype(np.int8)
print("First row (float):", np.round(temperatures[0], 2))
print("First row (int8):", temp_int[0])

print("\n2. Generating timestamps with linspace and arange")
times1 = np.linspace(0, 24, 48, endpoint=False)
times2 = np.arange(0, 24, 0.5)

print("linspace first 6:", times1[:6])
print("arange first 6:", times2[:6])
print("linspace == arange ?", np.allclose(times1, times2))

print("\n3. Negative indexing")
print("Bathroom - last 3 readings:", np.round(temperatures[-1, -3:], 2))
print("LivingRoom - last reading:", round(temperatures[0, -1], 2))
print("Last room name:", rooms[-1])

print("\n4. Fancy indexing")
selected = [0, 2]
subset = temperatures[selected]
night = subset[:, :12]

print("Subset shape:", subset.shape)
print(np.round(subset, 2))
print("Night-window subset shape:", night.shape)
print(np.round(night, 2))

print("\n5. Anomaly detection with ndenumerate")
anomalies = []

for (room_no, time_no), value in np.ndenumerate(temperatures):
    if value < 18 or value > 28:
        anomalies.append((rooms[room_no], times1[time_no], value))

print("Anomalies found:", len(anomalies))

for item in anomalies:
    print(f"({item[0]} {item[1]:.1f}h {item[2]:.2f}C)")

print("\n6. Locating a threshold with searchsorted")
living_sorted = np.sort(temperatures[0])
position = np.searchsorted(living_sorted, 25.0)

print("Insertion position for 25.0 in sorted LivingRoom:", position)
print("Readings of LivingRoom below 25.0C:", position, "of", len(living_sorted))

print("\n7. Reverse sorting rooms by average temperature")
averages = np.mean(temperatures, axis=1)
order = np.argsort(averages)[::-1]

print("Rooms ranked warmest -> coldest:")
for i in order:
    print(rooms[i], f"{averages[i]:.2f}C")

print("\n8. Splitting the day into time windows")
morning, afternoon, evening = np.hsplit(temperatures, 3)

print("Morning shape", morning.shape, "mean", f"{np.mean(morning):.2f}C")
print("Afternoon shape", afternoon.shape, "mean", f"{np.mean(afternoon):.2f}C")
print("Evening shape", evening.shape, "mean", f"{np.mean(evening):.2f}C")

print("\n9. Joining arrays in multiple directions")
next_half = 22 + 3 * np.random.randn(4, 24)
joined1 = np.hstack((temperatures, next_half))
print("hstack shape:", joined1.shape)

hallway = 22 + 3 * np.random.randn(1, 48)
joined2 = np.concatenate((temperatures, hallway), axis=0)
print("concatenate shape:", joined2.shape)

day2 = 22 + 3 * np.random.randn(4, 48)
joined3 = np.dstack((temperatures, day2))
print("dstack shape, ndim:", joined3.shape, joined3.ndim)

print("\n10. Automatic reshaping with reshape(-1)")
flat = temperatures.reshape(-1)
new_shape = flat.reshape(8, -1)

print("Flattened shape:", flat.shape)
print("Reshaped shape:", new_shape.shape)
