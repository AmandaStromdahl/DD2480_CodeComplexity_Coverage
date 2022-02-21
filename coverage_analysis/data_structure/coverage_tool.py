from .coverage_data_structure import CoverageData

class Coverage_tool:

    '''
    Constructor of the tool
    :param nb_run: number of times the function will be run
    :param function: the function to test
    :param inputs: specific inputs for all the runs
    :param nb_branches: total number of branches in the given function
    '''
    def __init__(self, tests, nb_branches):
        self.nb_test = len(tests)
        self.tests = tests
        if nb_branches <= 0:
            raise ValueError("The number of branches has to be > 0")
        self.nb_branches = nb_branches
        self.data_results = []
        self.accesses_sum = [0] * self.nb_branches

    '''
    This method runs the coverage tool, i.e it will execute the function for the given
    number of runs with their specific inputs
    '''
    def run(self):
        for i in range(self.nb_test):
            coverage = CoverageData(self.nb_branches)
            # execute the test
            self.tests[i](coverage)
            # retrieve the result
            data = coverage.get_data()
            self.data_results.append(data)
            # add results in accesses_sum in order to compute an average at the end
            for id in data:
                self.accesses_sum[id - 1] = self.accesses_sum[id - 1] + data[id]["total"]
    
    '''
    This method prints the results in the terminal
    '''
    def print_results(self):
        # make sure that we ran the tool
        if self.data_results == []:
            print("You need to run the tool before!")
            return
        # used to compute the branch coverage percentage
        nb_unreached_branches = 0
        # print headers
        print("TOTAL ACCESSES")
        print("\t\t", end="")
        for test in self.tests:
            print(test.__name__, end="\t") 
        print("mean")
        # iterate on the branches
        for id in range(1, self.nb_branches + 1):
            i = 0
            type = ""
            # this loop is needed since a specific branch might not be present in one or many branch
            while i < self.nb_test and type == "":
                if id in self.data_results[i]:
                    type = self.data_results[i][id]["type"]
                i = i + 1
            # print the type of the branch
            if type == "":
                print("?\t" + str(id) + ":\t", end="")
            else:
                print(type + "\t" + str(id) + ":\t", end="")
            # print results
            for i in range(self.nb_test):     
                if id in self.data_results[i]:
                    print(str(self.data_results[i][id]["total"]), end="\t\t\t")
                else:
                    print("0", end="\t\t\t")
            # print mean accesses
            print(self.accesses_sum[id - 1] / self.nb_test)
            if self.accesses_sum[id - 1] == 0:
                nb_unreached_branches = nb_unreached_branches + 1
        # print percentage coverage
        perc = 1 - (nb_unreached_branches / self.nb_branches)
        print("\nBranch coverage: %0.2f" % (perc * 100), end="")
        print("%")
            
