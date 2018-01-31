package tdd;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * TODO あとでJUnit5を使用して実行させる
 * 今このままJunit4で実行してもエラーになります
 */
public class FizzBuzzTest {
    FizzBuzz fizzBuzz;

    @Before
    public void serup() {
        //前準備
        fizzBuzz = new FizzBuzz();
    }

    //@Nested
    class convertメソッド {
        //@Nested
        class 数を文字列に変換する {

            @Test
            public void 数1を渡すと文字列1に変換する() throws Exception {
                //実行 検証
                assertEquals("1", fizzBuzz.convert(1));
            }

            @Test
            public void 数2を渡すと文字列2に変換する() throws Exception {
                //実行 検証
                assertEquals("2", fizzBuzz.convert(2));
            }
        }

        //@Nested
        class _3の倍数の時は数の代わりにfizzと変換する {
            @Test
            public void 数3を渡すと文字列Fizzに変換する() throws Exception {
                //実行 検証
                assertEquals("Fizz", fizzBuzz.convert(3));
            }

            @Test
            public void 数6を渡すと文字列Fizzに変換する() throws Exception {
                //実行 検証
                assertEquals("Fizz", fizzBuzz.convert(6));
            }
        }

        //@Nested
        class _5の倍数の時はbuzzと変換する {

            @Test
            public void 数5を渡すと文字列Buzzに変換する() throws Exception {
                //実行 検証
                assertEquals("Buzz", fizzBuzz.convert(5));
            }

            @Test
            public void 数10を渡すと文字列Buzzに変換する() throws Exception {
                //実行 検証
                assertEquals("Buzz", fizzBuzz.convert(10));
            }
        }
    }

}
