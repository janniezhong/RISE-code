
# Machine Learning - Supervised learning, a classification task
# Exercise based on Chapter 3 of ...


# Although we are working in python version 2, we can include these extra packages to support both python 2 and python 3
from __future__ import division, print_function, unicode_literals

# Other packages that we need to import for use in our script
import numpy as np
import os

# to make this script's output stable across runs, we need to initialize the random number generator to the same starting seed each time
np.random.seed(42)

# To plot nice figures
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

# Where to save the figures that our code generates
def save_fig(fig_id, tight_layout=True):
    path = os.path.join("ML_" + fig_id + ".png") #PROJECT_ROOT_DIR, "images", CHAPTER_ID, fig_id + ".png")
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format='png', dpi=300)

####################
# STEP 1: OBTAIN THE DATA
####################

# Now, we need to download a dataset to work with
# The sklearn package has a function that can download the data for us:
from sklearn.datasets import fetch_mldata

# TO DO: use the fetch_mldata function to download the dataset
#        and load it into our workspace with the variable name
#        'mnist'.  The fetch_mldata function takes one argument,
#        the name of the dataset we want to download. The name 
#        of the dataset to download is 'MNIST original'.
import mnistbackup
mnist = mnistbackup.load_obj("mnist")

# Now, If we want to display part of the dataset on the screen, we can simply
# enter the name of the variable we called it:


# TO DO: We can see that our variable is a dictionary. It contains multiple 
# fields that are named and have different types of data in them. If we want
# a clearer look at just the field names in the dictionary, we can use the 
# "keys()" function by entering our variable name followed immediately by 
# ".keys()"  (but without the quotes around it):
mnist.keys()


# TO DO: let's organize our dataset into two variables, one a matrix that contains
#        all the descriptions of the handwritten numbers (in the "data" key of the
#        dictionary) and one a vector that contains the labels for each of those
#        numbers, the label being the actual number that was written (in the "target"
#        key of the dictionary).
#        Let's name the matrix of handwriting data "X" and the vector of labels "y":
X = mnist[b'data']
y = mnist[b'target']

# TO DO: Now, we can check the size of our dataset by using the shape function (this is
#        one of the few times where we need to call it without adding parenthesis at the
#        the end). We can call this function on our dataset by adding ".shape" to the
#        variable name:
X.shape

# Now we see that our matrix has 70,000 rows, meaning it describes 70,000
# handwritten numbers. The matrix has 728 columns, so each of the 70,000
# handwritten numbers in our database is described by 728 data points. These points
# define a 28 pixel x 28 pixel square. There is one data point for each pixel in the
# square, which gives the shade of gray in that square (anything from white to black
# and all the shades of gray in-between). If we were to graph a figure using the data
# for one of those handwritten numbers, we would get a 28x28 sized square that depicts
# a single hand-written number.

####################
# STEP 2: EXPLORE THE DATA
####################

# TO DO: Import the plotting package matplotlib. Uncomment the following
#        two lines to import matplotlib and to have a short way to refer
#        to its subpackage pyplot:
import matplotlib
import matplotlib.pyplot as plt

# TO DO: Let's look at one of the numbers described in our matrix. First, define a new
#        variable called 'some_digit' that is equal to one of the rows of data in matrix X:
some_digit = X[0]

# TO DO: Now, we need to reshape that row into a square, the 28x28 square that can
#        represent the picture of that handwritten number. We can do this using the
#        "reshape" function, which takes two arguments, the row and column dimensions
#        to reshape our variable into:
some_digit_image = some_digit.reshape(28, 28)

# TO DO: Next, we need to use pyplot's "imshow" function to show our image. The arguments
#        it takes are the 28x28 matrix we just made to describe the image, a colormap that
#        tells pyplot which colors are represented by which values found in the matrix, and
#        a method for handling values in the matrix that don't exactly match the values
#        defined in the color map (ex: if the color map only says 0.1 = almost black and
#        0.5 = medium gray, pyplot needs to know what to do for the value 0.3). Uncomment
#        the following lines to show a picture of the handwritten number:
#plt.imshow(some_digit_image, cmap = matplotlib.cm.binary,interpolation="nearest")
#plt.axis("off")
#plt.show()

# TO DO: What if we want to look at other numbers in our dataset? It's more efficient
#        to write a function that repeats the steps we just did:
#        Given a row of the matrix, the function should reshape it into a 28x28 square,
#        plot it in an image using the imshow function, and then turn the axis off so
#        that the resulting figure looks like an image and not a graph. Try defining a
#        function called 'plot_digit' that accomplishes this task, where 'data' is the
#        name given the incoming argument (the row of the matrix with 728 data points).
#        Remember to indent the substatements of the function by four spaces:
def plot_digit(data):
    some_digit = data
    some_digit_image = some_digit.reshape(28, 28)
    plt.imshow(some_digit_image, cmap = matplotlib.cm.binary,interpolation="nearest")
    plt.axis("off")
    plt.show()
        

# TO DO: Now, let's test out our new function on the handwritten number in row
#        3600 of our X matrix. We should be able to call it as follows:
#plot_digit(X[36000])

# What number do you see when you call that function? Is the number hard to read?
# What number is the computer likely to think it is? If you are unsure what number
# it is, can you think of an easy way to find out?

