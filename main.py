import seaborn as sns
sns.lineplot(x=[1, 2, 3], y=[2, 5, 12])

iris = sns.load_dataset('iris')

iris

sns.scatterplot(x=iris.sepal_length,y=iris.sepal_width)

sns.scatterplot(x=iris.sepal_length,y=iris.petal_length)

sns.scatterplot(x=iris.petal_width,y=iris.petal_length)

sns.distplot(iris['sepal_length'])

sns.histplot(iris['sepal_length'])

tips = sns.load_dataset('tips')

tips

sns.scatterplot(x=tips.total_bill,y=tips.tip)

tips.head()

tips['smoker'].value_counts()

sns.scatterplot(data=tips,x=tips['total_bill'],y=tips['tip'], hue = 'smoker' )

sns.scatterplot(data=tips,x=tips['total_bill'],y=tips['tip'], hue = 'size' )

tips['size'].value_counts()

sns.scatterplot(data=tips,x=tips['total_bill'],y=tips['tip'], style = 'size' )

sns.scatterplot(data=tips,x=tips['total_bill'],y=tips['tip'],hue='time' ,style = 'size' )

sns.scatterplot(data=tips, x=tips['day'],y=tips['total_bill'])

sns.scatterplot(data=tips, x=tips['smoker'],y=tips['tip'])

sns.histplot(x=tips['total_bill'],y=tips['tip'])

sns.scatterplot(tips)

sns.scatterplot(iris)

sns.histplot(iris)

