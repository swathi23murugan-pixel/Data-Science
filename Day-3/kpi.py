import json
def export_kpi_summary(data,top,file):
    report={"status":"SUCCESS","top_category":top,"metrics":data}
    with open(file,"w") as f:
        json.dump(report,f,indent=2)
    with open(file,"r") as f:
        return json.load(f)
data=[{"category":"Electronics","total_revenue":2650.0,"avg_revenue":1325.0},{"category":"Furniture","total_revenue":300.0,"avg_revenue":300.0}]
print(export_kpi_summary(data,"Electronics","kpi_report.json"))