import Model.Parity;
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

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
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

    //Stop the server.
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    @Override
    public void stop(Future stopFuture) throws Exception
    {
        System.out.println("My Server stopped!");
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
}