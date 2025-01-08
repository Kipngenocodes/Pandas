import pandas as pd
from io import StringIO


# create a html string
html_string = """
<html>
<head>
    <title>Employee Data</title>
</head>
<body>
    <h1>Employee Information</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Employee_ID</th>
                <th>Name</th>
                <th>Age</th>
                <th>Department</th>
                <th>Salary</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>EMP001</td>
                <td>John Doe</td>
                <td>28</td>
                <td>IT</td>
                <td>60000</td>
            </tr>
            <tr>
                <td>EMP002</td>
                <td>Jane Smith</td>
                <td>32</td>
                <td>HR</td>
                <td>55000</td>
            </tr>
            <tr>
                <td>EMP003</td>
                <td>Chris Johnson</td>
                <td>45</td>
                <td>Finance</td>
                <td>75000</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""

# Save to a temporary file and read
with open("temp.html", "w") as f:
    f.write(html_string)
# output the dataframe 
df = pd.read_html("temp.html")[0]
print(df)

print('\n')

# Reading the HTML string using pandas and stringio
dfs = pd.read_html(StringIO(html_string))
print(dfs[0])