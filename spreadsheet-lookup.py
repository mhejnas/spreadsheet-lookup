import numpy, pandas as pd
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def in_range(low, high, actual):
    if(low <= actual <= high):
        return True
    else:
        return False

code_range_sheet = pd.read_excel("/home/matt/projects/joining-spreadsheets/Code_Range_Sheet.xlsx")
print("Code Range Sheet Dimensions: " + str(code_range_sheet.shape))
code_sheet = pd.read_excel("/home/matt/projects/joining-spreadsheets/Code_Sheet.xlsx")
print("Code Sheet Dimensions: " + str(code_sheet.shape))

matched_df = pd.DataFrame(columns=["Code", "Modifier"])

for index_codes, code_row in code_sheet.iterrows():
    code = code_row["Code"]
    print(code)
    for index_code_range, code_range in code_range_sheet.iterrows():
        is_in_range = in_range(code_range["Code Range Low"], code_range["Code Range High"], code)
        print("is_in_range: " + str(is_in_range))
        if is_in_range:
            modifier = code_range["Modifier"]
            matched_df.loc[len(matched_df.index)] = [code, modifier]

matched_df.to_excel("/home/matt/projects/joining-spreadsheets/Code_Modifier_Sheet.xlsx")


