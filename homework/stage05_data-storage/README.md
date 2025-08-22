# Folder structure (data/raw/, data/processed/)
.csv is put in data/raw/
.parquet is put in data/processed/

#Formats used and why

small/exchange file use csv. —> easy to read, easy diffs in git
analysis-ready and bigger file use parquet —> compressed, fast reading speed

#How your code reads/writes using env variables
using os.getenv get path from env
