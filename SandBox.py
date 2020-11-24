import os
import xml.etree.ElementTree as ET
import random
import matplotlib.pyplot as plt


class Config:
    CONFIG_DIR = os.path.join(os.path.dirname(__file__), "config")

    def __init__(self, filename="app.xml"):
        self.filename = filename
        self.config_File = os.path.join(self.CONFIG_DIR, filename)
        self.xmlRoot = ET.parse(self.config_File)
        self.loadConfiguration()

    def loadConfiguration(self):
        self.XML = ET.parse(self.config_File)

    def saveChanges(self):
        self.XML.write(self.config_File)

    def setTitle(self, title):
        self.XML.getroot().attrib['title'] = title

    @property
    def title(self):
        return self.XML.getroot().attrib['title']

    def setColor(self, color):
        self.XML.getroot().attrib['color'] = color

    @property
    def color(self):
        return self.XML.getroot().attrib['color']

    def setUser(self, user):
        self.XML.getroot().attrib['user'] = user

    @property
    def user(self):
        return self.XML.getroot().attrib['user']

    def setPassword(self, password):
        self.XML.getroot().attrib['password'] = password

    @property
    def password(self):
        return self.XML.getroot().attrib['password']

    def __repr__(self):
        return """Config Object purpuse is to abstract the work with 
        The Configuration file , can only work with one specifice file at time , 
        requers , "config" child folder for work , for changes you can change CONFIG_DIR property . """

    def __str__(self):
        return f"<Config class - {self.filename}>"


class App(Config):

    def __init__(self, filename="app.xml"):
        super().__init__(filename)

    def getSamples(self):
        #   For Offline Mode and too keep things simple
        # self.x = list(range(0,20))
        # self.y = [random.randrange(1, 101, 1) for _ in range(20)]
        # self.success = True
        #   For imitate real HTTP JSON API Calls
        import json
        data = json.loads(self.JsonAPI_server_side(self.user, self.password))
        self.success = data["success"]
        self.x = data["x"]
        self.y = data["y"]

    @staticmethod
    def JsonAPI_server_side(user, password):
        import json
        if user == "root" and password == "123456":
            data = {
                "x": list(range(0, 20)),
                "y": [random.randrange(1, 101, 1) for _ in range(20)],
                "success": True
            }
            return json.dumps(data, indent=2)
        return json.dumps({"success": False, "x": [], "y": []})

    def createGraph(self):
        self.graph = self.Graph(self.x, self.y, self.color, self.title)

    class Graph:

        def __init__(self, x, y, color, title):
            plt.plot(x, y, color=color)
            plt.title(title)

        def display(self):
            plt.show()

    def __str__(self):
        return "<App class : user: {} , config: {} >".format(self.user , self.filename)

    def __repr__(self):
        return "Weclcome to App Class, for now its only Graph in the future will be more :)"
