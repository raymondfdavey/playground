
### **********************************PANDAS FROM KAGGLE*************************************
# Pandas is the most poular python library for data analysis
# use shift and enter to display results
import pandas as pd
pd.set_option("display.max_rows", 5)


# There are two core objects in pandas: the DATAFRAME and the SERIES.

### DATAFRAME

# A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.

# For example, consider the following simple DataFrame:
# We are using the pd.DataFrame() constructor to generate these DataFrame objects. The syntax for declaring a new one is a dictionary whose keys are the column names (Bob and Sue in this example), and whose values are a list of entries. This is the standard way of constructing a new DataFrame, and the one you are most likely to encounter.

print(pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))

#    Yes   No
# 0   50  131
# 1   21    2

# DataFrame entries are not limited to integers. For instance, here's a DataFrame whose values are strings:

print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}))

#   Bob	            Sue
# 0	I liked it.	    Pretty good.
# 1	It was awful.	Bland.

### ROW LABELS

# The dictionary-list constructor assigns values to the COLUMN LABELS from the keys in the dictionary, but just uses an ascending count from 0 (0, 1, 2, 3, ...) for the ROW LABELS. Sometimes this is OK, but oftentimes we will want to assign these labels ourselves.

# The list of row labels used in a DataFrame is known as an INDEX. We can assign values to it by using an INDEX PARAMETER in our constructor:

print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index = ['Product A', 'Product B']))

#                      Bob           Sue
# Product A    I liked it.  Pretty good.
# Product B  It was awful.        Bland.

### SERIES'
### SERIES CAN HAVE AN INDEX REMEMBER!!!

# A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:

print(pd.Series([1, 2, 3, 4, 5]))

# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

print(pd.Series([1, 2, 3, 4, 5], index = ["A", "B", "C", "D", "E"]))

# A    1
# B    2
# V    3
# V    4
# Y    5
# dtype: int64

print(pd.Series([1, 2, 3, 4, 5], index = [num for num in range(10, 15)]))

# 10    1
# 11    2
# 12    3
# 13    4
# 14    5
# dtype: int64

# A Series is, in essence, a single column of a DataFrame. So you can assign column values to the Series the same way as before, using an index parameter. However, a Series does not have a column name, it only has one overall name:

