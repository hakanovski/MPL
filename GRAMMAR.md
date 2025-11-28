# 📜 MPL Grammar (EBNF Definition)

This document defines the formal grammar of the **Magick Programming Language (MPL)** version 0.1.0-alpha. It is used by the Lexer and Parser to validate the structure of ritual scripts.

## Notation
The grammar is defined using **Extended Backus-Naur Form (EBNF)**.

```ebnf
(* ========================================== *)
(* TOP LEVEL STRUCTURE                        *)
(* ========================================== *)

program         = { statement } ;

statement       = invocation
                | binding
                | casting
                | transmutation
                | loop_block
                | conditional
                | comment ;

block           = "{" , { statement } , "}" ;

(* ========================================== *)
(* CORE OPERATIONS (RITUAL ACTIONS)           *)
(* ========================================== *)

(* Invoking an Entity from the Ontology *)
invocation      = "invoke" , "." , entity_id , "(", [ parameters ] , ")" ;

(* Assigning a value to a variable *)
binding         = "bind" , variable_name , "to" , expression ;

(* Executing a named function or spell *)
casting         = "cast" , spell_name , [ "with" , parameters ] ;

(* Converting data types *)
transmutation   = "transmute" , target , "->" , result_type ;

(* Tesla Protocol Loops (Resonance Cycles) *)
loop_block      = "cycle" , "(", frequency , ")" , block ;

(* Logic Control *)
conditional     = "if" , condition , block , [ "else" , block ] ;

(* ========================================== *)
(* EXPRESSIONS & TYPES                        *)
(* ========================================== *)

expression      = literal 
                | variable_name 
                | function_call 
                | binary_op ;

parameters      = param_pair , { "," , param_pair } ;
param_pair      = identifier , "=" , expression ;

condition       = expression , operator , expression ;
operator        = "==" | "!=" | ">" | "<" | ">=" | "<=" ;

(* ========================================== *)
(* PRIMITIVES                                 *)
(* ========================================== *)

entity_id       = identifier ; (* e.g., hermes, tesla, solomon *)
variable_name   = identifier ;
spell_name      = identifier ;
target          = identifier ;

result_type     = "Sigil" | "Flux" | "Mana" | "Vessel" | "Void" ;

frequency       = integer ; (* strictly: 3, 6, or 9 in Tesla Protocol *)

identifier      = letter , { letter | digit | "_" } ;
literal         = string | number | boolean ;

string          = '"' , { character } , '"' ;
number          = digit , { digit } , [ "." , { digit } ] ;
boolean         = "True" | "False" ;

comment         = "#" , { character } ;


🔮 Syntax Examples
Below are valid code snippets derived from the grammar above.
1. Invocation (Calling an Entity)
# Calls the 'Hermes' object from data/magi_225.json
invoke.hermes(intent="clarity", duration=300)

2. Binding (Variable Assignment)
# Binds the value 100 to the variable 'mana_pool'
bind mana_pool to 100
bind target_sigil to "PROTECT"

3. Tesla Cycle (Loop)
# A loop that repeats based on the Tesla 3-6-9 key
cycle(3) {
    cast cleanse_memory
    bind entropy to entropy + 1
}

4. Transmutation (Type Conversion)
# Converts a string (Sigil) into an integer (Mana)
transmute input_text -> Mana
