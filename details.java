
class Employee{
    int salary;
    String name;
    public  int getSalary(){
        return salary;
    }
    public String getName(){
        return name;
    }
    public void setName(String n)
    {
        name=n;
    }
}

public class details
{
    public static void main(String [] args)
    {
        Employee obj = new Employee();
        obj.setName("KAJAL");
        System.out.println(obj.getName());
    }
}