print(pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A'))

# 2015 Sales    30
# 2016 Sales    35
# 2017 Sales    40
# Name: Product A, dtype: int64

# The Series and the DataFrame are intimately related. It's helpful to think of a DataFrame as actually being just a bunch of Series "glued together". We'll see more of this in the next section of this tutorial.

### READING IN DATA

# Being able to create a DataFrame or Series by hand is handy. But, most of the time, we won't actually be creating our own data by hand. Instead, we'll be working with data that already exists.

### CSV

#  CSV file is a table of values separated by commas. Hence the name: "Comma-Separated Values", or CSV.

# Product A,Product B,Product C,
# 30,21,9,
# 35,34,1,
# 41,11,11

# We'll use the pd.read_csv() function to read the data into a DataFrame.

wine_reviews = pd.read_csv("./dataForKaggleNotes/winemag-data_first150k.csv")

### INSPECTING

# We can use the SHAPE attribute to check how large the resulting DataFrame is:

print(wine_reviews.shape) # (129971, 14)

# So our new DataFrame has 129,971 records (ROWS) split across 14 different COLUMNS. That's almost 2 million entries!

# We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:

print(wine_reviews.head())

# Unnamed: 0 country                                        description  \
# 0           0      US  This tremendous 100% varietal wine hails from ...   
# 1           1   Spain  Ripe aromas of fig, blackberry and cassis are ...   
# 2           2      US  Mac Watson honors the memory of a wine once ma...   
# 3           3      US  This spent 20 months in 30% new French oak, an...   
# 4           4  France  This is the top wine from La Bégude, named aft......

# The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify. 

# For example, you can see in this dataset that the CSV file has a built-in index (The 0,1,2,3 column that matches the new index created by pandas), which pandas did not pick up on automatically. To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.

wine_reviews = pd.read_csv("./dataForKaggleNotes/winemag-data_first150k.csv", index_col=0)
wine_reviews.head()

### WRITING TO CSV

# use dataframeVariable.to_csv("path")

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals.to_csv("./dataForKaggleNotes/cows_and_goats.csv")

### INDEXING SELECTING AND ASSIGNING

reviews = pd.read_csv("./dataForKaggleNotes/winemag-data_first150k.csv", index_col=0) 
reviews.head()

# These are the two ways of selecting a specific Series out of a DataFrame. Neither of them is more or less syntactically valid than the other, but the indexing operator [] does have the advantage that it can handle column names with reserved characters in them (e.g. if we had a country providence column, reviews.country providence wouldn't work).

# eg reviews.country accesses the country property of 'reviews' which is the series (list) of data in the country column

type(reviews["country"]) # print(pd.Series([1, 2, 3, 4, 5]))
type(pd.Series([1, 2, 3, 4, 5])) # print(pd.Series([1, 2, 3, 4, 5]))

reviews.country
# 0             US
# 1          Spain
# 2             US
# 3             US
# 4         France
#            ...  
# 150925     Italy
# 150926    France
# 150927     Italy
# 150928    France
# 150929     Italy
# Name: country, Length: 150930, dtype: object

# you can also access it with the same notation as dictionary eg:
reviews[["country", "description"]]
# 0             US
# 1          Spain
# 2             US
# 3             US
# 4         France
#            ...  
# 150925     Italy
# 150926    France
# 150927     Italy
# 150928    France
# 150929     Italy
# Name: country, Length: 150930, dtype: object

# And items in a panda series are accessable similar to a dictionary. I.e. the term France on row index 4 is accessable in the following way

print(reviews["country"][4]) # Reviews DF, country column, index 4 ... = France

reviews[["country", "description"]]

#       country	    description
# 0	    Italy	    Aromas include tropical fruit, broom, brimston...
# 1	    Portugal	This is ripe and fruity, a wine that is smooth...
# 2	    US	        Tart and snappy, the flavors of lime flesh and...
# 3	    US	        Pineapple rind, lemon pith and orange blossom ...
# 4	    US	        Much like the regular bottling from 2012, this...
# ...	...	...
# 129966	Germany	Notes of honeysuckle and cantaloupe sweeten th...
# 129967	US	Citation is given as much as a decade of bottl...
# 129968	France	Well-drained gravel soil gives this wine its c...
# 129969	France	A dry style of Pinot Gris, this is crisp with ...
# 129970	France	Big, rich and off-dry, this is powered by inte...

type(reviews[["country", "description"]])


### INDEXING IN PANDAS

# The indexing operator and attribute selection are nice because they work just like they do in the rest of the Python ecosystem. As a novice, this makes them easy to pick up and use. However, pandas has its own accessor operators, LOC and ILOC. For more advanced operations, these are the ones you're supposed to be using.

# Both loc and iloc are row-first, column-second. 

### ILOC  - INDEX LOCATION

# Follows the indexing-based selection process - selecting data based on its numerical position in the data.add()

# EG to select the first row or data in a dataFrame

print(reviews.iloc[0]) # row 0, all columns
# country                                                       US
# description    This tremendous 100% varietal wine hails from ...
# designation                                    Martha's Vineyard
# points                                                        96
# price                                                      235.0
# province                                              California
# region_1                                             Napa Valley
# region_2                                                    Napa
# variety                                       Cabernet Sauvignon
# winery                                                     Heitz
# Name: 0, dtype: object

# To select a column you must ignore the row selector (i.e. select all) and specify the column

reviews.iloc[:, 0] # all rows, column 0

# same as reviews["country"]
# 0             US
# 1          Spain
# 2             US
# 3             US
# 4         France
#            ...  
# 150925     Italy
# 150926    France
# 150927     Italy
# 150928    France
# 150929     Italy
# Name: country, Length: 150930, dtype: object

reviews.iloc[0, 0] # US row 0 column 0
reviews.country.iloc[0] # us column specified by.country (which is column 0) and row 0



# On its own, the : operator, which also comes from native Python, means "everything". 
# When combined with other selectors, however, it can be used to indicate a range of values. For example, to select the country column from just the first, second, and third row, we would do:

print(reviews.iloc[:3, 0]) # rows 0 to 3 (not including 3) column 0
# 0       US
# 1    Spain
# 2       US
# Name: country, dtype: object

reviews.iloc[[0, 1, 2], 0]
# 0       US
# 1    Spain
# 2       US
# Name: country, dtype: object
reviews.country.iloc[[0,1,2]] # IS EQUIVALENT OF ABOVE
# 0       US
# 1    Spain
# 2       US
# Name: country, dtype: object


print(reviews.iloc[1:3, 0]) # rows 1 and 2, column 0
# 1    Spain
# 2       US
# Name: country, dtype: object

#Negative numbers work the same as in other contexts

print(reviews.iloc[-5:, 0]) # last five rows, column 0
# 150925     Italy
# 150926    France
# 150927     Italy
# 150928    France
# 150929     Italy
# Name: country, dtype: object

# examples
# Select the first value from the description column of `reviews`, assigning it to variable `first_description`.
first_description = reviews.description.iloc[0]
# Select the first row of data (the first record) from reviews, assigning it to the variable first_row.
first_row = reviews.iloc[0, :]
first_row = reviews.iloc[0] # is equivalent of above - can leave out columns if its all of them

# Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions
first_descriptions = reviews.description.iloc[0:10]
# Select the records with index labels 1, 2, 3, 5, and 8, all columns assigning the result to the variable sample_reviews.
sample_reviews = reviews.iloc[[1,2,3,5,8],:]
sample_reviews = reviews.iloc[[1,2,3,5,8]]# can also leave out the column bit if its all columns


### LOC - LABEL BASED SELECTION
# In this paradigm, it's the data index value, not its position, which matters.

reviews.loc[0, 'country'] # row index 0, country column, = "US"
reviews.country.loc[0] # same thing
# iloc is conceptually simpler than loc because it ignores the dataset's indices. When we use iloc we treat the dataset like a big matrix (a list of lists), one that we have to index into by position. loc, by contrast, uses the information in the indices to do its work. Since your dataset usually has meaningful indices, it's usually easier to do things using loc instead. For example, here's one operation that's much easier using loc:

reviews = pd.read_csv("./dataForKaggleNotes/winemag-data-130k-v2.csv", index_col=0)

print(reviews.loc[:3, ['taster_name', 'taster_twitter_handle', 'points']])
# rows 0 to 3 or columns taster_name, taster twitter handle, and points
#           taster_name taster_twitter_handle  points
# 0       Kerin O’Keefe          @kerinokeefe      87
# 1          Roger Voss            @vossroger      87
# 2        Paul Gregutt           @paulgwine       87
# 3  Alexander Peartree                   NaN      87

# EXAMPLES

# Create a `df` containing the `country`, `province`, `region_1`, and `region_2` columns of the records with the index labels `0`, `1`, `10`, and `100`. In other words, generate the following DataFrame:
reviews.loc[[0,1,10,100], ['country', "province", "region_1", "region_2"]]



### LOC INCLUDES UPPER VALUE IN SLICE, ILOC DOES NOT

# iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

# Why the change? Remember that loc can index any stdlib type: strings, for example. If we have a DataFrame with index values Apples, ..., Potatoes, ..., and we want to select "all the alphabetical fruit choices between Apples and Potatoes", then it's a lot more convenient to index df.loc['Apples':'Potatoes'] than it is to index something like df.loc['Apples', 'Potatoet'] (t coming after s in the alphabet).

# This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000. In this case df.iloc[0:1000] will return 1000 entries, while df.loc[0:1000] return 1001 of them! To get 1000 elements using loc, you will need to go one lower and ask for df.loc[0:999].

# Otherwise, the semantics of using loc are the same as those for iloc.

### EXAMPLES WRITTN IN BOTH LOC AND ILOC
### REMEMBER ITS NOT [0:100], it's just 0:100. 0:100 creates a list [0,1,2,3...100]

# Create a variable df containing the country and variety columns of the first 100 records.
# ALL OF THE FOLLOWING ARE EQUIVALENT 
df = reviews.loc[0:99, ["country", "variety"]] # where country and variety are columns 0 and 11 of 12 
df = reviews.loc[:99, ["country", "variety"]]
df = reviews.loc[range(100), ["country", "variety"]]
df = reviews.iloc[0:100, [0, -2]]
df = reviews.iloc[:100, [0, -2]]
df = reviews.iloc[range(100), [0, -2]]
df = reviews.iloc[0:100, [0, 11]]
df = reviews.iloc[0:100, [0, 11]]

# Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
italian_wines = reviews.loc[(reviews.country == "Italy"), :]
italian_wines = reviews[reviews.country == 'Italy']

# Create a DataFrame `top_oceania_wines` containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.


top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand']))& (reviews.points >= 95)]
top_oceania_wines = reviews.loc[(reviews.points >= 95) & ((reviews.country == "Australia") | (reviews.country == "New Zealand"))]




### MESSING WITH THE INDEX

# you can set the index to be any of the columns
reviews.set_index("country")

# country                                             
# Italy                                      Nicosia  
# Portugal                       Quinta dos Avidagos  
# US                                       Rainstorm  
# US                                      St. Julian  
# US                                    Sweet Cheeks  
# ...                                            ...  
# Germany   Dr. H. Thanisch (Erben Müller-Burggraef)  
# US                                        Citation  
# France                             Domaine Gresser  
# France                        Domaine Marcel Deiss  
# France                            Domaine Schoffit  

# This is useful if you can come up with an index for the dataset which is better than the current one.

### CONDITIONAL SELECTION OF DATA ******

# Using conditions to make more interesting selections

# For example, suppose that we're interested specifically in better-than-average wines produced in Italy.

# We can start by checking if each wine is Italian or not:

reviews.country == 'Italy' # prints a series where they evaluate all the entries in column 'country' against the condition

# 0         False
# 1         False
#           ...  
# 150928    False
# 150929     True
# Name: country, Length: 150930, dtype: bool

# This operation produced a Series of True/False booleans based on the country of each record. This result can then be used inside of loc to select the relevant data:

reviews.loc[reviews.country == 'Italy', ['country', 'designation', 'points']] # this one here selects all the rows where reviews.country == Italy evaluates to true. So it is selecting all the rows where the wine is from italy

#
#           country	    designation	            points
# 10	    Italy	    Ronco della Chiesa	    95
# 32	    Italy	    Vigna Piaggia	        90
# ...	...	...	...
# 150927	Italy	    Terre di Dora	        91
# 150929	Italy	    NaN	                    90
# 23478 rows × 3 columns

# his DataFrame has ~20,000 rows. The original had ~130,000. That means that around 15% of wines originate from Italy.

# We can use the ampersand (&) to bring the two questions together:

### AND &

reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90), ['country', 'designation', 'points']] # This is looking for all entries where the country = italt and the points are 90 or above

