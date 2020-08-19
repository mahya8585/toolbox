package batik;

import org.apache.batik.transcoder.TranscoderInput;
import org.apache.batik.transcoder.TranscoderOutput;
import org.apache.batik.transcoder.image.PNGTranscoder;

import java.awt.*;
import java.io.*;
import java.util.Arrays;


/**
  本コードと同じディレクトリ内にあるSVGディレクトリへSVGが格納されたディレクトリを置くと作れる
**/
public class PngConverter {
    //TODO ちゃんといい感じにパスを取れるように変更する
   static final String basePath = new File(".").getAbsoluteFile().getParent() + "\\src\\main\\java\\batik";
   static final String svgDir = basePath + "\\svg";
   static final String pngDir = basePath + "\\png";

    /**
     * SVGディレクトリ直下にsvgファイルは置かないでねｗ
     * @param args
     */
    public static void main(String[] args) {
        //svnディレクトリ内のファイル全部処理する
        Arrays.stream(new File(svgDir).listFiles())
                .filter(f -> f.isDirectory())
                .forEach(
                        d -> {
                            String newDir = d.toString().replace("svg", "png");
                            if(new File(newDir).mkdir()){
                                System.out.println("ディレクトリ生成 : " + newDir);
                            }

                            Arrays.stream(d.listFiles())
                                    .filter(dd -> dd.isFile())
                                    .forEach(df -> converter(df.toString()));
                        }
                );
    }

    /**
     * SVG->PNG処理
     * @param filePath ファイルパス名
     */
    public static void converter(String filePath){
        // widthとheightは好きに指定してください
        final float width = 512;
        final float height = 512;

        //TODO 後でいい感じのファイルパス設定にする
        try (InputStream inputStream = new FileInputStream(filePath);
             OutputStream outputStream = new FileOutputStream(pngDir +"\\" + filePath.replace(svgDir + "\\", "").replace(".svg", ".png"));) {

            TranscoderInput input = new TranscoderInput(inputStream);
            TranscoderOutput output = new TranscoderOutput(outputStream);
            PNGTranscoder pngTranscoder = new PNGTranscoder();

            Rectangle rect = new Rectangle(0, 0, (int)width, (int)height);
            pngTranscoder.addTranscodingHint(PNGTranscoder.KEY_WIDTH, Float.valueOf(width));
            pngTranscoder.addTranscodingHint(PNGTranscoder.KEY_HEIGHT, Float.valueOf(height));

            // 変換
            pngTranscoder.transcode(input, output);

        } catch (Exception e) {
            System.out.println("★エラーファイル: " + filePath);
            e.printStackTrace();
        }  finally {
            //TODO あとでかく
        }
    }
}

