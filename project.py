class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
    def display(self):
        print("Circle with radius:", self.radius)
        print("Area:", self.area())
        print("perimeter:", self.perimeter())
def main():
    radius = float(input("Enter the radius of the circle: "))
    c = circle(radius)
    c.display()
if __name__ == "__main__":
    main()