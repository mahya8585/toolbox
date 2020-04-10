import java.util.Base64;

/**
 * Base64&#x306e;&#x30a8;&#x30f3;&#x30b3;&#x30fc;&#x30c9;&#x30fb;&#x30c7;&#x30b3;&#x30fc;&#x30c9;
 */
class Base64Converter {
    public static void main(String... args) {
        //エンコード
        final String words = "よーしBase64にするぞ";
        System.out.println(words + "  :  " + encodeWords(words));

        //デコード
        final String encryptedWords = "44KI44O844GXQmFzZTY044Gr44GZ44KL44Ge";
        System.out.println(encryptedWords + "  :  " + decodeWords(encryptedWords));
    }

    /**
     * Base64でエンコードする
     *
     * @param targetWords エンコードさせたい文字列
     * @return エンコード済み文字列
     */
    static private String encodeWords(String targetWords) {
        return Base64.getEncoder().encodeToString(targetWords.getBytes());
    }

    /**
     * Base64の文字列をデコードする
     *
     * @param targetWords デコードしたい文字列
     * @return デコード済み文字列
     */
    static private String decodeWords(String targetWords) {
        return new String(Base64.getDecoder().decode(targetWords));
    }
}
