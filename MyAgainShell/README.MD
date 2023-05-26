Интрепретатор 

lexer.py - Лексический нализатор кода
intrep.py - Интрепретатор кода
MyAggainShell - оболочка для интрепретатора


Backus–Naur грамматика:
<digit> ::= [0-9]
<letter> ::= [A-Z] | [a-z]
<symbol> ::= "|" | " " | "-" | "!" | "#" | "$" | "%" | "&" | "(" | ")" | "*" | "+" | "," | "-" | "." | "/" | ":" | ";" | "<" | "=" | ">" | "?" | "@" | "[" | "\\" | "]" | "^" | "_" | "`" | "{" | "|" | "}" | "~"
<character> ::= <letter> | <digit> | <symbol>
<string> ::= <character>*
<int> ::= "0" | ("-"? [0-9] <digit>*)
<decimal> ::= "0.0" | ("-"? [0-9] <digit>* "." [0-9] <digit>* )

<oper> ::= "+" | "-" | "*" | "/"
<logOper> ::= "<" | ">" | "==" | "!=" | "<=" | ">="
<value> ::= <int> | <decimal> | <string>
<staples> ::= "(" <expression> ")"
<logStaples> ::= "(" <logExpression> ")"
<expression> ::= <staples> | (<staples> | <value>) <oper> (<staples> | <value>)
<logExpression> ::= <logStaples> | (<logStaples> | <value>) <logOper> (<logStaples> | <value>)
<if> ::= "if " <logExpression> "\n" <expression> "\n" | else \n " <expression> " \n"
<wile> ::= "while " <logExpression> " \n " <expression> " \n "


Пример запуска:

python3	MyAggainShell.py script.txt



пимер скрипта

a = 2
while a<100:
    a+=1
    if a<80:
        <<a
    else:
        <<("abc"+"df")
        <<a
        b = 0
        while b<3
            <<b
            b+=1
    a+=10
a = 2
b = 1
g = 1+(10+34)*2
t = (a>b) && (b>(a+b))
<<t
t = (a>b) || (b<3)
<<t
g += 1
<<g
>>t
t = t.Upper()+"ssf"
<<t