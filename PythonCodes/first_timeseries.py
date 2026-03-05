import pandas as pd
import matplotlib.pyplot as plt

df_all = pd.read_csv('PreliminaryAnalysis.csv')
min_date = pd.to_datetime('2026-02-22 17:00:00')

print(df_all.columns)

df_all['time'] = pd.to_datetime(df_all['time'])

df = df_all.loc[df_all['time'] > min_date]

x = 1
plt.figure(1)
plt.plot(df['time'], df['temp_salon_c'], label="Saloni")
plt.plot(df['time'], df['temp_kids_c'], label="paidiko")
plt.legend()

plt.figure(2)
plt.plot(df['time'], df['temp_out_1_b_c'], label="North")
plt.plot(df['time'], df['temp_out_2_n_c'], label="South")
plt.legend()

plt.show()
