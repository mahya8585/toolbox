package tdd;

public class FizzBuzz {
    public String convert(int i) {
        if (i % 3 == 0) {
            return "Fizz";
        } if (i % 5 == 0) {
            return "Buzz";
        }

        return String.valueOf(i);
    }
}
