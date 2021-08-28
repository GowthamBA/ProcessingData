import pandas as pd

#loading Required files
input_file = pd.read_csv("input/main.csv")
filtered_Country_file = pd.read_csv("output/filteredCountry.csv")

#Clearing Unwanted data
def clearing_data(value):
    value = list(value)
    data = []
    for item in value:
        value = item[1]['PRICE'].str.replace(',', '').str.replace('$','').str.replace('?','')

        # Decimal Value Checking
        list_data = list(value)
        if len(list_data) == 1:
            continue
        else:
            min_first = float(list_data[0])
            min_second = float(list_data[1])
        if min_first / int(min_first) == 1.0:
            min_first = int(min_first)

        if min_second / int(min_second) == 1.0:
            min_second = int(min_second)

        data.append((item[0], min_first, min_second))

    return data


# Filter rows by Country_code
def filteredCountry(df,country_code):
    df1 =df[df['COUNTRY'].str.contains(country_code)]
    return df1

# Function for finding minimum
def lowestPrice(fd):
    group = fd.groupby(['SKU'])
    clear_data = clearing_data(group)
    final_data = pd.DataFrame(columns=['SKU', 'FIRST_MINIMUM_PRICE', 'SECOND_MINIMUM_PRICE'])
    for sku, f_min, s_min in clear_data:
        final_data = final_data.append({
            'SKU': sku,
            'FIRST_MINIMUM_PRICE': f_min,
            'SECOND_MINIMUM_PRICE': s_min
        }, ignore_index=True)
    return final_data

# Filter Country Code contains USA
filtered_pd = filteredCountry(input_file,"USA")
filtered_pd.to_csv("output/filteredCountry.csv", index=False)

# Filtering the first two min values
finding_lowesst =lowestPrice(filtered_Country_file)
finding_lowesst.to_csv("output/lowestPrice.csv", index=False)
