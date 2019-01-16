/*
Copyright Jason ALOYAU was born on November 11th, 1993 in Saint-Louis (France)
Date of creation of this software : March 31st, 2018

E-mail of Jason ALOYAU : jason.aloyau@outlook.fr

This software is a computer program whose purpose is to extract data concerning the world funds published on the website :
https://fr.investing.com/funds/world-funds

The world funds data are represented by :
- Name
- Symbol
- Last
- Variation in pourcentage
- Total volume
- Hours

This software is governed by the CeCILL-B license under French law and
abiding by the rules of distribution of free software.  You can  use,
modify and/ or redistribute the software under the terms of the CeCILL-B
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info".

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability.

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or
data to be ensured and,  more generally, to use and operate it in the
same conditions as regards security.

The fact that you are presently reading this means that you have had
knowledge of the CeCILL-B license and that you accept its terms.
 */

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
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Server extends AbstractVerticle
{
    //Instanciate an ObjectMapper to map the "Fund" Java Object
    private ObjectMapper mapper = new ObjectMapper();

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
        //Router to catch the API in order to get the world funds data into JSON Array of HTTP Response
        router.get("/api/scraperInvestingWorldFunds").handler(this::scrapeDataInvestingCommodities);
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        httpServer.requestHandler(router::accept);

        //The server listens on the port 9898.
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

    //Handlers
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //Handler for giving the list of the world funds into JSON Array of HTTP Response
    private void scrapeDataInvestingCommodities(RoutingContext routingContext)
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