from scipy.stats import spearmanr

df = pd.read_csv('3.2.1.csv')

# 1. Avg. Session Length для пользователя с максимальным Time on App
max_time_idx = df['Time on App'].idxmax()
avg_session = df.loc[max_time_idx, 'Avg. Session Length']

# 2. Корреляция Спирмена
corr, _ = spearmanr(df['Yearly Amount Spent'], df['Length of Membership'])

# 3. 40-й перцентиль Length of Membership
perc_40 = df['Length of Membership'].quantile(0.4)

# Округление
result = f"{avg_session:.2f};{corr:.2f};{perc_40:.2f}"
print(result)