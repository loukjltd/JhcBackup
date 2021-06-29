public class Person {
    String personName;
    int personAge;

    public void show() {
        System.out.println("Hi! My name is " + personName + " and I am " + personAge + " years old.");
    }

    Person() {

    }

    Person(String _personName, int _personAge) {
        personName = _personName;
        personAge = _personAge;
    }

    public static void main(String[] args) {
        Person p1 = new Person();
        Person p2 = new Person("Sean", 21);

        p1.show();
        p2.show();
    }
}
