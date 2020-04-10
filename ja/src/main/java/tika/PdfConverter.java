package tika;

import org.apache.tika.exception.TikaException;
import org.apache.tika.metadata.Metadata;
import org.apache.tika.parser.ParseContext;
import org.apache.tika.parser.Parser;
import org.apache.tika.parser.pdf.PDFParser;
import org.apache.tika.sax.BodyContentHandler;
import org.xml.sax.ContentHandler;
import org.xml.sax.SAXException;

import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URI;
import java.net.URLConnection;
import java.util.Arrays;

public class PdfConverter {
    private static String targetUrl = "https://www.maff.go.jp/j/supply/nyusatu/zuii/rakusatu/attach/pdf/index-33.pdf";

    /**
     * PDFからテキスト抽出
     * @param args
     * @throws IOException
     */
    public static void main(String... args) throws IOException {
        URLConnection connection = URI.create(targetUrl).toURL().openConnection();

        //pdfからテキスト抽出
        ContentHandler contentHandler = new BodyContentHandler();
        Metadata metadata = new Metadata();
        Parser parser = new PDFParser();
        ParseContext parseContext = new ParseContext();

        try (InputStream inputStream = new BufferedInputStream(connection.getInputStream())) {
            parser.parse(inputStream, contentHandler, metadata, parseContext);

        } catch (TikaException e) {
            System.out.println("parser error");
        } catch (SAXException e) {
            System.out.println("parser error");
        }

        final String fullContents = contentHandler.toString();

        //調達結果抽出
        String[] lines = fullContents.split("\n");
        Arrays.stream(lines).findAny();


//        Pattern pattern = Pattern.compile("[①②③④⑤⑥⑦⑧⑨⑩]");
//        Matcher matcher = pattern.matcher(fullContents);
//        while(matcher.find()){
//            System.out.println(matcher.group());
//        }

    }
}
