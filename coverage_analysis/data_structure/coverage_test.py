from .coverage_data_structure import CoverageData

class Coverage_test:

    def __init__(self, nb_run, function, inputs, nb_branches):
        if nb_run <= 0:
            raise ValueError("The number of run has to be > 0")
        self.nb_run = nb_run
        if nb_run != len(inputs):
            raise ValueError("The number of inputs does not match the number of run")
        self.function = function
        self.inputs = inputs
        if nb_branches <= 0:
            raise ValueError("The number of branches has to be > 0")
        self.nb_branches = nb_branches
        self.data_results = []
        self.accesses_sum = [0] * self.nb_branches

    def run(self):
        for i in range(self.nb_run):
            coverage = CoverageData(self.nb_branches)
            self.function(self.inputs[i], coverage)
            data = coverage.get_data()
            self.data_results.append(data)
            for id in data:
                self.accesses_sum[id - 1] = self.accesses_sum[id - 1] + data[id]["total"]
    
    def print_results(self):
        print("TOTAL ACCESSES")
        print("\t\t", end="")
        # print headers
        for i in range(self.nb_run):
            print("run " + str(i + 1), end="\t") 
        print("mean")
        for id in range(1, self.nb_branches + 1):
            i = 0
            # print the type of the branch
            type = ""
            while i < self.nb_run and type == "":
                if id in self.data_results[i]:
                    type = self.data_results[i][id]["type"]
                i = i + 1
            if type == "":
                print("?\t" + str(id) + ":\t", end="")
            else:
                print(type + "\t" + str(id) + ":\t", end="")
            # print results
            for i in range(self.nb_run):     
                if id in self.data_results[i]:
                    print(str(self.data_results[i][id]["total"]), end="\t")
                else:
                    print("0", end="\t")
            # print mean accesses
            print(self.accesses_sum[id - 1] / self.nb_run)
            
