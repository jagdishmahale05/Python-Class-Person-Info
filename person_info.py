class person :
    def __init__(mysillyobject ,fname , lname , roll , clgname , branch , address ):
        mysillyobject.fname = fname
        mysillyobject.lname = lname
        mysillyobject.roll = roll
        mysillyobject.clgname =clgname
        mysillyobject.branch = branch
        mysillyobject.address = address

    def myfunc(jagdish):
        print("my name is "+ jagdish.fname + "my last name is "+ jagdish.lname + "my roll no. is " + jagdish.roll
              + " clg is "+ jagdish.clgname + "branch is " + jagdish.branch + " address is " + jagdish.address
              )

x = person("jay ","mahale ", "21", "dfghjktyui", "AIDS ", "nashik ")
x.myfunc()
