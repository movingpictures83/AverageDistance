import PyPluMA

class AverageDistancePlugin:
    def input(self, filename):
        params = dict()
        paramfile = open(filename, 'r')
        for line in paramfile:
            line = line.strip()
            contents = line.split('\t')
            params[contents[0]] = contents[1]

        self.distmat = []
        csvfile = open(PyPluMA.prefix()+"/"+params["csvfile"], 'r')
        self.cols = csvfile.readline().strip().split(',')
        if (self.cols[0] == '\"\"'):
            self.cols = self.cols[1:]
        while (self.cols.count('') != 0):
            self.cols.remove('')

        self.rows = []
        for line in csvfile:
            line = line.strip()
            contents = line.split(',')
            self.rows.append(contents[0])
            newrow = []
            for i in range(1, len(contents)):
                newrow.append(float(contents[i]))
            self.distmat.append(newrow)

        infile = open(PyPluMA.prefix()+"/"+params["locations"], 'r')
        self.locations = []
        for line in infile:
           line = line.strip()
           contents = line.split('\t')
           self.locations.append((contents[0], contents[1]))

    def run(self):
        # Compute Average
        sum = 0.0
        for location in self.locations:
           i = self.rows.index(location[0])
           j = self.cols.index(location[1])
           #print(self.rows)
           #print(self.cols)
           #print(i)
           #print(j)
           sum += self.distmat[i][j]
           #print(self.distmat[i][j])
        self.avg = sum / len(self.locations)
        #print("AVERAGE:"+str(self.avg))

    def output(self, filename):
        outfile = open(filename, 'w')
        outfile.write("\"\",\"Value\"\n")
        outfile.write("\"Average\","+str(self.avg)+"\n")