# 	        country	    designation	        points
# 10	    Italy	    Ronco della Chiesa	95
# 32	    Italy	    Vigna Piaggia	    90
#             ...	...	...	...
# 150927	Italy	    Terre di Dora	    91
# 150929	Italy	    NaN	                90
# 7945 rows × 3 columns

top_oceania_wines = reviews.loc[(reviews.points >= 95) & ((reviews.country == "Australia") | (reviews.country == "New Zealand"))]
# at least 95 point wines from australia or new zealand


### OR |

reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90), ['country', 'designation', 'points']]
# Looking for entries where the country is italy OR the reviews are 90 or above


#           country	    designation	                            points
# 0	        US	        Martha's Vineyard	                    96
# 1	        Spain	    Carodorum Selección Especial Reserva	96
# ...	...	...	...
# 150928	France	    Grand Brut Rosé	                        90
# 150929	Italy	    NaN	                                    90
# 63743 rows × 3 columns

### ISIN 

# The first is isin. isin is lets you select data whose value "is in" a list of values. For example, here's how we can use it to select wines only from Italy or France:

reviews.loc[reviews.country.isin(['Italy', 'France']), ['country', 'designation', 'points']]
# selects entries where the country is in the supplied list, but includes columns country designation and point(for brevity of return)

#               country	designation	        points
# 4	            France	La Brûlade	        95
# 10	        Italy	Ronco della Chiesa	95
# ...	...	...	...
# 150928	    France	Grand Brut Rosé	    90
# 150929	    Italy	NaN	                90
# 44576 rows × 3 columns

### ISNULL NOTNULL

# The second is isnull (and its companion notnull). These methods let you highlight values which are (or are not) empty (NaN). 

# For example, to filter out wines lacking a price tag in the dataset (WHERE PRICE IS NAN), here's what we would do:

reviews.loc[reviews.price.notnull(), ['country', 'points', 'price']]

# 	                country	points	price
# 0	                US	    96	    235.0
# 1	                Spain	96	    110.0
#                      ...	...	...	...
# 150928	        France	90	    52.0
# 150929	        Italy	90	    15.0
# 137235 rows × 3 columns

reviews.loc[reviews.price.isnull(), ['country', 'points', 'price']]
# 	        country	points	price
# 32	    Italy	90	    NaN
# 56	    France	90	    NaN
# ...	...	...	...
# 150673	US	    87	    NaN
# 150922	Italy	91	    NaN
# 13695 rows × 3 columns

### ASSIGNING DATA AKA ADDING TO THE DATAFRAME

reviews['critic'] = 'everyone' # adds the column critic and fills with 'everyone'
reviews.loc[:,['country', 'points', 'price', 'critic']]

# 	        country	points	price	critic
# 0	        US	    96	    235.0	everyone
# 1	        Spain	96	    110.0	everyone
#           ...	...	...	...	...
# 150928	France	90	    52.0	everyone
# 150929	Italy	90	    15.0	everyone
# 150930 rows × 4 columns

reviews['index_backwards'] = range((len(reviews)), 0, -1)
reviews.loc[:,['country', 'points', 'critic', 'index_backwards']]
help(range)

#           country	points	critic	    index_backwards
# 0	        US	    96	    everyone	150930
# 1	        Spain	96	    everyone	150929
# ...	...	...	...	...
# 150928	France	90	    everyone	2
# 150929	Italy	90	    everyone	1
# 150930 rows × 4 columns


print(reviews.loc[reviews.taster_name.isin(["Sean P. Sullivan"]), ['country', 'designation', 'points']])

### **************************SUMMARY FUNCTIONS/MAP/APPLY *********************************************************************************************************

import pandas as pd
pd.set_option("display.max_rows", 10)

reviews = pd.read_csv("./dataForKaggleNotes/winemag-data-130k-v2.csv", index_col=0)
reviews.describe()

#      	points	        price
# count	129971.000000	120975.000000
# mean	88.447138	    35.363389
# std	3.039730	    41.022218
# min	80.000000	    4.000000
# 25%	86.000000	    17.000000
# 50%	88.000000	    25.000000
# 75%	91.000000	    42.000000
# max	100.000000	    3300.000000

### SUMMARY FUNCTIONS

# Pandas provides many simple "summary functions" (not an official name) which restructure the data in some useful way.

reviews.points.describe() 
reviews["points"].describe() 

# returns count of non NaN cells and other values of the column specified, or if applied to whole DF all the numeric ones. NOTE THE DTYPE

