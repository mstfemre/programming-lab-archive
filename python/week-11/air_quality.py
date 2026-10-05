import numpy as np

cities = ['Ankara', 'Istanbul', 'Izmir', 'Bursa', 'Antalya']
days   = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

aqi = np.array([
    [55,  60,  72,  68,  80,  75, 65],   # Ankara
    [90,  95, 110, 105, 120, 100, 85],   # Istanbul
    [40,  45,  50,  55,  60,  50, 42],   # Izmir
    [70,  75,  85,  95, 100,  90, 80],   # Bursa
    [35,  38,  42,  48,  55,  45, 40]    # Antalya
])

# 1. Array properties
print("Shape:", aqi.shape, "  ndim:", aqi.ndim, "  size:", aqi.size)

# 2. Slicing: first 3 cities, last 5 days
print("\nLast 5 days of first 3 cities:")
print(aqi[:3, -5:])

# 3. Aggregation along axes
weekly_avg = np.round(aqi.mean(axis=1), 2)   # her sehir icin haftalik ortalama
daily_avg  = np.round(aqi.mean(axis=0), 2)   # her gun icin sehirler arasi ortalama
print("\nWeekly average per city:", weekly_avg)
print("Daily average across cities:", daily_avg)

# 4. Argmax / Argmin
worst_city   = cities[np.argmax(weekly_avg)]
cleanest_day = days[np.argmin(daily_avg)]
print("\nCity with highest weekly average AQI:", worst_city)
print("Cleanest day of the week:", cleanest_day)

# 5. Boolean filtering
unhealthy = aqi[aqi > 100]
moderate  = aqi[(aqi >= 50) & (aqi <= 80)]
print("\nUnhealthy readings (>100):", unhealthy)
print("Moderate readings (50-80):", moderate)

# 6. Searching with np.where()
rows, cols = np.where(aqi >= 100)
print("\nPositions where AQI >= 100:")
for r, c in zip(rows, cols):
    print(f"{cities[r]} - {days[c]} ({aqi[r, c]})")

# 7. Sorting
sorted_each = np.sort(aqi, axis=1)
order = np.argsort(weekly_avg)
sorted_cities = [cities[i] for i in order]
print("\nEach city's daily AQI sorted (ascending):")
print(sorted_each)
print("Cities from cleanest to most polluted:", sorted_cities)

# 8. Day-over-day change
change = np.diff(aqi, axis=1)
print("\nDay-over-day change shape:", change.shape)
print(change)

# 9. Copy vs View
view = aqi[:3]
copy = aqi[:3].copy()
view[0, 0] = 999
changed_by_view = aqi[0, 0] == 999
aqi[0, 0] = 55          # eski degeri geri yukle
copy[0, 0] = 0
changed_by_copy = aqi[0, 0] == 0
print("\nView modified -> original changed:", changed_by_view)
print("Copy modified -> original changed:", changed_by_copy)
print("view.base is aqi:", view.base is aqi, "  |  copy.base is None:", copy.base is None)

# 10. Joining and reshaping
konya = np.array([60, 65, 70, 72, 78, 75, 68])
new_aqi = np.vstack((aqi, konya))
reshaped = new_aqi.flatten().reshape(7, 6)
print("\nNew array with Konya, shape:", new_aqi.shape)
print("Flattened then reshaped to (7, 6):")
print(reshaped)
