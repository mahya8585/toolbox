import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

/**
 * HMAC_SHA256のエンコードツール
 */
public class HmacSha256Encoder {
    public static void main(String... args) {
        final String target = "ぴよぴよ";
        final String secretKey = "test";

        System.out.println(convertHmacSha256(target, secretKey));
    }

    /**
     * HMAC-SHA256で暗号化する
     * algorithm変数を書き換えればほかのアルゴリズムにも使用できます
     * @param target 暗号化したい文字列
     * @param secretKey 暗号キー
     * @return 暗号化済み文字列
     */
    static private String convertHmacSha256(String target, String secretKey) {
        final String algorithm = "HmacSHA256";

        SecretKeySpec sk = new SecretKeySpec(secretKey.getBytes(), algorithm);
        try {

            Mac mac = Mac.getInstance(algorithm);
            mac.init(sk);

            byte[] mac_bytes = mac.doFinal(target.getBytes());

            StringBuilder sb = new StringBuilder(2 * mac_bytes.length);
            for (byte b : mac_bytes) {
                sb.append(String.format("%02x", b & 0xff));
            }

            return sb.toString();
        } catch (InvalidKeyException e) {
            e.printStackTrace();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }

        return "";
    }
}
