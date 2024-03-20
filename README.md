# Depression Level Assignment (DLA)
#### Video Demo:
#### Description:
This is my CS50P final project, dedicated to implementing depression levels test into the interactive form using python.
Initial idea was to make a test which would first ask a permission to participate in taking a test, greeting a person even if they choose to don't participate.

If the person chose to take a test, it starts to bring question one by one, including question number. To make experience more comfortable, I added some little stops between questions using 'time' library.

User can only choose numbers between 1 and 4. Everything besides that leads to reprompt by a program with additional info message. It was done using 'try' and 'Except' statements with converting input to an integer, checking ValueError and if number is in accepted range. Same idea was later implemented with making choices when answering questions.

The way program sends question is using a while loop with a counter. I made an external library, containing lists for every question, so that when printing a question, it would 'numerate()' and display only needed answers.

Anwering a question puts a choice in a list, which then sums together and goes to the result function in the program.

When user answers all of the asked questions, a special function will calculate the result and return a value. Depression test itself is easy to calculate, so the function just substracts the amount of questions from the sum of inputs.

Then the result goes to the function, specially dedicated for showing a result to the end user. It shows an amount of points user got and also shows possible diagnosis on the basis of the Beck's Depression Inventory.

#### Encountered problems:
 1. Biggest problem was with checking if the user inputs a word or not. The cause of the problem was that I placed a function call inside a 'try' and 'Except' statements which were used to check what user types to participate in taking a test. So whenever someone was taking a test and randomly or maliciously typed a string, it would wipe all the posssible progress and reprompt to participate or not. Solved it moving a function call, but now when user mistypes on the first stage, program exits with a text hint.