# count    129971.000000
# mean         88.447138
# std           3.039730
# min          80.000000
# 25%          86.000000
# 50%          88.000000
# 75%          91.000000
# max         100.000000
# Name: points, dtype: float64

# This method generates a high-level summary of the attributes of the given column. It is type-aware, meaning that its output changes based on the data type of the input. The output above only makes sense for numerical data; for string data here's what we get:

reviews.taster_name.describe()
reviews["taster_name"].describe()


# count         103727
# unique            19
# top       Roger Voss
# freq           25514
# Name: taster_name, dtype: object

# NOTE THE DTYPE - this column is actually comprised of strings of tasters names

### OTHER HELPFUL SUMMARY FUNCTIONS
pd.set_option("display.max_rows", 5)
list(reviews) # list of column names

# If you want to get some particular simple summary statistic about a column in a DataFrame or a Series, there is usually a helpful pandas function that makes it happen.


reviews.points.mean() # 88.44713820775404 # MEAN OF A NUMERICAL COLUMN
reviews["points"].mean() # 88.44713820775404
reviews["points"].median()


reviews.taster_name.unique() # NP ARRAY OF OF UNIQUE VALUES IN A COLUMN
reviews["taster_name"].unique()
# array(['Kerin O’Keefe', 'Roger Voss', 'Paul Gregutt',
#        'Alexander Peartree', 'Michael Schachner', 'Anna Lee C. Iijima',
#        'Virginie Boone', 'Matt Kettmann', nan, 'Sean P. Sullivan',
#        'Jim Gordon', 'Joe Czerwinski', 'Anne Krebiehl\xa0MW',
#        'Lauren Buzzeo', 'Mike DeSimone', 'Jeff Jenssen',
#        'Susan Kostrzewa', 'Carrie Dykes', 'Fiona Adams',
#        'Christina Pickard'], dtype=object)


len(reviews["country"].unique()) # 44  # number of unique values


# To see a list of unique values and how often they occur in the dataset, we can use the value_counts() method:

reviews.taster_name.value_counts() # LIST OF UNIQUE VALUES AND HOW OFTEN THEY OCCUR
reviews["taster_name"].value_counts()

# Roger Voss            25514
# Michael Schachner     15134
#                       ...  
# Fiona Adams              27
# Christina Pickard         6
# Name: taster_name, Length: 19, dtype: int64

reviews["country"].value_counts() # LIST OF UNIQUE VALUES AND HOW OFTEN THEY OCCUR

# US                        54504
# France                    22093
#
# China                         1
# Egypt                         1
# Name: country, Length: 43, dtype: int64



### MAPS - MAPPING ACROSS EACH VALUE AND PERFORMING A FUNCTION

# two mapping methods MAP() and apply()

### map() - simpler

# Remean the scores the wines received to 0 (change all the values to the mean is 0)

reviews["points"]
# 0         87
# 1         87
#           ..
# 129969    90
# 129970    90
# Name: points, Length: 129971, dtype: int64

review_points_mean = reviews.points.mean() # set variable review_points_mean to current mean of the points column

reviews["points"].map(lambda current_value: current_value - review_points_mean)
# 0        -1.447138
# 1        -1.447138
#             ...   
# 129969    1.552862
# 129970    1.552862
# Name: points, Length: 129971, dtype: float64

# ADD THIS NEW COLUMN to the df

reviews["mean_adjusted_points"] = reviews["points"].map(lambda current_value: current_value - review_points_mean)
pd.set_option("display.max_rows", 15)
reviews.loc[70:90, ["points", "mean_adjusted_points"]]

# mean points is 88.44713820775404 

#       points	mean_adjusted_points
# 70	86	    -2.447138
# 71	86	    -2.447138
# 72	86	    -2.447138
# 73	86  	-2.447138
# 74	86  	-2.447138
# ...	...	...
# 86	86      -2.447138
# 87	86	    -2.447138
# 88	86	    -2.447138
# 89	88  	-0.447138
# 90	88  	-0.447138

### apply()

### ACTALLY AS IN THE EXAMPLE AT THE BOTTOM, UNLESS YOU RETURN THE ROW YOU ACTUALLY CAN JUST RETURN VALUES THAT BECOME A NEW SERIES
# is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row. 

# returns a complete dataframe with the transformation in situ. original unmutated rather than just creating new series

reviews = pd.read_csv("./dataForKaggleNotes/winemag-data-130k-v2.csv", index_col=0)

# DEFINE CUSTOM METHOD (TAKES A SINGLE ROW AS AN ARGUMENT - if column specified, or a whole column if "axis" specified (or 0 and 1, where 0 is default and is column))
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

# apply() takes the custom function and axis parameters (either "columns" or "index" ) to transform each row or column by that function

reviews.apply(remean_points, axis='columns') # transforms the data into a new data frame with the function applied row by row )

# Returns a new DF so you must save it into new variable or wont see change: 

reviews.loc[:5,["country", "points"]]
# 	country	    points
# 0	Italy	    87
# 1	Portugal	87
# 2	US	        87
# 3	US	        87
# 4	US	        87
# 5	Spain	    87

newReviews = reviews.apply(remean_points, axis='columns')
newReviews.loc[:5,["country", "points"]]
# 	country	    points
# 0	Italy	    -1.447138
# 1	Portugal	-1.447138
# 2	US	        -1.447138
# 3	US      	-1.447138
# 4	US      	-1.447138
# 5	Spain	    -1.447138

# Note that map() and apply() return new, transformed Series and DataFrames, respectively. They don't modify the original data they're called on. If we look at the first row of reviews, we can see that it still has its original points value

# basically, you specify a function that either trasnforms each row, or each column, and then use that function and the axis specification in to the df.apply(func, axis) method and it returns a transformed df where the transformation carried out it done by the function specified

### BUILT IN MAPPINGS

# Pandas provides many common mapping operations as built-ins. For example, here's a faster way of remeaning our points column:

#eg
pd.set_option("display.max_rows", 5)

review_points_mean = reviews.points.mean()
reviews.points - review_points_mean # performs operation on all cells in reviews.points to 
# return a Series list of the values

centered_price = reviews["price"] - reviews["price"].mean()


# 0        -1.447138
# 1        -1.447138
#             ...   
# 129969    1.552862
# 129970    1.552862
# Name: points, Length: 129971, dtype: float64

# In this code we are performing an operation between a lot of values on the left-hand side (everything in the Series) and a single value on the right-hand side (the mean value). Pandas looks at this expression and figures out that we must mean to subtract that mean value from every value in the dataset.

# it can also figure out what to do if you perform an operation between two long series' (i.e. two colums - summing or concatenating etc)

