from mrjob.job import MRJob

class AvgSalary(MRJob):
    def mapper(self, _, line):
        _, economic_sector, salary, _ = line.split(",")
        
        yield (economic_sector, (int(salary), 1))
      
    def reducer(self, economic_sector, salaries):
        sum = 0
        cont = 0
        for s, c in salaries:
            sum += s
            cont += c
        
        yield (economic_sector, sum / cont)

if __name__ == '__main__':
    AvgSalary.run()