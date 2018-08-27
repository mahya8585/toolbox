public class StringCreator {
    public static void main(String[] args) {
        System.out.println(createPropertyFileName());
    }

    private static String createPropertyFileName() {
        String PROPERTY_FILE = "atve.portal.properties";
        String propertyNameSuffix = "staging";
        final String regex = "\\.";
        String[] baseName = "atve.portal.properties".split(regex);

        String propertyName = "";
        for(int cnt=0; cnt <= baseName.length - 1; cnt++) {
            //最後の文字列(ファイル拡張子相当）の前に実行環境名を追加する
            if(cnt == baseName.length - 1) {
                propertyName = propertyName + "-" + propertyNameSuffix;
            }

            if (cnt == 0) {
                propertyName = baseName[cnt];
            } else {
                propertyName = propertyName + regex.replace("\\", "") + baseName[cnt];
            }
        }


        return propertyName;
    }
}
