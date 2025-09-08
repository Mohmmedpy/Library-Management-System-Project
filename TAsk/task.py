l={"Book Title1":"The world of math",
    "author1":"saleh"}

show="show all books"
add="add a book"
delete="delete a book"
search="search for a book"
exit="exit"
a=print("Choose",show,"or",add,"or",search,"or",delete,"or",exit)
e=input("Choose ")

if e==show:
    print(l)
elif e==add:
    bookn=input("Write a book title ")
    booka=input("Write a the book author ")
    l["Book Title2"]=bookn
    l["author2"]=booka
    print(l)

    print("The book was not found")
elif e==delete:
    re=input("remove a book ")
    del l[re]
    print(l)
elif e==exit:
    print("Thank you")
