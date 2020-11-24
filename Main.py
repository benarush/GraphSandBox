# Written on Python 3.8.1 and Testing on linuxs & windows .
# I decided to Write SandBox Client to Graph app .
# Dependencies libraries : json , matplotlib , xml for fast installation  - > pip install matplotlib
from SandBox import App

# by defuelt the file name will be app.xml , its for option to load from different file .
my_app = App(filename="app.xml")

# you can set title , color , user & password:)
my_app.setTitle("Wassup :) ")
my_app.setColor("green")

# Get Data for x , y Coordinates
my_app.getSamples()

if my_app.success:
    # Create Graph Obj and feed matplot Obj
    my_app.createGraph()

    # Show Graph
    my_app.graph.display()

    # Apply changes from SandBox Mode to Prod (Write changes to the configuration file )
    my_app.saveChanges()
else:
    print("Credentials Wrong , user need to be 'root' & and password '123456' "
          "OR Check Connection to the server ")


#print(repr(my_app))
#print(repr(Config()))