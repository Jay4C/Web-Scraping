package Service;

import Model.TEData;
import Model.Wages;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ExtractData {

    //Model number 1 for extracting data
    //This method permit to extract all data from the main HTML page from URL
    public static String ExtractDataModel1(String URL)
    {
        //This is the result of the extraction of data
        String result = null;

        //List of Statistics for each horse
        List<TEData> tEDataList = new ArrayList<>();

        //It permits to map the Java object into JSON object
        ObjectMapper mapper = new ObjectMapper();

        String country;
        String last;
        String monthYear;
        String previous;
        String highest;
        String lowest;
        String unit;
        String period;

        //Extract the main HTML page for the table of competitors
        Document doc = null;
        try {
            doc = Jsoup.connect(URL)
                    .maxBodySize(0)
                    .userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36")
                    .timeout(10000)
                    .get();
        } catch (IOException e) {
            e.printStackTrace();
        }

        //Extract the table of data
        Element tableOfData = null;
        if (doc != null) {
            tableOfData = doc.getElementsByClass("table-hover").get(0);
        }

        //Extract all tr tag from the table of data
        Elements trTag = null;
        if (tableOfData != null) {
            trTag = tableOfData.getElementsByTag("tbody").get(0).getElementsByTag("tr");
        }

        //Extract each tr from trTag Elements
        if (trTag != null) {
            for (Element tr : trTag)
            {
                //New instance of TEData
                TEData newTEData = new TEData();

                country = tr.getElementsByTag("td").get(0).getElementsByTag("a").get(0).text();
                last = tr.getElementsByTag("td").get(1).text();
                monthYear = tr.getElementsByTag("td").get(2).getElementsByTag("span").get(0).text();
                previous = tr.getElementsByTag("td").get(3).text();
                highest = tr.getElementsByTag("td").get(4).text();
                lowest = tr.getElementsByTag("td").get(5).text();
                unit = tr.getElementsByTag("td").get(6).text();
                period = tr.getElementsByTag("td").get(7).getElementsByTag("small").get(0).text();

                newTEData.setCountry(country);
                newTEData.setLast(last);
                newTEData.setMonthYear(monthYear);
                newTEData.setPrevious(previous);
                newTEData.setHighest(highest);
                newTEData.setLowest(lowest);
                newTEData.setUnit(unit);
                newTEData.setPeriod(period);

                //Add the new wage in the list
                tEDataList.add(newTEData);
            }
        }

        //Display a Java object in JSON string and pretty print

        try {
            result = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(tEDataList);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        return result;
    }

    public static String minimumWagesDataset() throws JsonProcessingException {
        //List of Statistics for each horse
        List<Wages> wagesList = new ArrayList<>();

        String country;
        String last;
        String monthYear;
        String previous;
        String highest;
        String lowest;
        String currencyPeriod;
        String changePeriod;

        //Extract the main HTML page for the table of competitors.
        Document doc = null;
        try {
            doc = Jsoup.connect("https://tradingeconomics.com/country-list/minimum-wages")
                    .userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36")
                    .get();
        } catch (IOException e) {
            e.printStackTrace();
        }

        //Extract the table of data
        Element tableOfData = null;
        if (doc != null) {
            tableOfData = doc.getElementsByClass("table-hover").get(0);
        }

        //Extract all tr tag fro the table of data
        Elements trTag = null;
        if (tableOfData != null) {
            trTag = tableOfData.getElementsByTag("tbody").get(0).getElementsByTag("tr");
        }

        //Extract each tr fron trTag Elements
        if (trTag != null) {
            for (Element tr : trTag)
            {
                //New instance of mnimum wages
                Wages newWage = new Wages();

                country = tr.getElementsByTag("td").get(0).getElementsByTag("a").get(0).text();
                last = tr.getElementsByTag("td").get(1).text();
                monthYear = tr.getElementsByTag("td").get(2).getElementsByTag("span").get(0).text();
                previous = tr.getElementsByTag("td").get(3).text();
                highest = tr.getElementsByTag("td").get(4).text();
                lowest = tr.getElementsByTag("td").get(5).text();
                currencyPeriod = tr.getElementsByTag("td").get(6).getElementsByTag("small").get(0).text();
                changePeriod = tr.getElementsByTag("td").get(7).getElementsByTag("small").get(0).text();

                newWage.setCountry(country);
                newWage.setLast(last);
                newWage.setMonthYear(monthYear);
                newWage.setPrevious(previous);
                newWage.setHighest(highest);
                newWage.setLowest(lowest);
                newWage.setCurrencyPeriod(currencyPeriod);
                newWage.setChangePeriod(changePeriod);

                //Add the new wage in the list
                wagesList.add(newWage);
            }
        }

        //Display newStatistique in JSON object string and pretty print
        ObjectMapper mapper = new ObjectMapper();
        return mapper.writerWithDefaultPrettyPrinter().writeValueAsString(wagesList);
    }
}
