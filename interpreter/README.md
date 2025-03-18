# DAT259 – Modern Compiler Construction Tools

## Interpreter with ANTLR

What is needed to create an interperter?

- Lexer
- Tokens
- Parser

Connect to another programming language to execute the code.

#### How to create an interpreter?

##### Lexer and tokens

- Create your own programming language

  - Example `hello.edbs`

    ```
    OBS! Detter en kommentar til linje er slutt.
    SKRIV «Hels på deg verda!».
    FERDIG.
    ```

    The file is supposed to output `Hels på deg verda!` in the terminal and can be used as testFile.

- Set up class paths and commands
  ```bash
  export CLASSPATH=".:/usr/local/bin/antlr-4.13.2-complete.jar:$CLASSPATH"
  alias antlr='java -jar /usr/local/bin/antlr-4.13.2-complete.jar'
  alias antdbg='java org.antlr.v4.gui.TestRig'
  ```
- Create a **lexer file** file (`.g4`) and generate a parser `antlr <LanguageName>.g4`
  - Compile lexer and scanner with `javac *.java`
  - Debug lanugage `antdbg <LanguageName> tokens -tokens <testFileWithLanguage>`
  -

##### Syntax-directed translation

- Add **semantic rules to grammar rules**

  - Example

    ```python
    expression : expression '+' expression # add
    | expression '*' expression # mul
    | '(' expresssion ')' # nested
    | INT # lit
    ;
    ```

- Install antlr tools `pip install antlr4-tools`
- Generate **visitor** `antlr <file> -o test-java -no-listener -visitor`
  - Example `antlr4 -Dlanguage=Python3 EDBS.g4 -o edbs -visitor`
- Install runtime library `pip install antlr4-python3-runtime`
- Run python file

  - Example `Driver.py`

    ```python
    import sys

    from antlr4 import \*
    from XLexer import XLexer
    from XParser import XParser

    class MyVisitor(XBaseVisitor):

        def visit_xyz(self, ctx):
            pass

        # ... more visitor methods

    def main(argv): # 2. open input stream
    input*stream = FileStream(argv[1]) # 3. create lexer object
    lexer = ExprLexer(input_stream) # 4. create token stream object
    stream = CommonTokenStream(lexer) # 5. create parser objectt
    parser = ExprParser(stream) # 6. create parse tree by calling the "top-level rule"
    tree = parser.start*()

        # 7. run the visitor
        vizz = MyVisitor()
        vizz.visit(tree)

    if **name** == '**main**':
    main(sys.argv)
    ```
