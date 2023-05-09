import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Calculator calculator = new Calculator();

        double num1, num2;
        char operator;

        try {
            System.out.print("Enter first number: ");
            num1 = input.nextDouble();

            System.out.print("Enter second number: ");
            num2 = input.nextDouble();

            System.out.println("Choose an operation (+, -, *, /): ");
            operator = input.next().charAt(0);

            double result;

            switch(operator) {
                case '+':
                    result = calculator.add(num1, num2);
                    break;
                case '-':
                    result = calculator.subtract(num1, num2);
                    break;
                case '*':
                    result = calculator.multiply(num1, num2);
                    break;
                case '/':
                    result = calculator.divide(num1, num2);
                    break;
                default:
                    throw new IllegalArgumentException("Invalid operator");
            }

            System.out.println("Result: " + result);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
