import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class DateFormatDev {
    public static void main(String...args){
        DateTimeFormatter format = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDate localDate = LocalDate.parse("1999-01-01T12:00:00".substring(0,10), format);
        System.out.println(localDate.toString());
    }
}
