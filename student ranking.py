

import pandas as pd
n = int(input("Enter number of students: "))

names = []
maths = []
physics = []
chemistry = []

for i in range(n):
    print(f"\nEnter details for Student {i+1}")
    name = input("Name: ")
    m = int(input("Maths marks (out of 100): "))
    p = int(input("Physics marks (out of 100): "))
    c = int(input("Chemistry marks (out of 100): "))

    names.append(name)
    maths.append(m)
    physics.append(p)
    chemistry.append(c)

df = pd.DataFrame({
    "Name": names,
    "Maths": maths,
    "Physics": physics,
    "Chemistry": chemistry
})

df["Total"] = df["Maths"] + df["Physics"] + df["Chemistry"]
df["Average"] = df["Total"] / 3
df["CGPA"] = df["Average"] / 10
df["Result"] = df.apply(
    lambda row: "Fail" if (row["Maths"] < 50 or row["Physics"] < 50 or row["Chemistry"] < 50)
    else "Pass",
    axis=1
)
df["Rank"] = df["Total"].rank(method="dense", ascending=False).astype(int)
df = df.sort_values("Rank")

df.to_csv("student_ranking.csv", index=False)

print("\n📊 FINAL STUDENT RANKING TABLE\n")
print(df.to_string(index=False))
