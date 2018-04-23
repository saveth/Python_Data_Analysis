import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

# Counts by source
click_source = ad_clicks.groupby('utm_source')\
  .size().reset_index()

# Actual clicks
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.notnull()

#print(ad_clicks.head())
clicks_by_source = ad_clicks.groupby([
  'utm_source', 'is_click'
]).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id').reset_index()

# Convert pivot table to flat datafile
clicks_pivot = pd.DataFrame(clicks_pivot.to_records())

# Add new column
clicks_pivot['percent_clicked'] = (
  clicks_pivot['True'] / (
    clicks_pivot['True'] + clicks_pivot['False'])
  ) *100

#print(clicks_pivot)

# Experimental group
experiment_group =   ad_clicks\
  .groupby('experimental_group')\
  .user_id.count().reset_index()

# Experimental group clicks
experiment_click_source = ad_clicks.groupby([
  'utm_source','experimental_group','is_click'
]).user_id.count().reset_index()\
  .pivot_table(
  index = ['utm_source','experimental_group'],
  columns = 'is_click',
  values = 'user_id').reset_index().to_records()
experiment_click_source = pd.DataFrame(experiment_click_source)

experiment_click_source['percent_clicked'] =  (
  experiment_click_source['True'] / (
    experiment_click_source['True'] + experiment_click_source['False'])
  ) *100
#print(experiment_click_source)

# Separating Testing Group
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

### Group clicks by Day
# Group A
a_clicks_day = a_clicks.groupby('day', as_index =False)\
  .user_id.count()
a_total = a_clicks_day['user_id'].sum()  
a_clicks_day['percent_clicked'] = (a_clicks_day['user_id'] /  a_total) * 100

# Group B
b_clicks_day = b_clicks.groupby('day', as_index =False)\
  .user_id.count()

b_total = b_clicks_day['user_id'].sum()  
b_clicks_day['percent_clicked'] = (b_clicks_day['user_id'] /  b_total) * 100
print(a_clicks_day)
print(b_clicks_day)
