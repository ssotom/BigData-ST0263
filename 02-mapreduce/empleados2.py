from mrjob.job import MRJob

class AvgSalary(MRJob):
    def mapper(self, _, line):
        empleado, _, salary, _ = line.split(",")
        
        yield (empleado, (int(salary), 1))
      
    def reducer(self, empleado, salaries):
        sum = 0
        cont = 0
        for s, c in salaries:
            sum += s
            cont += c
        
        yield (empleado, sum / cont)

if __name__ == '__main__':
    AvgSalary.run()