reviews["country"] + " - " + reviews["region_1"] # combines the two strings with - in the middle eg Italy - Milan

# 0             Italy - Etna
# 1                      NaN
#                ...       
# 129969        France - Alsace
# 129970        France - Alsace
# Length: 129971, dtype: object

# These operators are faster than map() or apply() because they uses speed ups built into pandas. All of the standard Python operators (>, <, ==, and so on) work in this manner.

# However, they are not as flexible as map() or apply(), which can do more advanced things, like applying conditional logic, which cannot be done with addition and subtraction alone.

### tricky eg

# Which wine is the "best bargain"? Create a variable `bargain_wine` with the title of the wine with the highest points-to-price ratio in the dataset.

# mine
reviews["ratio"] = reviews["points"] / reviews["price"]
print(reviews.ratio)
print(list(reviews))
index = reviews.ratio.idxmax(axis=0)
print(type(index))
bargain_wine = reviews["title"][index]
print(bargain_wine)

# theirs

bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']


# Is a wine more likely to be "tropical" or "fruity"? Create a Series `descriptor_counts` counting how many times each of these two words appears in the `description` column in the dataset. (For simplicity, let's ignore the capitalized versions of these words.)

tropical = reviews["description"].map(lambda current_description: 1 if "tropical" in current_description else 0).sum()
fruity = reviews["description"].map(lambda current_description: 1 if "fruity" in current_description else 0).sum()
print(tropical, fruity)
descriptor_counts = pd.Series([tropical, fruity], index=['tropical','fruity'])

# We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.

# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.

# Create a series star_ratings with the number of stars corresponding to each review in the dataset.

def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')

# I think what is going on here is that if you return  row in the function it returns a data frame if you return a value it returns a series - THIS IS CORRECT


reviews = pd.read_csv("./dataForKaggleNotes/winemag-data-130k-v2.csv", index_col=0)

def stars(row):
    return row
    # if row.country == 'Canada':
    #     return 3
    # elif row.points >= 95:
    #     return 3
    # elif row.points >= 85:
    #     return 2
    # else:
    #     return 1

star_ratings = reviews.apply(stars, axis='columns')

# https://www.activestate.com/resources/quick-reads/how-to-apply-functions-in-pandas/

  ### *******************************GROUP BY SORT BY ETC MULTI INDEX*****************************************************************************************************************************************************************************************************************************************

### GROUP BY SORT BY ETC

import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("./dataForKaggleNotes/winemag-data-130k-v2.csv", index_col=0)
reviews.head()

### group by plus count
# groupby almost creates a new index which is the group and then does some operation
list(reviews)
reviews.groupby("country").country.count()
reviews_written = reviews.groupby('country').size()
reviews.groupby("points").points.count()


reviews.groupby("taster_twitter_handle").taster_twitter_handle.count()
reviews_written = reviews.groupby('taster_twitter_handle').size()



reviews.points.value_counts()

# groupby() creates a group of reviews with the same point values given. Then, for each of these groups, we counted how many valid points() entries were within that group. value_counts() is just a shortcut to this groupby() operation.

# We can use any of the summary functions we've used before with this data. For example, to get the cheapest wine in each point value category, we can do the following:

list(reviews.groupby('points').price)

### These create 21 different groups of review, where each group is complrised of reviews that all have the same points rating (so some have loads of reviews, some have hardly any)
### then the next operation specifies that for each of those 21 groups of reviews that all have the same points, look at the price column, and return the max for that whole group, which is one value. And as there is only one value for the whole group for points, there is a one to one relationship that can be returned for each of the 21 groups to for a 21 x 2 DF which is actually a Series where the index is the points value of the group

reviews.groupby('points').price.max()
reviews.groupby('points').price.min()
reviews.groupby("price").points.max()
# these gives max points per price and max and min prices per points


### Group by plus apply

# You can think of each group we generate as being a slice of our DataFrame containing only data with values that match. This DataFrame is accessible to us directly using the apply() method, and we can then manipulate the data in any way we see fit. For example, here's one way of selecting the name of the first wine reviewed from each winery in the dataset:

reviews.groupby('winery').size() # tells us how many reviews each winery has

# winery
# 1+1=3        6
# 10 Knots     4
#             ..
# àMaurice    40
# Štoka        3
# Length: 16757, dtype: int64

reviews.groupby('winery') # creates 16757 groups of reviews where, within each group all the reviews are for wines from that winery

reviews.groupby('winery').apply(lambda df: df.title.iloc[0]) # here we are applying the lambda function to each of the groups that is created by the winery (each group is its own df). In this case we are accessing first review (row) in each of the winery groups and selecting its tite. And so what should be produces is a series of 16757 entries where the winery is the index and the name or 'title' of the first wine on each winerys list of reviews is the entry

# winery
# 1+1=3                          1+1=3 NV Rosé Sparkling (Cava)
# 10 Knots                 10 Knots 2010 Viognier (Paso Robles)
#                                   ...                        
# àMaurice    àMaurice 2013 Fred Estate Syrah (Walla Walla V...
# Štoka                         Štoka 2009 Izbrani Teran (Kras)
# Length: 16757, dtype: object

### group by more than one column

reviews.groupby(['country', 'province']).size()

# country    province        
# Argentina  Mendoza Province    3264
#            Other                536
# Armenia    Armenia                2
# Australia  Australia Other      245
#            New South Wales       85
#                                ... 
# Uruguay    Juanico               12
#            Montevideo            11
#            Progreso              11
#            San Jose               3
#            Uruguay               24
# Length: 425, dtype: int64

reviews.groupby('country').size() # length 43
reviews.groupby('province').size() # length 425

# This is an interesting one where the groupby creates 425 different groups where all the reviews in each group have the same COUNTRY AND PROVENCE 

reviews.groupby(['country', 'points']).size() # length 463
reviews.groupby('country').size() # length 43
reviews.groupby('points').size() # length 21


# country    points
# Argentina  80         76
#            81         94
#            82        149
#            83        285
#            84        409
#                     ... 
# Uruguay    88         20
#            89          9
#            90          9
#            91          6
#            92          2
# Length: 463, dtype: int64

# This one is interesting because there are only 21 different points, and 43 different countries in the data set. But this groupby creates 463 different groups, where each group is a set of reviews where the country and the points given are the same. So for example in this you could find all the reviews with a points value of x from australia. So you could analyse all the 95 point wines from America, or all the 86 wines from Brazil.



# this one gets the best wine in each province of each country
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

