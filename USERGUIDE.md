
# **SNAKEPEOPLE User Guide** 🐍

So, you've slithered on over to the SNAKEPEOPLE UML editor user guide... Well you're in luck, this document provides a rundown on how to use Snake_UML to generate and modify UML class diagrams.

There are two user interfaces that are available for use in editing said diagrams -- the GUI (Graphical User Interface) and CLI (Command Line Interface). 
This guide will describe how to use the features within each interface.

### Tips and Tricks
- Type `help` to see all available commands while in the CLI.
- Type `help <command>` to see helpful information relevant to the command you're trying to execute. 
- Consume rodents and small animals while sliding across the ground to be considered a snake by your peers.<br />
## **How to Run**
1. First task is to navigate to the main repo on Github and download the latest version of SNAKEPEOPLE UML editor. [repo](https://github.com/mucsci-students/2021fa-420-SNAKEPEOPLE)
2. Make sure you have the latest version of python language installed on your machine as outlined in the README (https://www.python.org/downloads/)
3. Once the repo is downloaded, navigate to it using your favorite terminal. If you don't know how, check this website out first and learn how you beautiful snake. [learn terminal](https://www.digitalocean.com/community/tutorials/basic-linux-navigation-and-file-management)
4. Your terminal should be in the `/2021fa-420-SNAKEPEOPLE/` directory for the next steps. 
5. Next, execute `pip install -r requirements.txt` when in the above directory to install the necessary libraries for the program to function.
6. __Now it's time to run!__ (the program)
7. In order to run in **GUI** mode, execute `python snake_uml.py` with no flags. This will bring up the glorious GUI.
8. In order to run in **CLI** mode, execute `python snake_uml.py --cli`. This command has the **--cli** flag to specify you want the CLI. Reference the below commands for help in the CLI. 
9. If everything worked then you should be enjoying UML right now, have fun!


### **CLI commands** 🐍<br /> 

#### Class Commands 

- `addclass <classname>`  
  - Add a new class to the system. The provided class name must not already exist in the system.
- `delclass <classname>` 
  - Delete a class from the system forever. The provided class name must exist in the system in order to be deleted. When a class is deleted, all attributes attached to the class and all relationships associated with the class are also deleted.
- `renclass <classname> <newname>` 
  - Rename an existing class that is in the system. All attributes attached to the class and all relationships associated with the class are also updated upon the renaming of the class.
#### Relationship Commands
- `addrel <source> <destination> <type>`  
  - Add a new relationship between two classes. Both the source class and the destination class specified by the user have to exist in the system. The relation type must be one of the following: "aggregation", "composition", "inheritance", "realization". <br />
- `delrel <source> <destination>`   
  - Delete a relationship between two classes in the system. Both
     		user-specified class names must exist and must already have an
     	 	existing relationship.
#### Field Commands
- `addfield <classname> <fieldname> <type>` 
  - Adds a new field to a given class in the system. The class name must
     		be one that exists in the system. The field must also not share a
      	 	name with another field in the class.
- `delfield <classname> <fieldname>`
  - Deletes a field from a class in the system. The class name and field 
     	 	name must both be ones that exist in the system, and the field must be
       	in the specified class.
- `renfield <classname> <fieldname> <newname>`
  - Renames an existing field in a class in the system. The class name and
		current field name must both exist in the system, and the current field
		must be in the specified class. The new field name must not be one that
		already exists in that class.
#### Method Commands
- `addmethod <class name> <method name> <method return type>`
  - Adds a new method to a given class in the system. The class name must
      		be one that exists in the system. The method must also not share a
      		combination of the same name and return type as another method in the
      		class. 
- `delmethod <class name> <method name> <method return type>`
  - Deletes a method from a class in the system. The class name and method name must both be ones that exist in the system, and the method must be in the specified class, with the specified method type.
- `renmethod <class name> <method name> <method return type> <new name>`
  - Renames an existing method in a class in the system. The class name and
        	current method name must both exist in the system, and the current
       	 method must be in the specified class with the specified type. The new
       	 method name must not be one that exists in that class already.
#### Parameter Commands
- `addparam <class name> <method name> <method type> <param name> <param type>`
  - Adds a parameter to a method in the system. The specified class name
       	 must have the method with the method type. The param name with the
       	 specified type must not already exist in that method.
- `delparam <class_name> <method name> <method type> <param name>`
  - Deletes a parameter from a method in the system. The specified class
      	  	name must have the method with the method type, and the param with the
      	 	 method.
- `renparam <class_name> <method name> <method type> <param name> <new name>`
  - Renames an existing parameter in a method in the system. The specified
    		class name must have the method with the method type. The new param
        	name must not be one that exists in the method already.
#### List Commands
- `listclass <class_name>`
  - If the user inputs 'all' as the input, list all the classes in the current system, as well as their contents. If the user inputs the name of a class in the system, lists the contents of the specified class.
- `listrel`
  - List all the relationships that exist between classes in the
       	 current system.
#### Bonus Special Commands for only the most dedicated snakes
- `undo`
  - Undo the last performed action, returning the UML to the state it was
       	 previously at.
- `redo`
  - Redo the last action that was undid by the user.
- `save filename [<flag> <path>]`
  - Saves the current work to a JSONfile, with a user-specified name.
- `load <flag> [<file name> | <path to file>]`
  - Load a JSON file, providing the name or path of an existing file.
    - Flags: `-e, --external`
      - `load [-e | --external] <path to file>`
    - Indicates that a file is to be loaded from an external directory. A complete path to the file must be provided after the flag.
    - Flags: `-i, --internal`
      - `load [-i | --internal] <file name>`
- `help`
  - Get help young snake person
- `exit`
  - Quit the program.



## It's time to get GUI

##### The GUI is a graphical way to see all of the commands that were just listed above. <br />
##### Each command has a button in the GUI and they provide the same functionality as the CLI. <br />
##### It looks prettier to your very perceptive snake eyes and there are even colors! <br />
##### The top of the GUI window has "File" header for saving and loading while the "edit" header has undo and redo and such. <br />
##### When you click on a button that has your preferred action, a second window will pop up where you can make your changes. <br />
##### Some have dropdowns for various selections and there are confirm buttons to solidify your choices. <br />
##### Once you are satisfied with the pretty boxes or are just done making changes, you can see the canvas on the main GUI windows accept your changes provided they were okay with the program. <br />

#### Wow what a great experience that was! You are now a certified snake and we hope you enjoy making UML with SNAKEPEOPLE's UML editor
