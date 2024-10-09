import pandas as pd
import numpy as np

cube_ruler = [4.45, 4.40, 4.45, 4.40, 4.45, 4.45, 4.40, 4.45, 4.40, 4.45] # küp-cetvel cm
sphere_caliper = [23.02, 23.70, 23.80, 23.84, 23.90, 23.68, 23.80, 23.70, 23.80, 23.70] # küre-kompas mm

sphere_micrometer = [23.06, 23.05, 23.49, 23.48, 23.47, 23.01, 23.49, 23.49, 23.02, 23.06,
                   23.03, 23.00, 23.02, 23.07, 23.08, 23.11, 23.03, 23.02, 23.49, 23.47] # küre-mikrometre mm

# 1. Aritmetik ortalama (gerçek değer)

cube_mean = sum(cube_ruler) / len(cube_ruler)
sphere_caliper_mean = sum(sphere_caliper) / len(sphere_caliper)
sphere_micrometer_mean = sum(sphere_micrometer) / len(sphere_micrometer)

max_len = max(len(cube_ruler), len(sphere_caliper), len(sphere_micrometer))
mean_df = pd.DataFrame(data={"Cube Ruler Mean": cube_mean,
                             "Sphere Caliper Mean": sphere_caliper_mean,
                             "Sphere Micrometer Mean": sphere_micrometer_mean},
                       index=[1]) # print only once
print(mean_df)

# 2. Mutlak Hata

def get_absolute_error(arr, mean_val):
    absolute_arr = []
    for i in range(len(arr)):
        absolute_number = round(abs(arr[i] - mean_val), 2)
        absolute_arr.append(absolute_number)
    return absolute_arr

cube_absolute_error = get_absolute_error(cube_ruler, cube_mean)
sphere_caliper_absolute_error = get_absolute_error(sphere_caliper, sphere_caliper_mean)
sphere_micrometer_absolute_error = get_absolute_error(sphere_micrometer, sphere_micrometer_mean)

# 3. Bağıl Hata

def get_relative_error(arr, mean_val):
    relative_arr = []
    for i in range(len(arr)):
        relative_number = round(abs(arr[i] - mean_val) / arr[i], 2)
        relative_arr.append(relative_number)
    return relative_arr

cube_relative_error = get_relative_error(cube_ruler, cube_mean)
sphere_caliper_relative_error = get_relative_error(sphere_caliper, sphere_caliper_mean)
sphere_micrometer_relative_error = get_relative_error(sphere_micrometer, sphere_caliper_mean)

#############################

def pad_data(arr, max_len, arr_len):
    padded_arr = np.pad(arr, (0, max_len - arr_len), "constant", constant_values=np.nan)
    return padded_arr

# cube_absolute_error_padded = np.pad(cube_absolute_error, (0, max_len - len(cube_absolute_error)), 'constant', constant_values=np.nan)
# sphere_caliper_absolute_error_padded = np.pad(sphere_caliper_absolute_error, (0, max_len - len(sphere_caliper_absolute_error)), 'constant', constant_values=np.nan)
# sphere_micrometer_absolute_error_padded = np.pad(sphere_micrometer_absolute_error, (0, max_len - len(sphere_micrometer_absolute_error)), 'constant', constant_values=np.nan)

cube_absolute_error_padded = pad_data(cube_absolute_error, max_len, len(cube_absolute_error))
sphere_caliper_absolute_error_padded = pad_data(sphere_caliper_absolute_error, max_len, len(sphere_caliper_absolute_error))
sphere_micrometer_absolute_error_padded = pad_data(sphere_micrometer_absolute_error, max_len, len(sphere_micrometer_absolute_error))

# DataFrame
absolute_error_dataframe = pd.DataFrame(data={
    "Küp Mutlak Hata": cube_absolute_error_padded,
    "Küre Kumpas Mutlak Hata": sphere_caliper_absolute_error_padded,
    "Küre Mikrometre Mutlak Hata": sphere_micrometer_absolute_error_padded
})

# # Eksik verileri nan ile doldur
# cube_relative_error_padded = np.pad(cube_relative_error, (0, max_len - len(cube_relative_error)), 'constant', constant_values=np.nan)
# sphere_caliper_relative_error_padded = np.pad(sphere_caliper_relative_error, (0, max_len - len(sphere_caliper_relative_error)), 'constant', constant_values=np.nan)
# sphere_micrometer_relative_error_padded = np.pad(sphere_micrometer_relative_error, (0, max_len - len(sphere_micrometer_relative_error)), 'constant', constant_values=np.nan)

cube_relative_error_padded = pad_data(cube_relative_error, max_len, len(cube_relative_error))
sphere_caliper_relative_error_padded = pad_data(sphere_caliper_relative_error, max_len, len(sphere_caliper_relative_error))
sphere_micrometer_relative_error_padded = pad_data(sphere_micrometer_relative_error, max_len, len(sphere_micrometer_relative_error))

relative_error_dataframe = pd.DataFrame(data={
    "Küp Bağıl Hata": cube_relative_error_padded,
    "Küre Kumpas Bağıl Hata": sphere_caliper_relative_error_padded,
    "Küre Mikrometre Bağıl Hata": sphere_micrometer_relative_error_padded
})

print(absolute_error_dataframe)
print(relative_error_dataframe)

# 4. Standart Sapma

def standard_deviation(arr, mean_val, N):
    value = 0
    for i in range(len(arr)):
        value += ((arr[i] - mean_val) ** 2) / (N - 1)
    return np.sqrt(value)

cube_std = standard_deviation(cube_ruler, cube_mean, len(cube_ruler))
sphere_caliper_std = standard_deviation(sphere_caliper, sphere_caliper_mean, len(sphere_caliper))
sphere_micrometer_std = standard_deviation(sphere_micrometer, sphere_micrometer_mean, len(sphere_micrometer))

std_df = pd.DataFrame(data={"Küp Std": cube_std,
                             "Küre Kumpas Std": sphere_caliper_std,
                             "Küre Mikrometre Std": sphere_micrometer_std},
                       index=[1]) # print only once
print(std_df)

# print(np.std(cube_ruler))
# print(np.std(sphere_caliper))
# print(np.std(sphere_micrometer))

# 5. Kürenin Hacmi

def sphere_volume(arr):
    return [((4 / 3) * np.pi * (arr[i] / 2)) for i in range(len(arr))]

sphere_caliper_volume = sphere_volume(sphere_caliper)
sphere_micrometer_volume = sphere_volume(sphere_micrometer)

volume_max = max(len(sphere_caliper_volume), len(sphere_micrometer_volume))

sphere_caliper_volume_padded = pad_data(sphere_caliper_volume, volume_max, len(sphere_caliper_volume))
sphere_micrometer_volume_padded = pad_data(sphere_micrometer_volume, volume_max, len(sphere_micrometer_volume))

sphere_volume_df = pd.DataFrame(data={"Küre Kumpas Hacim": sphere_caliper_volume_padded,
                                      "Küre Mikrometre Hacim": sphere_micrometer_volume_padded})

print(sphere_volume_df)

# 6. Verileri excel dosyasına çevirme

mean_df.to_excel("./mean.xlsx", index=False)
absolute_error_dataframe.to_excel("./absolute_error.xlsx", index=False)
relative_error_dataframe.to_excel("./relative_error.xlsx", index=False)
std_df.to_excel("./standard_deviation.xlsx", index=False)
sphere_volume_df.to_excel("./sphere_volume.xlsx", index=False)