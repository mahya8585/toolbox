package tika;

import org.apache.tika.metadata.Metadata;
import org.apache.tika.parser.ParseContext;
import org.apache.tika.parser.Parser;
import org.apache.tika.parser.pdf.PDFParser;
import org.apache.tika.sax.BodyContentHandler;
import org.xml.sax.ContentHandler;

import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URI;
import java.net.URLConnection;

public class PdfConvertor {
    private static String targetUrl = "https://www.maff.go.jp/j/supply/nyusatu/zuii/rakusatu/attach/pdf/index-33.pdf";

    /**
     * PDF to text‚ÌƒeƒXƒg
     */
    public static void main(String... args) throws IOException {
        URLConnection conn = URI.create("http://dynabook.com/pc/catalog/dynabook/manupdf/gx1c00177210.pdf").toURL().openConnection();
        try (InputStream is = new BufferedInputStream(conn.getInputStream())) {
            Parser parser = new PDFParser();
            ContentHandler contentHandler = new BodyContentHandler();
            Metadata metadata = new Metadata();
            ParseContext context = new ParseContext();

        }

    }
}
