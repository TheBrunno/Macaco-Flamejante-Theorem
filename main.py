class MacacoFlamejanteProve:
  def __init__(self, equation):
    self.equation = equation
    self.needReverse = False

    self.goThroughString()

    self.first = self._factorAndSum(int(self.a))

    aux = 0
    if self.needReverse:
      aux = 1
    
    self.second = self._factorAndSum(int(self.rev[aux]))

    self.first, self.second = self.mmc(self.first, self.second)

    prr = '-1 . ' if aux == 1 else ''
    print(f'{prr}{self.second}/{self.first}')


  def _factorAndSum(self, value):
    div = sumDiv = 0
    originalValue = value
    needChange = True

    while True:
      if value == 1:
        break
      if needChange:
        for c in range(2, value+1):
          if value % c == 0:
            div = c
            needChange = False
            break
      
      while value > 1:
        if div != 0:
          value = value / div
          sumDiv += div
          if value % div != 0:
            needChange = True
            break
        else:
          return sumDiv
    
    return sumDiv
  
  def goThroughString(self):
    self.a = self.equation.split('**', 1)[0]
    self.members = self.equation.split('=', 1)
    self.rev = self.members[1].split('/', 1)
    if int(self.rev[0]) < int(self.rev[1]):
      self.needReverse = True

  def mmc(self, first, second):
    bigger = smaller = 0
    mm = True
    firstIsBigger = False
    if int(first) > int(second):
      bigger = int(first)
      smaller = int(second)
      firstIsBigger = True
    else:
      bigger = int(second)
      smaller = int(first)

    while True:
      if mm:
        mm = False
        for c in range(smaller, 1, -1):
          if smaller % c == 0 and bigger % c == 0:
            smaller = int(smaller / c)
            bigger = int(bigger / c)
            mm = True
        if not mm:
          break
    
    if firstIsBigger:
      return bigger, smaller
    else:
      return smaller, bigger



if __name__ == "__main__":
  MacacoFlamejanteProve('32**x=2/1')