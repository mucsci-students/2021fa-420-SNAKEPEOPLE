import uml_class

classes = uml_class.class_dict

def single_add():
    # Add a single, valid class that doesn't exist.
    uml_class.add_class("Valid")
    print(classes)
    
    # Add a single, valid class that already exists.
    uml_class.add_class("Valid")
    
    # Add a single, invalid class.
    uml_class.add_class("")
    uml_class.add_class(None)

def multi_add():
    pass

def single_delete():
    pass

def multi_delete():
    pass

def main() -> None:
    print("|----------CLASS TESTS----------|")
    option = input("\tChoose an option:\n" +
                   "\t1. Run all tests. [Default]\n" +
                   "\t2. Run add tests.\n" +
                   "\t3. Run del tests.\n" )
    
    if option == "2":
        single_add()
        multi_add()
    elif option == "3":
        single_delete()
        multi_delete()
    else:
        single_add()
        multi_add()
        single_delete()
        multi_delete()

if __name__ == '__main__':
    main()