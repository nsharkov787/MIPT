class Vector:

    def __init__(self, t):
        self.x, self.y, self.z = list(map(float, t.split())) 
    def __add__(self, new):
        x1 = self.x + new.x
        y1 = self.y + new.y
        z1 = self.z + new.z
        return Vector(str(f"{x1} {y1} {z1}"))
    def __radd__(self, n):
        x1 = self.x + n
        y1 = self.y + n
        z1 = self.z + n
        return Vector(str(f"{x1} {y1} {z1}"))
    def __sub__(self, new):
        x1 = self.x - new.x
        y1 = self.y - new.y
        z1 = self.z - new.z
        return Vector(str(f"{x1} {y1} {z1}"))
    def __mul__(self, new) :
        x1 = self.y * new.z - self.z * new.y
        y1 = -1*(self.x * new.z - self.z * new.x)
        z1 = self.x * new.y - self.y * new.x
        return Vector(str(f"{x1} {y1} {z1}"))
    def __abs__(self):
        return(self.x**2 + self.y**2 + self.z**2)**0.5
    def outt(self):
        return [self.x,self.y,self.z]
    def __str__(self):
        return (f"coords are: x - {self.x}, y - {self.y}, z - {self.z}.")
    def centre(array):
        xc = Vector("0 0 0")
        for x in array:
            xc = xc + x
        xc = xc/len(array)
        return xc
    def __truediv__(self, n):
        x1 = self.x / n
        y1 = self.y / n
        z1 = self.z / n
        return Vector(str(f"{x1} {y1} {z1}"))
    def searchS(array):
        n = len(array)
        if len(array)>=3 :
            areas = []

            for i in range(n):
               for j in range(i + 1, n):
                  for k in range(j + 1, n):
                        area = abs((array[i]-array[j])*(array[k]-array[j]))/2
                        areas += [area]
            return max(areas)
        else : 
            print('нет треугольникв')
            return 0
    
def inputtvec():
    n = int(input('сколько векторов ? '))
    vectors = []
    for x in range(n):
        t = str(input(f"введите координаты {x+1} вектора : "))
        vectors += [Vector(t)]
    return vectors

vectors = inputtvec()
print(f"у центра масс {Vector.centre(vectors)}")
print(f"максимальная площадь = {Vector.searchS(vectors)}")

