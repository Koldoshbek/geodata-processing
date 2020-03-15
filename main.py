import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def second_task():
    print(df[['DEPT', 'K', 'MAG(XM,FM)', 'RMS']].describe())


def third_task():
    plt.hist(df.DEPT, color='r')
    plt.xlabel('Depth,km')
    plt.ylabel('N')
    plt.savefig('images/third_task.png')
    plt.show()


def fourth_task():
    plt.hist(df.K, color='g', bins=15)
    plt.xlabel('K')
    plt.ylabel('N')
    plt.savefig('images/fourth_task.png')
    plt.show()


def fifth_task():
    plt.rcParams['figure.figsize'] = (15, 3)
    plt.plot(df.ORIGIN, df.RMS, 'o-')
    plt.xlabel('Datetime')
    plt.ylabel('RMS')
    plt.rcParams['figure.figsize'] = (15, 3)
    plt.savefig('images/fifth_task.png')
    plt.show()


def sixth_task():
    plt.plot(df['LONG E'], df['LAT N'], 'go', markersize=15)
    plt.savefig('images/sixth_task.png')
    plt.show()


def seventh_task():
    df.plot.scatter('MAG(XM,FM)', 'K', color='r')
    # a•n + b∑x = ∑y
    # a∑x + b∑x2 = ∑y•x

    # where x is Magnitude and x is 'K'
    n = df['MAG(XM,FM)'].count()
    sum_of_x = df['MAG(XM,FM)'].sum()
    sum_of_y = df['K'].sum()
    multiplication_x = (df['MAG(XM,FM)'] * df['MAG(XM,FM)']).sum()
    multiplication_xy = (df['MAG(XM,FM)'] * df['K']).sum()

    # with Kramer's Method
    d = n * multiplication_x - sum_of_x * sum_of_x
    d1 = sum_of_y * multiplication_x - multiplication_xy * sum_of_x
    d2 = n * multiplication_xy - sum_of_x * sum_of_y

    a = d1 / d
    b = d2 / d

    plt.title(f'K={a:.{2}f} + {b:.{2}f}*mag')
    plt.xlabel('Magnitude')
    plt.plot(df['MAG(XM,FM)'], df['MAG(XM,FM)'] * b + a, linestyle='--', linewidth=5)
    plt.savefig('images/seventh_task.png')
    plt.show()


if __name__ == '__main__':
    file_with_data = "cat2010.xlsx"
    df = pd.read_excel(file_with_data)
    second_task()
    third_task()
    fourth_task()
    sixth_task()
    seventh_task()
    fifth_task()
