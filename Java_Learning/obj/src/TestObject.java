import java.util.Objects;

public class TestObject {
    public static void main(String[] args) {
        Employee e1 = new Employee(1001, "Sean");
        Employee e2 = new Employee(1001, "Bruce");
        System.out.println(e1.toString());
        System.out.println(e2.toString());

        System.out.println(e1.equals(e2));

    }
}

class Employee  {
    int id;
    String name;

    public Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }

    @Override
    public String toString() {
        return "ID: " + id + ", Name: " + name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Employee employee = (Employee) o;
        return id == employee.id;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
