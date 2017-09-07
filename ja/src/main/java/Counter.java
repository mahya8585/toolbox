/**
 * いろいろカウントする
 */
public class Counter {
    public static void main(String...args){
        //文字数カウント
        final String targetStr = "数えよう";
        System.out.println(countStr(targetStr));
    }

    private static Integer countStr(String target) {
        return target.length();
    }
}
