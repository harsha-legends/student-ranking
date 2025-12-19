import pandas as pd

data = {
    "Name": ["Harsha", "Teja", "Jama", "Madhu", "Maddy"],
    "Maths": [89, 77, 90, 59, 66],
    "Physics": [99, 90, 88, 77, 66],
    "Chemistry": [90, 100, 77, 56, 88]
}
df = pd.DataFrame(data)

print("ORIGINAL DATA:")
print(df)
print("\n-----------------------------\n")


df["Total"] = df[["Maths", "Physics", "Chemistry"]].sum(axis=1)
df["Average"] = df[["Maths", "Physics", "Chemistry"]].mean(axis=1)
def result_status(row):
    if row["Maths"] < 50 or row["Physics"] < 50 or row["Chemistry"] < 50:
        return "Fail"
    else:
        return "Pass"

df["Result"] = df.apply(result_status, axis=1)
df["CGPA"] = (df["Average"] / 10).round(2)

df["Rank"] = df[df["Result"] == "Pass"]["Total"].rank(
    ascending=False, method="dense"
)
df = df.sort_values(by="Rank")

print("FINAL RESULT WITH TOTAL, CGPA, RESULT & RANK:")
print(df)

df.to_csv("student_results.csv", index=False)
print("\nResult saved as student_results.csv")

