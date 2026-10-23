# def age_cat(df):
#     if df.Age < 18:
#         df['agedim'] = 0
#     elif df.Age < 55 and df.Age > 18:
#         df['agedim'] = 1
#     else:
#         df['agedim'] = 2
# train_df = train_df.apply(age_cat,axis= 0 )
# train_df.groupby(['Age','Sex']).Survived.mean()