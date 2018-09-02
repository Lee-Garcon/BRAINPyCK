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
    
    
    
# Docs / How To Use

### Step 0: Import the module

If you can't do this why are you on this repo

    import BRAINPyCK as bfpy

### Step 1: Create an interpreter object

Do you know how to make objects? God, I sure hope so.

    interpreter = bfpy.interpreter(*code_goes_here*)

### Step 2: Run it

There's many options to running your code. Read through the Features section first to get a grip.

#### Arguments

##### predef_input

Determines where to get input from.

Default: None

type: list/tuple

example:

    interpreter.interpret(predef_input=[88, 87, 86, 85, 87, 92])
    
##### output_location

Determines where to output all '.' commands

Default: 'print'

type: str

###### options

'self': Outputted to interpreter.out

filepath: Writes to file (file must be accessable)

### Step 3: ???

### Step 4: Profit!

#### You now have an output! How wonderful is that?
