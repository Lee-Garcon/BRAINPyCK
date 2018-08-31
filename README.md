# BRAINPyCK

What it is: An advanced interpreter written using python





# Features

### Macros
The groundbreaking, brainfuck-purpose-defying feature is here! With BRAINPyCK, you can now create macro shortcuts in your code! (recursives sold separately)

To specify a macro, start with the '$' symbol and then the character you will use as a shortcut and the list of commands you want it to represent. To end the macro, put a '%' symbol after it.

#### Examples of Macros

Command for transferring values from one cell to another:

    $x[->+<]%

Command for Addition:

    $y[->>+<<]>[->+<]>.%



### Comments

BRAINPyCK can now process comments without breaking down like a script a 13-year old copied off of pastebin to h4x their enemies! yAy!

Example of a comment:

    /This is a comment. The interpreter will skip to the next slash which is this one: -> /

### Input and Output Specifications

You can now specify where the input for your code is coming from! Just specify the input like this:

    interpreter.interpret(predef_input=[*your_input_here*])
    
To set your output to a class variable (interpreter.out):

    interpreter.interpret(output_location='self')
    
To write your output to a file:

    interpreter.interpret(output_location='/i/cant/think/of/interesting/directory/names.txt')
    
# FAQs

### Why is your code so messy?

Did you know that the new MacBook Pro keyboards are garbage and decrease your ability to type? Neither did I, but then my school handed them out so I guess I'm stuck with them.

### I hate you and your project!

OK bye then
