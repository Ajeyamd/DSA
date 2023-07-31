// Shape is the parent class that defines a common interface for all shapes.
abstract class Shape {
    abstract public function getArea();
}

// Rectangle is a subclass of Shape.
class Rectangle extends Shape {
    private $width;
    private $height;

    public function __construct($width, $height) {
        $this->width = $width;
        $this->height = $height;
    }

    public function getArea() {
        return $this->width * $this->height;
    }
}

// Circle is another subclass of Shape.
class Circle extends Shape {
    private $radius;

    public function __construct($radius) {
        $this->radius = $radius;
    }

    public function getArea() {
        return M_PI * pow($this->radius, 2);
    }
}

// Function that uses the common interface to calculate the area of a shape.
function calculateShapeArea(Shape $shape) {
    return $shape->getArea();
}

// Usage of the classes and polymorphism.
$rectangle = new Rectangle(4, 6);
$circle = new Circle(3);

echo "Area of Rectangle: " . calculateShapeArea($rectangle) . "\n";
echo "Area of Circle: " . calculateShapeArea($circle) . "\n";
