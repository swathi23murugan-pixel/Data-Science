def parse_numeric_log(records):
    valid=[]
    count=0
    for x in records:
        try:
            a,b=x.split(",")
            valid.append({"id":a.strip(),"value":float(b.strip())})
        except:
            count+=1
    return {"valid":valid,"corrupted_count":count}
records=["TXN101, 145.50","TXN102, invalid_num","TXN103, 300.00","CORRUPTED_LINE","TXN104, 82.25"]
print(parse_numeric_log(records))