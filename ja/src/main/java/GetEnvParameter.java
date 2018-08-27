public class GetEnvParameter {
    public static void main(String...args){
        String env = System.getenv("JAVA_HOME");

        System.out.println(env);
    }
}