### when thinking about group by in multiple groups. immagine the abbey where im living now and each person is a row in the dataset of the place. if you were to groupby age and gender you would get lots of groups where for each age there were two groups. but the key thing is that those groups have multiple entries and in order for them to just appear as 2 entries for each age group on a spread sheet, you need to do some sort of aggregation to compile or collate the data. or at least you should to make it useful.

### so with this place age and sex. my age 37 male might be 12 entries, then 14 for 37 female, but on a spread sheet where 37 M and 37 F are indexes for single rows, you need to somehow compress the 16 entries and specify that compression in order not to have the same index (M 37) for multiple entries. so either create new agg rows or sum rows or something else, otherwise you just get the same number of entries as before like
# 37 M 
# 37 M 
# 37 M 

### GROUP BY agg()

# Another groupby() method worth mentioning is agg(), which lets you run a bunch of different functions on your DataFrame simultaneously. For example, we can generate a simple statistical summary of the dataset as follows:


reviews.groupby(['country']).price.agg([len, min, max]) # groups by country then combines the reviews in the groups by looking at the price column and making a count value (len) min and max


#           len	    min	    max
# country			
# Argentina	3800	4.0	    230.0
# Armenia	2	    14.0	15.0
# ...	...	...	...
# Ukraine	14	    6.0	    13.0
# Uruguay	109	    10.0	130.0
# 43 rows × 3 columns
reviews.groupby(['country']).points.agg([len, min, max])
# groups by country then combines the reviews in the groups by looking at the points column and making a count value (len) min and max

#           len	    min	max
# country			
# Argentina	3800	80	97
# Armenia	2	    87	88
# ...	...	...	...
# Ukraine	14	    82	88
# Uruguay	109	    80	

list(reviews)
reviews.groupby(['country']).province.agg([len, min, max])
# 	          len	min	                max
# country			
# Argentina   3800	Mendoza Province	Other
# Armenia	  2	    Armenia	            Armenia
# Australia	  2329	Australia Other	    Westzern Australia
# Austria	  3345	Austria	            Österreichischer Sekt
# Bosnia	  2	    Mostar	            Mostar
# ...	...	...	...
# Switzerland 7	    Neuchâtel	        Valais
# Turkey  	  90	Aegean	            Urla-Thrace
# US	      54504	America	            Washington-Oregon
# Ukraine	  14	Ukraine	            Ukraine
# Uruguay	  109	Atlantida	        Uruguay

# What are the minimum and maximum prices for each variety of wine? Create a DataFrame whose index is the variety category from the dataset and whose values are the min and max values thereof.

# answer:
price_extremes = reviews.groupby('variety').price.agg([min, max])

### MULTI INDEX

# In all of the examples we've seen thus far we've been working with DataFrame or Series objects with a single-label index. groupby() is slightly different in the fact that, depending on the operation we run, it will sometimes result in what is called a multi-index.

# A multi-index differs from a regular index in that it has multiple levels. For example:

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed
#                               len
# country	province	
# Argentina	Mendoza Province	3264
# Other	                        536
# Armenia	Armenia	            2
# Australia	Australia Other	    245
# New South Wales	            85
# 425 rows × 1 columns

countries_reviewed.index
# MultiIndex([('Argentina',  'Mendoza Province'),
#             ('Argentina',             'Other'),
#             (  'Armenia',           'Armenia'),
# ...
#             (  'Uruguay',           'Uruguay')],
#   names=['country', 'province'], length=425)
type(countries_reviewed.index) # pandas.core.indexes.multi.MultiIndex

### Here, as with other groupby 2 columns, there is essentially 2 indexes - a multi-index

# Multi-indices have several methods for dealing with their tiered structure which are absent for single-level indices. They also require two levels of labels to retrieve a value. Dealing with multi-index output is a common "gotcha" for users new to pandas.

# The use cases for a multi-index are detailed alongside instructions on using them in the MultiIndex / Advanced Selection section of the pandas documentation.

# However, in general the multi-index method you will use most often is the one for converting back to a regular index, the reset_index() method:

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed
# 425 rows × 1 columns
type(countries_reviewed.index) # pandas.core.indexes.multi.MultiIndex

countries_reviewed.reset_index() # 425 rows × 3 columns
#   country	    province	        len
# 0	Argentina	Mendoza Province	3264
# 1	Argentina	Other	            536
# 2	Armenia	    Armenia	            2
# 3	Australia	Australia Other	    245
# 4	Australia	New South Wales	    85

# this seems to separate out the indices so instead of the province being a subindex of the index country, each country and province combo is given it's own index 

### SORT BY

countries_reviewed = countries_reviewed.reset_index()
countries_reviewed
countries_reviewed.sort_values(by='len')
# re-orders the df to be in ascending order by len (which in this case is number of entries in each province)

# 	    country	province	            len
# 179	Greece	Muscat of Kefallonian	1
# 192	Greece	Sterea Ellada	        1
# ...	...	...	...
# 415	US	    Washington	            8639
# 392	US	    California	            36247

# sort_values() defaults to an ascending sort, where the lowest values go first. However, most of the time we want a descending sort, where the higher numbers go first. That goes thusly:

countries_reviewed.sort_values(by='len', ascending=False)
# 	    country	province	len
# 392	US	    California	36247
# 415	US	    Washington	8639
# ...	...	...	...
# 63	Chile	Coelemu	    1
# 149	Greece	Beotia	    1   


# sort by more than one column at a time

countries_reviewed.sort_values(by=['country', 'len'])
# 	    country	    province	        len
# 1	    Argentina	Other	            536
# 0	    Argentina	Mendoza Province	3264
# ...	...	...	...
# 424	Uruguay	    Uruguay	            24
# 419	Uruguay	    Canelones	        43

#to revert to index
countries_reviewed.sort_index()

#       country	    province	        len
# 0	    Argentina	Mendoza Province	3264
# 1	    Argentina	Other	            536
# ...	...	...	...
# 423	Uruguay	    San Jose	        3
# 424	Uruguay	    Uruguay	            24

# What are the most expensive wine varieties? Create a variable sorted_varieties containing a copy of the dataframe from the previous question where varieties are sorted in descending order based on minimum price, then on maximum price (to break ties).

sorted_varieties = price_extremes.sort_values(by=["min", "max"], ascending = False)

# Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer. Hint: you will need the taster_name and points columns.

reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean().sort_values(ascending = False)
reviewer_mean_ratings.describe()

# What combination of countries and varieties are most common? Create a Series whose index is a MultiIndexof {country, variety} pairs. For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}. Sort the values in the Series in descending order based on wine count.