# TO DO: Sometimes we may want to view a whole bunch of numbers at once. For that,
#        we can define a different function that shows many numbers together. The
#        function is already written for you here, just uncomment each line. As you
#        uncomment each line, take a look at it to see if you can figure out what
#        that line of code is doing:
def plot_digits(instances, images_per_row=10, **options):
    size = 28
    images_per_row = min(len(instances), images_per_row)
    images = [instance.reshape(size,size) for instance in instances]
    n_rows = (len(instances) - 1) // images_per_row + 1
    row_images = []
    n_empty = n_rows * images_per_row - len(instances)
    images.append(np.zeros((size, size * n_empty)))
    for row in range(n_rows):
        rimages = images[row * images_per_row : (row + 1) * images_per_row]
        row_images.append(np.concatenate(rimages, axis=1))
    image = np.concatenate(row_images, axis=0)
    plt.imshow(image, cmap = matplotlib.cm.binary, **options)
    plt.axis("off")


# TO DO: Now, we can make use of this new function to show many handwritten
#        numbers at a time. Uncomment the following lines to show many numbers:
#plt.figure(figsize=(9,9))
#example_images = np.r_[X[:12000:600], X[13000:30600:600], X[30600:60000:590]]
#plot_digits(example_images, images_per_row=10)
#plt.show()



####################
# STEP 2: SEPARATE TRAINING AND TEST DATA
####################

# TO DO: We need to separate both our number data matrix (X) and
#        the vector of labels that contains the true identity of
#        each number (y). We have 70,000 numbers total, so lets
#        use 60,000 numbers for training and 10,000 for test.
#        Use your knowledge of slicing arrays to select the first
#        60,000 numbers for training and the last 10,000 for testing:
X_train = X[:60000]
X_test = X[60000:]
y_train = y[:60000]
y_test = y[60000:]


# Next, let's shuffle the data in case there is an order to the
# numbers in our matrix. Machine learning algorithms may be thrown
# off if a lot of the same number are presented in a row or if the
# order of numbers presented follows a specific pattern. Therefore,
# we will randomly rearrange the numbers in our test data set to
# disrupt any patterns in the presentation of the numbers.

# TO DO: Uncomment the following code to load in a new module and
#        create a vector that will list the row indices of our
#        test matrix in random order. Then we can use that vector
#        to rearrange the test matrix:
import numpy as np

shuffle_index = np.random.permutation(60000)
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]



####################
# STEP 3: TRAIN THE NETWORK
####################

# We'll first start with a simpler task of having the network
# only differentiate between 5s and everything else.

# We need to copy the rows from our data matrix that correspond
# to the number 5. However, the only way to know which rows
# represent 5s is to consult our label vector. We can create a
# vector of row indices that correspond to 5s from our label
# vector using the commands below. Notice that we have to do
# this both for the training vector and for the test vector.

# TO DO: Uncomment the code below to create vectors that
#        list whether each entry in the training and test sets
#        is a 5 or is not a 5:
y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)


# Now, we are ready to train our network using the training
# data. The algorithm we want to use, SGDClassifier, must
# be imported from the sklearn module.

# TO DO: Uncomment the code below to import the algorithm:
from sklearn.linear_model import SGDClassifier

# TO DO: Now, we need to call the SGDClassifier. This function
#        requires two named arguments, max_iter and random_state.
#        The max_iter argument sets the maximum number of
#        iterations to perform while learning the task (it is
#        a coincidence that this number should be set to 5). The
#        random_state argument lets us specify a random seed
#        to use to initialize our network. Lets use 42. Set the
#        output of the function to 'sgd_clf'. This represents
#        our learning algorithm object.
#
sgd_clf = SGDClassifier(max_iter=10, random_state=4)

# TO DO: Next, we need to provide our learning algorithm with the
#        training data and its corresponding labels. Because we
#        created a new vector called y_train_5, our labels for this
#        task are no longer the actual number represented by the
#        training data, but are instead all set to 0 for numbers
#        that are not 5 and to 1 for numbers that are 5.  Call the
#        fit() method of the sgd_clf object with two arguments, the
#        training data set and the new label vector (with 0 for non-5
#        and 1 for 5).
sgd_clf.fit(X_train, y_train_5)


# TO DO: Now let's see what our trained algorithm thinks that strange
#        looking number is. Uncomment and run the following code to
#        find out:
some_digit = X_train[43679]
sgd_clf.predict([some_digit])

####################
# STEP 5: EVALUATE THE NETWORK PERFORMANCE
####################

# To DO: Now we want to measure the performance of the training algorithm
#        taking into account all of the training data. We can find out the
#        exact performance of the algorithm because we know the real identities
#        of the number samples and we know what the algorithm came up with
#        for each sample. We need to import the function 'cross_val_score'
#        from sklearn.model_selection and then call that function with the
#        arguments 'sgd_clf' (the learning algorithm object), our training
#        dataset, our label vector that labels whether each training row
#        is a 5 or not a 5 (called y_train_5, don't use the other vector y_train
#        for this exercise), and two named arguments: cv=3, scoring="accuracy"
from sklearn.model_selection import cross_val_score
print("cross_val_score = ", cross_val_score(sgd_clf, X_train, y_train_5, cv = 3, scoring = "accuracy"))


# Before we go any further, refer back to the steps in Exercise 1 of the
# Machine Learning lab in your lab manual. Let's discuss the performance
# of the model and then see how we can better measure the performance.

from sklearn.metrics import confusion_matrix

confused = confusion_matrix(y_train_5, sgd_clf.predict(X_train))
print(confused)
plt.imshow(confused)
plt.show()
