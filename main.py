import streamlit as st
import pandas as pd
import numpy as np

# Загрузка набора данных
df = pd.read_csv('nics-firearm-background-checks.csv')

# Создание боковой панели для выбора параметров
st.sidebar.title('Параметры анализа')
year = st.sidebar.selectbox('Год', df['month'].unique())
state = st.sidebar.selectbox('Штат', df['state'].unique())

# Выполнение анализа
selected_df = df[(df['month'] == year) & (df['state'] == state)]
total_checks = selected_df['totals'].sum()
average_checks = selected_df['permit'].mean()
max_checks = selected_df['permit_recheck'].max()
min_checks = selected_df['admin'].min()

# Отображение результатов
st.title('Результаты анализа')
st.write(f'Общее количество проверок в {state} в {year} году: {total_checks:,}')
st.write(f'Число разрешений: {average_checks:,.2f}')
st.write(f'Число провереных разрешений: {max_checks:,}')
st.write(f'Администратор: {min_checks:,}')

# Сохранение результатов
st.sidebar.title('Сохранение результатов')
if st.sidebar.button('Экспортировать в CSV'):
    selected_df.to_csv('results.csv', index=True)





