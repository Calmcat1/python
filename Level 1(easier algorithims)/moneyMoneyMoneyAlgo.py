def calculate_years(principle,interest,tax,desired):
      year = 0
      displayArr = []
      while principle < desired:
            grossinterest = principle * interest 
            netinterest = grossinterest - grossinterest*tax
            year += 1
            principle += netinterest
            displayArr.append(principle)
      return year,displayArr
  

print(calculate_years(1000,0.01625,0.18,1200))