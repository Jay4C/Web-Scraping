import Model.Fund;
import Model.Parity;
import Model.RealTimeFutures;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.vertx.core.AbstractVerticle;
import io.vertx.core.Future;
import io.vertx.core.http.HttpServer;
import io.vertx.core.http.HttpServerResponse;
import io.vertx.ext.web.Router;
import io.vertx.ext.web.RoutingContext;
import io.vertx.ext.web.handler.BodyHandler;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Server extends AbstractVerticle
{
    ObjectMapper mapper = new ObjectMapper();

    //The httpServer starts in this method.
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    @Override
    public void start(final Future<Void> startFuture) throws Exception
    {
        HttpServer httpServer = vertx.createHttpServer();

        //Instanciate the router
        final Router router = Router.router(vertx);

        System.out.println("My Server started!");

        router.route().handler(BodyHandler.create());

        //API
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        router.get("/api/scraperInvestingForex").handler(this::scrapeDataInvestingForex);
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //API
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //router.get("/api/scraperTurfooCompetitors/:url").handler(this::scrapeDataTurfooCompetitors);
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //API
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        router.get("/api/scraperInvestingCommodities").handler(this::scrapeDataInvestingCommodities);
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        //API
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //Router to catch the API in order to get the world funds data into JSON Array of HTTP Response
        router.get("/api/scraperInvestingWorldFunds").handler(this::scrapeDataInvestingWorldFunds);
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        httpServer.requestHandler(router::accept);

        httpServer.listen(9898, res -> {
            if (res.succeeded())
            {
                startFuture.complete();
            }
            else {
                startFuture.fail(res.cause());
            }
        });
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Handler
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    private void scrapeDataInvestingForex(RoutingContext routingContext)
    {
        System.out.println("ScrapeData executed");
        HttpServerResponse response = routingContext.response();
        response.putHeader("content-type", "application/json");
        try {
            response.end(financialDataset());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Handler
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    /*private void scrapeDataTurfooCompetitors(RoutingContext routingContext)
    {
        String query = routingContext.request().query();
        String finalURL = query.substring(7,query.length()-3);
        System.out.println("scrapeDataTurfooCompetitors executed");
        HttpServerResponse response = routingContext.response();
        response.putHeader("content-type", "application/json");
        try {
            response.end(competitorDataset(finalURL));
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }*/
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Methods
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    /*private String competitorDataset(String URL) throws JsonProcessingException {


        //Display all competitors in JSON array string and pretty print
        return mapper.writerWithDefaultPrettyPrinter().writeValueAsString();
    }*/
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Methods
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    private String financialDataset() throws JsonProcessingException {
        //List of parities
        List<Parity> parityList = new ArrayList<>();

        //Extract the main HTML page
        Document doc = null;
        try {
            doc = Jsoup.connect("https://fr.investing.com/currencies/single-currency-crosses")
                    .userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36")
                    .timeout(5000)
                    .get();

        } catch (IOException e) {
            e.printStackTrace();
        }

        //Extract all rows of the parity
        Elements financialData = null;
        Element tbodyTag = null;
        Elements trTag = null;

        if (doc != null) {
            financialData = doc.getElementsByClass("crossRatesTbl");
            tbodyTag = financialData.get(0).getElementsByTag("tbody").get(0);
            trTag = tbodyTag.getElementsByTag("tr");
        }

        //Browse each parity from newAds
        if (trTag != null) {
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
        }

        //Display all parities JSON array string and pretty print
        return mapper.writerWithDefaultPrettyPrinter().writeValueAsString(parityList);
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Handler
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    private void scrapeDataInvestingCommodities(RoutingContext routingContext)
    {
        System.out.println("scrapeDataInvestingCommodities executed");
        HttpServerResponse response = routingContext.response();
        response.putHeader("content-type", "application/json");
        try {
            response.end(commoditiesDataset());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Methods
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    private String commoditiesDataset() throws JsonProcessingException {

        //List of Competitors
        List<RealTimeFutures> realTimeFuturesList = new ArrayList<>();

        //Extract the main HTML page
        Document doc = null;
        try {
            doc = Jsoup.connect("https://fr.investing.com/commodities/real-time-futures")
                    .timeout(5000)
                    .userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36")
                    .get();
        } catch (IOException e) {
            e.printStackTrace();
        }

        //Extract all commodities
        Elements commodities = null;
        if (doc != null) {
            commodities = doc.getElementById("cross_rate_1")
                    .getElementsByTag("tbody").get(0)
                    .getElementsByTag("tr");
        }

        /*
            Extract the matierePremiere text, the mois text, the dernier text, the plusHaut text, the plusBas text,
            the variation text, the variationPourcentage text, the date text, the heure text
         */
        String matierePremiere;
        String mois;
        String dernier;
        String plusHaut;
        String plusBas;
        String variation;
        String variationPourcentage;
        String date;
        String heure;

        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd");
        LocalDate localDate = LocalDate.now();

        if (commodities != null) {
            for (Element commodity : commodities)
            {
                //New instance of RealTimeFutures
                RealTimeFutures newRealTimeFutures = new RealTimeFutures();

                matierePremiere = commodity.getElementsByTag("td").get(1)
                        .getElementsByTag("a").get(0)
                        .text();

                mois = commodity.getElementsByTag("td").get(2)
                        .text();

                dernier = commodity.getElementsByTag("td").get(3)
                        .text();

                plusHaut = commodity.getElementsByTag("td").get(4)
                        .text();

                plusBas = commodity.getElementsByTag("td").get(5)
                        .text();

                variation = commodity.getElementsByTag("td").get(6)
                        .text();

                variationPourcentage = commodity.getElementsByTag("td").get(7)
                        .text();

                date = dtf.format(localDate);

                heure = commodity.getElementsByTag("td").get(8)
                        .text();

                //Set the newRealTimeFutures object
                newRealTimeFutures.setMatierePremiere(matierePremiere);
                newRealTimeFutures.setMois(mois);
                newRealTimeFutures.setDernier(dernier);
                newRealTimeFutures.setPlusHaut(plusHaut);
                newRealTimeFutures.setPlusBas(plusBas);
                newRealTimeFutures.setVariation(variation);
                newRealTimeFutures.setVariationPourcentage(variationPourcentage);
                newRealTimeFutures.setDate(date);
                newRealTimeFutures.setHeure(heure);

                //Add newRealTimeFutures object in realTimeFuturesList
                realTimeFuturesList.add(newRealTimeFutures);
            }
        }

        //Display all competitors in JSON array string and pretty print
        return mapper.writerWithDefaultPrettyPrinter().writeValueAsString(realTimeFuturesList);
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Handlers
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //Handler for giving the list of the world funds into JSON Array of HTTP Response
    private void scrapeDataInvestingWorldFunds(RoutingContext routingContext)
    {
        System.out.println("scrapeDataInvestingWorldFunds executed");

        //Take the response of the server
        HttpServerResponse response = routingContext.response();

        //Set the header of the server
        response.putHeader("content-type", "application/json");
        try {
            //Return the HTTP response
            response.end(wolrdFundsDataset());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Methods
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //This method permits to return a String Object into the "scrapeDataInvestingCommodities" handler.
    private String wolrdFundsDataset() throws JsonProcessingException {
        //List of funds
        List<Fund> fundsList = new ArrayList<>();

        //Extract the main HTML page
        Document doc = null;
        try {
            doc = Jsoup.connect("https://fr.investing.com/funds/world-funds")
                    .maxBodySize(0)
                    .timeout(15000)
                    .userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36")
                    .get();
        } catch (IOException e) {
            e.printStackTrace();
        }

        //Extract the element section id="leftColumn"
        Element section = null;
        if (doc != null) {
            section = doc.getElementById("leftColumn");
        }

        //Extract all the tables from the previous section
        Elements tables = null;
        if (section != null) {
            tables = section.getElementsByTag("table");
        }

        /*
            Extract the name text,
            the symbol text,
            the last text,
            the variationInPourcentage text,
            the totalVolume text,
            the Heures text
         */
        String name;
        String symbol;
        String last;
        String variationInPourcentage;
        String totalVolume;
        String date;
        String hours;

        //This object permits to format a Date Object in this format "yyyy-MM-dd"
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-d");

        //Instanciate the Date Object for having the date of today
        Date today = new Date();

        //Extract all tr tag from all the tables
        if (tables != null) {
            //Browse each table from the main page
            for (Element table : tables)
            {
                //Get all tr tag from each table
                Elements trs = table.getElementsByTag("tbody").get(0).getElementsByTag("tr");

                //Browse all tr tag from each table
                for (Element tr : trs)
                {
                    //Instanciate a new Fund object
                    Fund newFund = new Fund();

                    //Extract the name text from the tr tag
                    name = tr.getElementsByTag("td").get(1)
                            .getElementsByTag("a").get(0)
                            .text();

                    //Extract the symbol text from the tr tag
                    symbol = tr.getElementsByTag("td").get(2)
                            .text();

                    //Extract the last text from the tr tag
                    last = tr.getElementsByTag("td").get(3)
                            .text();

                    //Extract the variationInPourcentage text from the tr tag
                    variationInPourcentage = tr.getElementsByTag("td").get(4)
                            .text();

                    //Extract the totalVolume text from the tr tag
                    totalVolume = tr.getElementsByTag("td").get(5)
                            .text();

                    //Format the date of today in the format "yyyy-MM-dd"
                    date = dateFormat.format(today);

                    //Extract the hours text from the tr tag
                    hours = tr.getElementsByTag("td").get(6)
                            .text();

                    //Set the new instance of Fund object
                    newFund.setName(name);
                    newFund.setSymbol(symbol);
                    newFund.setLast(last);
                    newFund.setVariationInPourcentage(variationInPourcentage);
                    newFund.setTotalVolume(totalVolume);
                    newFund.setDate(date);
                    newFund.setHours(hours);

                    //Add the new instance to the fundsList
                    fundsList.add(newFund);
                }
            }
        }

        //Display all competitors in JSON array string and pretty print
        return mapper.writerWithDefaultPrettyPrinter().writeValueAsString(fundsList);
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //Stop the server.
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    @Override
    public void stop(Future stopFuture) throws Exception
    {
        System.out.println("My Server stopped!");
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
}