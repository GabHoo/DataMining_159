import pandas as pd

df = pd.read_csv ('ODI-2022.csv',sep=';')

print(df.head())

df.rename(columns = {'Tijdstempel':'TimeStamp', 'What programme are you in?':'Program','Have you taken a course on machine learning?':'ML_background','Have you taken a course on information retrieval':'IR_backround'}, inplace = True)
df.rename(columns = {'Have you taken a course on statistics?':'Stats_background','Have you taken a course on databases?':'DB_background'},inplace=True)
df.rename(columns = {'What is your gender?':'Gender','Chocolate makes you.....':'Chocolate_effect','When is your birthday (date)?':'Birth_date','Number of neighbors sitting around you?':'Neighbors','Did you stand up?':'stood_up'},inplace=True)
df.rename(columns = {'What is your stress level (0-100)?':'Stress_level','You can get 100 euros if you win a local DM competition, or we don’t hold any competitions and I give everyone some money (not the same amount!). How much do you think you would deserve then?':'Money_competition'},inplace=True)
df.rename(columns = {'Give a random number':'random_nr','Time you went to be Yesterday':'bed_time','What makes a good day for you (1)?':'good_day_1','What makes a good day for you (2)?':'good_day_2'},inplace=True)

print(df.head())

#Further pre processing needs to be done

#Usefull link: https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

print(df['random_nr'].describe())