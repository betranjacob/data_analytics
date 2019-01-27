# DataCleansing exercise using Portuguese wine data

This exercise is about munging the data into the correct shape to pass into a selection of models and to display charts providing insights into the data.The data can be used to make predictions about the quality of a wine based on its chemical make up.

## Prerequisites
  - Python 3 environment
  - Numpy
  - Matplotlib library is used to plot charts.

There is a data directory with red and white wine data.
We will be working with "winequality-red.json" which is a json document of red wine data.

The objective of the exercise is to take the json data and clean it up so we can run the same model on the red wine data.

* The work is done in exercise.py.
* More tests need to be written to verify each part works as expected for various cases
* pro tip: as per the Json specification don't assume the json values will always be in the same order when parsing, you should rely on the field name of each field to detirmine the layout.

# Part 1a

provide a function to sort the rows by date, if there are two identical dates then sort by id lexicographically ascending

Changes added to run_part_a()

# Part 1b

We'd like to run our classification on red wine but to do that we'll need to get the data into the correct shape and remove any corrupted or invalid data in the json.
Your function should return two objects

  1. Feature list :  Two dimentional numpy array of float64 which are the 'features' of each wine
        "fixed acidity"
        "volatile acidity"
        "citric acid"
        "residual sugar"
        "chlorides"
        free sulfur dioxide"
        "total sulfur dioxide"
        "density"
        "pH"
        "sulphates"
        "alcohol"

  2. Labelled Target : A numpy array of ints for the "quality" of each wine

# Notes
  * X and y should have the same number of rows where row 1 of X should be the features for row 1 of y.
  * the id and vintage fields can be dropped as they are not inputs to the model.
  * Any wines in the json data with invalid field values should be removed
  * order the columns of X lexicographically in ascending order, this is for verification

Only use valid rows in these calculations.

A row is valid if *all* its columns are valid, even if the column which is invalid doesn't pertain to the column we're doing the calculation for.

A column is valid depending on its type
  * Date - a string which parses to a datetime object in the format ''%d/%m/%y'
  * float - number or string which parses to a number, Nan is invalid

* Example :

"date";       "fixed acidity";"volatile acidity";"citric acid";"residual sugar";
"12/17/2016";  7;                "0.27";             Nan;          20.7     <- Invalid nan valid - this row isn't used to calculate fa, va, ca or rs
"";            6.3;              "0.3";              0.34;         1.6      <- Invalid not a parsable date - this row isn't used to calculate fa, va, ca or rs
"12/17/2016";  8.1;              "0.28";             0.4;          6.9;     <- valid
"12/17/2016";  7.2;              "0.23";             0.32;         8.5;     <- valid

Make your changes to run_part_b()

# Part 1c

Plot a chart showing a count by date (grouped by year) of red wines.

Any invalid rows should be counted in the chart under 'invalid'
Hint: this means your chart should have exactly 16 data points

Make your changes to run_part_c()
to display the chart make changes to the function run_chart_c()

# Part 1d

Write a function which returns the mean, median, standard deviation, min and max for each of the following columns (there are 11).

Use only valid rows in the calculations (see above)

"fixed acidity"
"volatile acidity"
"citric acid"
"residual sugar"
"chlorides"
free sulfur dioxide"
"total sulfur dioxide"
"density"
"pH"
"sulphates"
"alcohol"

Plot this data in a chart (or charts) of your choice which best conveys the information

make your changes in run_part_d()
to display the chart make changes to the function run_chart_d()

Your functions will be run using the simple demo.py script in the solution.
Please ensure this outputs all the data correctly and that the charts plot when this script is called.
The expectation is that no unmanaged exceptions to be thrown when executing this script



