BRANCH = "branch"
EXIT = "exit"

class CoverageData:

    '''
    Constructor of the data structure
    :param nb: number of branches
    '''
    def __init__(self, nb):
        if nb <= 0:
            raise ValueError("The number of branches has to be > 0")
        self.access_sequence = []
        self.data = {}
        self.number_of_branches = nb

    '''
    This method logs a given branch
    :param type: the type of the branch, BRANCH or EXIT
    :param id: the id of the branch
    '''
    def log_branch(self, type, id):
        if id > self.number_of_branches:
            raise IndexError("The given id is bigger than the number of branches")
        if type != BRANCH and type != EXIT:
            raise NameError("The given type is invalid")
        # add the branch to the sequence
        self.access_sequence.append(id)
        # update the total number of accesses for this branch
        if not id in self.data:
            self.data[id] = {"type": type, "total": 1}
        else:
            self.data[id]["total"] = self.data[id]["total"] + 1

    '''
    This method prints the results in the terminal
    '''
    def print_results(self):
        print("--------------------------------------------------")
        print("ACCESS SEQUENCE")
        print("--------------------------------------------------\n")
        for id in self.access_sequence:
            if self.data[id]["type"] == BRANCH:
                print(str(id) + " -> ", end="")
            else:
                print("exit " + str(id) + "\n")
        print("--------------------------------------------------")
        print("TOTAL ACCESSES")
        print("--------------------------------------------------\n")      
        for id in range(1, self.number_of_branches + 1):
            if id in self.data:
                if self.data[id]["type"] == BRANCH:
                    print(BRANCH + "\t" + str(id) + ":\t" + str(self.data[id]["total"]) + "\taccesses")
                else:
                    print(EXIT + "\t" + str(id) + ":\t" + str(self.data[id]["total"]) + "\taccesses")
            else:
                print("?\t" + str(id) + ":\t0\taccesses")

    '''
    Getter for the access sequence
    :return: the access sequence
    '''
    def get_access_sequence(self):
        return self.access_sequence

    '''
    Getter for the data
    :return: the data
    '''
    def get_data(self):
        return self.data
