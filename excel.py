from database import select_feedbacks
import pandas as pd

text = list()
urls = list()

def create_table(filename):
    for i in select_feedbacks():
        print(i)
        text.append(''.join(filter(str.isdigit, i[0])))
        urls.append(i[1])
    df = pd.DataFrame({"text":text,"urls":urls})
    writer = pd.ExcelWriter(f'{filename}',engine='openpyxl')
    print(df)
    df.to_excel(writer,sheet_name=f'{filename}')
    writer.save()

















