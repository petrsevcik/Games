# Caesar Cipher

In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.

It is a type of substitution cipher in which each letter in the text is replaced by a letter some fixed number of positions up or down the alphabet.

For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.

The method is named after Julius Caesar, who used it in his private correspondence.

## Task

Your task is to write a function that accepts exactly 2 arguments (string, shiftkey) and encrypts the given string.
Any character that is not a letter should stay unchanged.

Assumption: shiftkey is an integer from an interval of [-25, 25].

## Examples

cipher("Abcd", 2) should return "Cdef"

cipher("message", -1) should return "ldrrzfd"

cipher("ZZ Top", 3) should return "CC Wrs"
