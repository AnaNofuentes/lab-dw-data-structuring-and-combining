def cleaning(df_insurance):

    df_insurance.columns= df_insurance.columns.str.replace(' ', '_').str.lower()

    df_insurance = df_insurance.rename(columns= {"st": "state"})

    df_insurance["gender"] = df_insurance["gender"].replace({"Male":"M", "Femal": "F","female":"F" })
    df_insurance["state"] = df_insurance["state"].replace({"AZ":"Arizona", "Cali":"California","WA":"Washinton"})
    df_insurance["education"] = df_insurance["education"].replace({"Bachelors":"Bachelor"})
    df_insurance["customer_lifetime_value"] = df_insurance["customer_lifetime_value"].str.rstrip("%")
    df_insurance["vehicle_class"] = df_insurance["vehicle_class"].replace({"Sports Car": "Luxury", "Luxury SUV":"Luxury","Luxury Car": "Luxury"})
    
    #  Customer lifetime value should be numeric
    df_insurance['customer_lifetime_value'] = df_insurance['customer_lifetime_value'].astype(float)

    df_insurance['number_of_open_complaints'].unique()

    #  Number of open complaints is a string - remember you can use `split()` to deal with it and take the number you need. 
    df_insurance['number_of_open_complaints'] = df_insurance['number_of_open_complaints'].str.split('/')
    df_insurance['number_of_open_complaints'] = df_insurance['number_of_open_complaints'].str[1]

    # Finally, since it should be numeric, cast the column to be in its proper type.
    df_insurance['number_of_open_complaints'] = df_insurance['number_of_open_complaints'].astype(float)

    # Drop the rows or columns with null values
    df_insurance = df_insurance.dropna(how='all')
    # Fill the null values with a specific value (such as the column mean or median for numerical variables,
    #  and mode for categorical variables)
    customer_lifetime_mean = df_insurance['customer_lifetime_value'].mean()
    df_insurance['customer_lifetime_value']= df_insurance['customer_lifetime_value'].fillna(customer_lifetime_mean)
    return(df_insurance)