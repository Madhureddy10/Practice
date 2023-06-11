def get_date_info(year_month, quarter):
    year = int(year_month[:4])
    month = int(year_month[4:])
    quarter_num = int(quarter[1:])

    # Calculate previous month

    if month > 1:
        previous_month = (year * 100 + month - 1)
    else:
        previous_month = ((year - 1) * 100 + 12)
    previous_month = str(previous_month).zfill(6)
    print("Previous Month:", previous_month)

    # Calculate previous quarter

    if quarter_num > 1:
        previous_quarter = quarter_num - 1
        previous_quarter = f"Q{previous_quarter}_{year}"

    else:
        previous_quarter = 4
        year1 = year - 1
        previous_quarter = f"Q{previous_quarter}_{year1}"
    print("Previous Quarter:", previous_quarter)

    # Calculate the current quarter

    current_quarter = f"Q{quarter_num}_{year}"
    print("Current Quarter:", current_quarter)

    # Calculate future year and month

    future_year = year
    future_month = month + 11
    if future_month > 12:
        future_month = future_month - 12  # future_month -= 12
        future_year = future_year + 1  # future_year += 1
    future_year_month = str(future_year).zfill(4) + str(future_month).zfill(2)
    print("Future_year_Month:", future_year_month)


# Example usage

get_date_info("202301","Q1")