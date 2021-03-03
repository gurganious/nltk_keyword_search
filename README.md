# nltk_keyword_search

In response to [https://stackoverflow.com/questions/66323508/parsing-and-avoiding-nested-loops-in-python/66444331?noredirect=1#comment117472485_66444331](https://stackoverflow.com/questions/66323508/parsing-and-avoiding-nested-loops-in-python/66444331?noredirect=1#comment117472485_66444331)

i have a sql table with 12000 entries stored in a dataframe df1 which looks like this:

id	name
00001	angiocarcoma
00261	shrimp allergy
and i have another table with 20000 entries which is stored in dataframe df:

Entry_name	CA
TRGV2	3BHS1 HSD3B1 3BH HSDB3
TRGJ1	3BP1 SH3BP1 IF
The aim is to match for each possible combination of name from df1 with that of CA(splitted with " " space) from df in a sentence with a condition that length of CA cell value should be greater than 2. The simplest logic would be to search for all the name values from df1 in the sentence and if a match is found then search for CA values in the same sentence. But doing that i am limiting resource usage.

Following is the code which i have tried and i can only think of nested loops to accomplish the task. If i use two functions then i am creating a functon calling overhead and if i try to do it recursive then if am exceeding the recusrive function call in Python which is forcing the kernel to shut off. The following function is called by passing a sentence (i have to parse 500k sentences) to it:

