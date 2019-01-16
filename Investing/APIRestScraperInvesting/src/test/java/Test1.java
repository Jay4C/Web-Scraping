import com.fasterxml.jackson.databind.ObjectMapper;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Test1
{
    public static void main(String args[]) throws IOException
    {
        //List of Parities
        List<Parity> parityList = new ArrayList<>();

        ObjectMapper mapper = new ObjectMapper();
        String arrayToJson = "";

        //URL
        String URL = "https://fr.investing.com/currencies/single-currency-crosses";

        //Extract the main HTML page
        Document doc = Jsoup.connect(URL).userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36").timeout(25000).get();

        //Extract all rows of the parity
        Elements financialData = doc.getElementsByClass("crossRatesTbl");
        Element tbodyTag = financialData.get(0).getElementsByTag("tbody").get(0);
        Elements trTag = tbodyTag.getElementsByTag("tr");

        //Browse each parity from newAds
        for (Element currency : trTag)
        {
            //New instance of Parity object
            Parity newParity = new Parity();

            //Get datum for parity, bid, ask, h, l, pc, pcp, date
            newParity.setParity(currency.getElementsByTag("td").get(1).getElementsByTag("a").text());
            newParity.setBid(currency.getElementsByTag("td").get(2).text());
            newParity.setAsk(currency.getElementsByTag("td").get(3).text());
            newParity.setH(currency.getElementsByTag("td").get(4).text());
            newParity.setL(currency.getElementsByTag("td").get(5).text());
            newParity.setPc(currency.getElementsByTag("td").get(6).text());
            newParity.setPcp(currency.getElementsByTag("td").get(7).text());
            newParity.setHeure(currency.getElementsByTag("td").get(8).text());

            //Add a parity in parityList
            parityList.add(newParity);
        }

        //Display all parities JSON array string and pretty print
        arrayToJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(parityList);
        System.out.println(arrayToJson);
    }
}