country_variety_counts = reviews.groupby(["country", "variety"]).title.count().sort_values(ascending= False)
print(country_variety_counts)

### ****************************************************************************************DATA TYPES MISSING VALUES**********************************************************************************************************************************************************
import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("./dataForKaggleNotes/winemag-data-130k-v2.csv", index_col=0)
reviews

### .dtype property and .astype

reviews.price.dtype # dtype('float64') # dtype of price column
reviews.dtypes # dtypes for all columns in df
# country                   object
# description               object
# designation               object
# points                     int64
# price                    float64
#                           ...   
# taster_name               object
# taster_twitter_handle     object
# title                     object
# variety                   object
# winery                    object
# Length: 13, dtype: objec

# float64 means that it's using a 64-bit floating point number; int64 means a similarly sized integer instead, and so on.

# NOTE columns of all strings do not get their own type; they are instead given the 'object' type.

# It's possible to convert a column of one type into another wherever such a conversion makes sense by using the astype() function. For example, we may transform the points column from its existing int64 data type into a float64 data type:

reviews.points.dtype # dtype('int64')
reviews.points.astype('float64') # outputs the points series but where it's float not int
# 0         87.0
# 1         87.0
#           ... 
# 129969    90.0
# 129970    90.0
# Name: points, Length: 129971, dtype: float64
point_strings = reviews.points.astype('str')

# The INDEX of the df or series has it's own dtype too

reviews.index.dtype # dtype('int64')

### MISSING DATA

# Entries missing values are given the value NaN, short for "Not a Number". 
# For technical reasons these NaN values are always of the float64 dtype.

# Pandas provides some methods specific to missing data. 
# To select NaN entries you can use pd.isnull() (or its companion pd.notnull()). 

reviews[pd.isnull(reviews.country)] # selects all entries where country == NaN

len(reviews[pd.isnull(reviews.country)]) # 63
len(reviews[pd.isnull(reviews.price)]) # 8996

### REPLACING MISSING VALUES

# can use fillna()
# help(reviews.fillna)

# fillna() provides a few different strategies for mitigating such data. For example, we can simply replace each NaN with an "Unknown":

reviews.region_2
reviews.region_2.fillna("Unknown")
reviews.region_2 = reviews.region_2.fillna("Unknown") # replaced region_2 with the uknown values
reviews.region_2

# Or we could fill each missing value with the first non-null value that appears sometime after the given record in the database. This is known as the backfill strategy.

### replacing non-null values

reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

# The replace() method is worth mentioning here because it's handy for replacing missing data which is given some kind of sentinel value in the dataset: things like "Unknown", "Undisclosed", "Invalid", and so on.

#  This means your df may have non-null values that you want to make explicitly null for ease of stuff later

# these two next operation replace all NAs with unknown in region 1 then counts how many of each value in region 1
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

# same as

reviews["region_1"] = reviews.region_1.fillna("Unknown")
reviews_per_region = reviews.groupby("region_1").region_1.count().sort_values(ascending = False)

### **************************RENAMING AND COMBINING COLUMNS INDEX ETC ****************************************************************************************************************************************************************************************************************

### RENAMING

import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("./dataForKaggleNotes/winemag-data-130k-v2.csv", index_col=0)


# THE Below code used rename() to rename the points column to score
reviews.rename(columns={'points': 'score'})

# rename() lets you rename index or column values by specifying a index or column keyword parameter, respectively. It supports a variety of input formats, but usually a Python dictionary is the most convenient. Here is an example using it to rename some elements of the index.

reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'}).loc[:, ["country", "designation"]]


#               country	    designation
# firstEntry	Italy	    Vulkà Bianco
# secondEntry	Portugal	Avidagos
# ...	...	...
# 129969	    France	    NaN
# 129970	    France	    Lieu-dit Harth Cuvée 
# 129971 rows × 2 columns

# so the column heading are 'columns={k:v}' and the rows is 'index={k:v} where they key is the current value and the value is the updated one you want

# You'll probably rename columns very often, but rename index values very rarely. For that, set_index() is usually more convenient.

### Rename axis - its like axis label

reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns').loc[:, ["country", "designation"]]

#    fields	country	    designation
#   wines		
#   0	    Italy	    Vulkà Bianco
#   1	    Portugal	Avidagos
#   ...	...	...
#   129969	France	    NaN
#   129970	France	    Lieu-dit Harth Cuvée Caroline
#   
# 129971 rows × 2 columns

### COMBINING

# When performing operations on a dataset, we will sometimes need to combine different DataFrames and/or Series in non-trivial ways. 
# Pandas has three core methods for doing this. In order of increasing complexity, these are 
# concat() 
# join() 
# merge() 

# Most of what merge() can do can also be done more simply with join(), so we will omit it and focus on the first two functions here.

### CONCAT 
# The simplest combining method is concat(). Given a list of elements, this function will smush those elements together along an axis.

# This is useful when we have data in different DataFrame or Series objects that have the same fields (columns). 

# For example: the YouTube Videos dataset, which splits the data up based on country of origin (e.g. Canada and the UK, in this example). If we want to study multiple countries simultaneously, we can use concat() to combine (without altering) the data. The entries from each have the same column names so they are just added together in one DF

canadian_youtube = pd.read_csv("./dataForKaggleNotes/CAvideos.csv")
british_youtube = pd.read_csv("./dataForKaggleNotes/GBvideos.csv")

canadian_youtube.shape # ((40881, 16))
list(canadian_youtube)
# ['video_id', 'trending_date', 'title', 'channel_title', 'category_id','publish_time','tags','views','likes','dislikes','comment_count','thumbnail_link','comments_disabled','ratings_disabled','video_error_or_removed', 'description'] 

british_youtube.shape # (38916, 16)
list(british_youtube) 
# ['video_id', 'trending_date', 'title', 'channel_title', 'category_id','publish_time','tags','views','likes','dislikes','comment_count','thumbnail_link','comments_disabled','ratings_disabled','video_error_or_removed', 'description'] 

combined = pd.concat([canadian_youtube, british_youtube])

combined.shape # (79797, 16)
list(combined) 
# ['video_id', 'trending_date', 'title', 'channel_title', 'category_id','publish_time','tags','views','likes','dislikes','comment_count','thumbnail_link','comments_disabled','ratings_disabled','video_error_or_removed', 'description'] 

### JOIN

# join() lets you combine different DataFrame objects which have an index in common. Obviously you can achieve this where 2 dfs have a column in common you can set that column to be the index/ group by

# For example, to pull down videos that happened to be trending on the same day in both Canada and the UK, we could do the following:


