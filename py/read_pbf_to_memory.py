# %%
import schema_pb2
import pandas as pd
#%% 
# declare a new PBF object
covid_schema = schema_pb2.Rows()
#%%
# Read the existing address book.
f = open('../data/pbfExport.pbf', "rb")
covid_schema.ParseFromString(f.read())
f.close()
# %%
def previewDates(covid_data):
    print(covid_data.dates[0:10])

def previewData(covid_data):
    print(list(covid_data.row[0].vals))
# %%
previewData(covid_schema)
# %%
previewDates(covid_schema)
# %%
def parseCovidDataToDf(covid_data):
    columns = ['id'] + list(covid_data.dates)
    dataRows = []
    for entry in covid_data.row:
        dataRows.append([entry.geoid] + list(entry.vals))
        
    return pd.DataFrame(dataRows, columns=columns)

# %%
parseCovidDataToDf(covid_schema).head()
# %%
