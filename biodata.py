class process_the_file():
    def __init__(self, file_name):
        self.file_name = file_name

    def process(self):
        file_discriptor = open(self.file_name, "r+")
        return file_discriptor.read()

    def biodata(self):
        data = self.process()
        for line in data.split("\n"):
            if line is not "":
                client_data = line.split("|")
                #print client_data
                first_name = client_data[0]
                last_name = client_data[1]
                address = client_data[2]
                city = client_data[3]
                state = client_data[4]
                print "first_name = " +  first_name
                print "last_name = " + last_name
                print "address = " + address
                print "city = " + city
                print "state = " + state + ("\n")

processed = process_the_file("/Users/harvindersingh/python/biodata.py")
processed.process()
processed.biodata()

