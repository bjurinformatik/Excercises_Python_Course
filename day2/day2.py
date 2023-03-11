###################
# Day 2 exercises #
###################

# Before staring, clone the exercise repository from github to the local computer so all scripts can be uploaded there
cd ~/Documents/Courses/python_2023/exercises
git clone https://github.com/bjurinformatik/Exercises_Python_Course.git
cd Exercises_Python_course

#-------------------------#
# Create a python package #
#-------------------------#

#Create directory for package
mkdir animals

#Add modules mammals.py, birds.py and __init__.py file

#Content of initial __init__.py
from .mammals import Mammals
from .birds import Birds

#Create a test file outside of the package and run it
cd ..
nano test_animals.py
chmod 755 test_animals.py 
./test_animals.py

#Edit animals to work with new script
cd animals
mkdir harmless dangerous
mv birds.py harmless
cd harmless
nano __init__.py

#Create fish.py inside dangerous directory
cd dangerous
nano fish.py
nano __init__.py

#__init__.py file edited to work for new script.

#Create a new test file outside the project
nano test_updated_animals.py
chmod 755 test_updated_animals.py
./

#-----------#
# Debugging #
#-----------#

# Clone day 2 repository
git clone https://github.com/bjurinformatik/day2-bestpractices-1.git
cd /day2-bestpractices-1/buggy

#Added a debugger to the code and looked through the scripts and how the package was running.
	#Did some changes in the modules in the package but did not manage to solve the task entirely.

#-----------#
# Profiling #
#-----------#

#Using cProfile
python -m cProfile matmult.py

#Using line_profiler
kernprof -l -v euler72.py

#matmult.py script - would start optimisation on line 9 and 14
#euler72.py script - would start optimising speed at line 52

#Optimised script: optimised_matmult.py, done after day3 so used numpy.
