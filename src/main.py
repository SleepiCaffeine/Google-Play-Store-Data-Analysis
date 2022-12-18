import helper_functions as hf
import pandas as pd
import matplotlib.pyplot as plt
# ============================================ PART 1: READING AND REDUCING CSV FILE ========================================================= #
android = pd.read_csv('resources/Google-Playstore.csv', encoding='utf8')     # It takes approx. 15s to open file
android.info()

useless_android = ['Minimum Installs', 'App Id', 'Maximum Installs', 'Price', 'Currency', 'Size', 'Minimum Android', 'Developer Id', 'Developer Website', 'Developer Email', 'Released', 'Last Updated', 'Content Rating', 'Privacy Policy', 'In App Purchases', 'Editors Choice', 'Scraped Time']      # Collumns that contain info, that we will not use

android_clean = hf.drop_col_pd(android, useless_android)
android_clean.info()
android_clean.to_csv("resources/android_clean.csv")

# ================================================ PART 2: FILTERING OUT PAID APPS =========================================================== #
android_clean = pd.read_csv('resources/android_clean.csv', encoding='utf8', index_col=[0])
free_bool = android_clean['Free'] == True
android_free = android_clean[free_bool]
android_free.info()
android_free.to_csv('resources/android_free.csv')

# =============================================== PART 3: FILTERING OUT NON-ENGLISH ========================================================== #
android_free = pd.read_csv('resources/android_free.csv', encoding='utf8', index_col=[0])
android_english = android_free[hf.is_eng(android_free["App Name"])]
android_english.info()
android_english.to_csv('resources/android_english.csv')

# =============================================== PART 4: ADDING COMPARISON GRAPH ========================================================== #
android_english = pd.read_csv('resources/android_english.csv', encoding='utf8', index_col=[0])

csv_files = ['English Apps', 'Unfiltered']
app_count = [android_english.shape[0], android.shape[0]]

fig, ax = plt.subplots(figsize =(8, 5))
ax.barh(csv_files, app_count,
        color=['#DF4C2D','#BF4126'],
        edgecolor=['#9F3620', '#602113'],
        height=0.5)

ax.set_xlim([2000000, 2350000])
ax.set_xticks([2000000, 2175000, 2350000])
ax.set_xticklabels(['2,000,000', '2,175,000', '2,350,000'])
ax.axvline(x=2175000, ymin=0.045, c='grey', alpha=0.5)

ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')

ax.set_yticklabels([])
for i, y in zip(range(0, 2), csv_files):
    ax.text(x=1940000,
            y=i-0.03,
            s=y)
    
ax.text(x=1940000, y=2,
        s='App numbers compared to filter status',
        weight='bold', size=17)
ax.text(x=1940000, y=1.8,
        s='English apps have been filtered to be free to download',
        size=12,
        color='darkgrey')
ax.text(x=1940000, y=1.6,
        s='x-axis: App number   ||   y-axis: Filter Status',
        size=12,
        color='darkgrey')

for s in ['top','right','bottom']:
    ax.spines[s].set_visible(False)


for i in ax.patches:
    plt.text(i.get_width()+5000, i.get_y()+0.25,
            str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
    
fig.tight_layout()
plt.show()

# =============================================== PART 5: MAKING GENRE DICTIONARIES ========================================================== #
android_english = pd.read_csv('resources/android_english.csv', encoding='utf8', index_col=[0])
genre_dict = hf.f_table(android_english["Category"])

# =============================================== PART 6: GRAPHING GENRE DICTIONARIES ========================================================== #
plt.rcParams.update({'font.size': 9})
fig, ax = plt.subplots(figsize =(20, 40))
ax.barh(list(genre_dict.keys()),
        genre_dict.values(),
        color='darkred',
        height=0.8)

for s in ['top','right','bottom']:
    ax.spines[s].set_visible(False)

ax.set_xticks([0, 6, 12])
ax.set_xticklabels(['0%', '6%', '12%'])
ax.axvline(x=6, ymin=0.045, c='grey', alpha=0.5)
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')

for i in ax.patches:
    plt.text(i.get_width()+0.1, i.get_y()+0.17,
            str(round((i.get_width()), 2)),
             fontsize = 8, fontweight='bold',
             color ='darkred')
    
ax.set_yticklabels([]) #removing them
for i, genre in zip(range(0, 48), list(genre_dict.keys())):
    ax.text(x=-1.25,
            y=i-0.156,
            s=genre)
    
ax.text(x=-1.25, y=52,
        s='Percentage frequency of app genres in the Google Play store',
        weight='bold', size=17)
ax.text(x=-1.25, y=50,
        s='x-axis: Percentage   ||  y-axis: Genres',
        size=12,
        color='darkgrey')

plt.show()
