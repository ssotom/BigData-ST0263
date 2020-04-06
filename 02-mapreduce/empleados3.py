from mrjob.job import MRJob

class AvgSalary(MRJob):
    def mapper(self, _, line):
        empleado, economic_sector, _, _ = line.split(",")
        
        yield (empleado, (economic_sector, 1))
      
    def reducer(self, empleado, economic_sector):
        sum = 0
        for e, c in economic_sector:
            sum += c
        yield empleado, sum

if __name__ == '__main__':
    AvgSalary.run()