import pandas as pd
fp = input("Enter your file part : ")
df = pd.read_csv (rf'{fp}')
df.to_json (r'output.json')