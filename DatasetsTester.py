import Datasets as data

db = data.Metadata()
print("\nExample dictionary:", db.getMetadata())

ds = data.Dataset()
db1 = ds.getFirst()
print("\nFirst dataset:", db1)
db2 = ds.getSecond()
print("\nSecond dataset:", db2)
db3 = ds.getThird()
print("\nThird dataset:", db3)
db4 = ds.getFourth()
print("\nFourth dataset:", db4)
db5 = ds.getFifth()
print("\nFifth dataset:", db5)