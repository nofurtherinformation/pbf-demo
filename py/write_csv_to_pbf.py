# %%
import pandas as pd
import schema_pb2
# %%
# import data
data = pd.read_csv('../data/covid_deaths_usafacts.csv').drop(columns=['County Name', 'State', 'StateFIPS'])

#%%
# clean data to expected types
data = data.replace('suppressed', -9999) \
    .apply(pd.to_numeric, errors="coerce") \
    .fillna(-999).astype(int)
print(data.head())
#%%
# Call new PBF Schema
pbfExport = schema_pb2.Rows()
pbfExport.dates.extend(list(data.columns)[1:])

# iterate over rows and pack into PBF format
for i in range(0, len(data)):
    # new row in the PBF
    rowObj = pbfExport.row.add()
    # set the GEOID field to be the FIPS code
    rowObj.geoid = data.iloc[i].countyFIPS
    # pack the values using extend for repeated values
    rowObj.vals.extend(data.iloc[i].values[1:])

# write the PBF to disk
f = open(f'./pbfExport.pbf', "wb")
f.write(pbfExport.SerializeToString())
f.close()


# %%
