/*
Declaring Variables: var, let, const	let 

Syntax: < var_name > = < value >	

Description: 
var - global access, value can chage
let - access within block where it is declared, value can change
const - access within block where it is declared, value cannot change	

Example: 
let i = 5;
var myStr = "John";
const pi = 3.14

*/

/*
Strings


Declaring: length

Syntax: string_obj.length	

Description: length Returns the length of the string	

Example: let myStr = "Hello"; console.log(myStr.length); --> Output is 5


Declaring: split

Syntax: string_obj.split(separator)	

Description: split Splits the string based on the separator and returns an array.	

Example: let myStr = "Hello! How are you?"; console.log(myStr.split()); --> Output is [ 'Hello!', 'How', 'are', 'you?' ]
 

Declaring: replace

Syntax: string_obj.replace("SearchValue","NewValue")

Description: replace searches a string for a specified value, or a regular expression, and returns a new string where the specified values are replaced.	

Example: let myStr = "Hello User"; console.log(myStr.replace("User","World")); --> Output is Hello World


Declaring: substring

Syntax: string_obj.substring(start, end)

Description: substring is used to extract characters, between to indices from the given string, and returns the substring. It excludes the last index

Example: let myStr="Hello"; console.log(myStr.substing(1,4)); --> Output is ell


Declaring: startswith

Syntax: string_obj.startsWith(searchvalue)

Description: startsWith returns true if a string begins with a specified string, otherwise false	

Example:  let myStr="Hello from the other side"; console.log(myStr.startsWith("Hello")); --> Output is true

*/