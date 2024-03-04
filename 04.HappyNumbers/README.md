# Happy Numbers
In this python project I dived into the world of happy numbers. A number is considered "happy" if by operating a mathematical sequence on that, it results in 1.  The process is as:
 - start with a positive integer
 - replace it with the sum of the squares of its digit
 - reapeat the process until you end up with a single digit number
If you eventually end up with 1, then the positive intiger is a happy number.

Take 19 as an example:
 - $1^2 + 9^2 = 82$
 - $8^2 + 2^2 = 68$
 - $6^2 + 8^2 = 100$
 - $1^2 + 0^2 + 0^2 = 1$

The goal if this project is to take any given integer and indicate if it is a happy number or not.

## Project Structure
```
HappyNumbers/
|
|--src/
|   |HappyNumbers.py
|   |HappyNumbers.ipynb
|
|--README.md -> This File
|--requirement.txt
|--.gitignore

```

## Process and How to run
To implement a process which indicates the happy numbers, I first took a number and applied the process of taking the sum of the squares of its digit until it is a single digit number. Then it returns whether the original number is happy (`True`), or not (`False`).
To run the script use the following command:
```
python ./src/HappyNumbers.py
```