# BEFORE RE-INDEX
canadian_youtube.shape # ((40881, 16))
canadian_youtube.index # RangeIndex(start=0, stop=40881, step=1)

# RE-INDEX
left = canadian_youtube.set_index(['title', 'trending_date'])
left.shape # (40881, 14)
left.index 
# MultiIndex...names=['title', 'trending_date'], length=40881)
list(left)
    #['video_id', 'channel_title', 'category_id','publish_time','tags','views','likes','dislikes','comment_count','thumbnail_link','comments_disabled','ratings_disabled','video_error_or_removed','description']

# BEFORE RE INDEX
british_youtube.shape # (38916, 16)
british_youtube.index # RangeIndex(start=0, stop=38916, step=1)

# RE INDEX
right = british_youtube.set_index(['title', 'trending_date'])
right.shape # (38916, 14)
right.index #  MultiIndex...names=['title', 'trending_date'], length=38916)
list(right)
    #['video_id', 'channel_title', 'category_id','publish_time','tags','views','likes','dislikes','comment_count','thumbnail_link','comments_disabled','ratings_disabled','video_error_or_removed','description']

#JOINING ON COMMON INDEX

joined = left.join(right, lsuffix='_CAN', rsuffix='_UK')
joined.shape # (40900, 28)
joined.index
# MultiIndex...names=['title', 'trending_date'], length=40900)
list(joined)
# ['video_id_CAN', 'channel_title_CAN','category_id_CAN','publish_time_CAN','tags_CAN','views_CAN','likes_CAN','dislikes_CAN','comment_count_CAN','thumbnail_link_CAN','comments_disabled_CAN','ratings_disabled_CAN','video_error_or_removed_CAN','description_CAN','video_id_UK','channel_title_UK','category_id_UK','publish_time_UK','tags_UK','views_UK','likes_UK','dislikes_UK','comment_count_UK','thumbnail_link_UK','comments_disabled_UK','ratings_disabled_UK','video_error_or_removed_UK','description_UK']


# The lsuffix and rsuffix parameters are necessary here because the data has the same column names in both British and Canadian datasets. If this wasn't true (because, say, we'd renamed them beforehand) we wouldn't need them. I.E you can have only the common index in common and all other columns different in which case you dont have to specify the suffex's

# SO WHAT SEEMS TO BE HAPPENING HERE, IS THAT RATHER THAN SIMPLY CONCATINATING ENTRIES AND HAVING A DF THATS EXPANDED IN NUMBERS OF ENTRIES. HERE BECAUSE THE TWO DFS RELATE TO THE SAME ENTRIES (I.E. YOUTUBE VIDEOS, THAT HAVE THE SAME TITLE) INSTEAD OF ADDING NEW ENTRIES, WE ARE SIMPLY JOINING THE UK INFORMATION ABOUT THE ITEM WITH THAT INDEX, TO THE THE CANADIAN INFORMATION ABOUT THAT THING. SO THE INDEXES ARE PRESERVED BUT THE NUMBER OF COLUMNS/DATA POINTS FOR THAT INDEX ARE EXPANDED. 

### Examples
# 1
# region_1 and region_2 are pretty uninformative names for locale columns in the dataset. Create a copy of reviews with these columns renamed to region and locale, respectively.

renamed = reviews.rename(columns={"region_1": 'region', 'region_2': 'locale'})

# 2
# The Things on Reddit dataset includes product links from a selection of top-ranked forums ("subreddits") on reddit.com. Run the cell below to load a dataframe of products mentioned on the /r/gaming subreddit and another dataframe for products mentioned on the r//movies subreddit.

gaming_products = pd.read_csv("./dataForKaggleNotes/gaming.csv")
gaming_products.shape # (493, 6)
list(gaming_products) 
# ['name',
#  'category',
#  'amazon_link',
#  'total_mentions',
#  'subreddit_mentions',
#  'subreddit']

movie_products = pd.read_csv("./dataForKaggleNotes/movies.csv")
movie_products.shape # (303, 6)
list(movie_products) 
# ['name',
#  'category',
#  'amazon_link',
#  'total_mentions',
#  'subreddit_mentions',
#  'subreddit']

# Create a DataFrame of products mentioned on either subreddit.

combined_products = pd.concat([gaming_products, movie_products])

# 3

# The Powerlifting Database dataset on Kaggle includes one CSV table for powerlifting meets and a separate one for powerlifting competitors. Run the cell below to load these datasets into dataframes:

powerlifting_meets = pd.read_csv("./dataForKaggleNotes/meets.csv")
powerlifting_meets.shape # (8482, 8)
powerlifting_meets.index # RangeIndex(start=0, stop=8482, step=1)
list(powerlifting_meets) 
# ['MeetID', 'MeetPath','Federation','Date', 'MeetCountry','MeetState','MeetTown','MeetName']

powerlifting_competitors = pd.read_csv("./dataForKaggleNotes/openpowerlifting.csv")
powerlifting_competitors.shape # (386414, 17)
powerlifting_competitors.index # RangeIndex(start=0, stop=386414, step=1)
list(powerlifting_competitors)
#['MeetID', 'Name','Sex','Equipment','Age','Division','BodyweightKg','WeightClassKg','Squat4Kg','BestSquatKg','Bench4Kg','BestBenchKg','Deadlift4Kg','BestDeadliftKg','TotalKg','Place','Wilks']

# Both tables include references to a MeetID, a unique key for each meet (competition) included in the database. Using this, generate a dataset combining the two tables into one.

leftSide = powerlifting_competitors.set_index(["MeetID"])
leftSide.shape # (386414, 16)
leftSide.index # Int64Index([0,0,...8481], dtype='int64', name='MeetID', length=386414)

rightSide = powerlifting_meets.set_index(["MeetID"])
rightSide.shape # (8482, 7)
rightSide.index
# Int64Index([0,1,2, ...8481], dtype='int64', name='MeetID', length=8482)

joined = leftSide.join(rightSide)
joined.shape # (386414, 23)
joined.index
# Int64Index([0,0,...8481, 8481], dtype='int64', name='MeetID', length=386414)
list(joined)
# ['Name','Sex','Equipment','Age','Division','BodyweightKg','WeightClassKg','Squat4Kg','BestSquatKg','Bench4Kg','BestBenchKg','Deadlift4Kg','BestDeadliftKg','TotalKg','Place','Wilks','MeetPath','Federation','Date','MeetCountry','MeetState','MeetTown','MeetName']

# EXPERIMENT 
joinedReverse = rightSide.join(leftSide)
joinedReverse.shape