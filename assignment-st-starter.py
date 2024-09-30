# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# show the title
st.title('Titanic App by Shirui Tang')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.write(df)
# create a figure with three subplots, size should be (15, 5)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
for i, pclass in enumerate([1, 2, 3]):
    sns.boxplot(x='Pclass', y='Fare', data=df[df['Pclass'] == pclass], ax=axes[i], width=0.2)
    axes[i].set_xlabel(f'PClass={pclass}')
    axes[i].set_ylabel('')
    axes[i].set_xticks([0])
    axes[i].set_xticklabels(['Fare'])
    axes[i].grid(True)
st.pyplot(fig)
