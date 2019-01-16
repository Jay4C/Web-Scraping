/*
Copyright ou © ou Copr. Entreprise ALOYAU - SIRET : 823 503 222 00015, le 09 Mars 2018

Adresse électronique : jason.aloyau@outlook.fr

Ce logiciel est un programme informatique servant à extraire des données concernant les crypto-monnaies sur le site :
https://fr.investing.com/crypto/currencies

Les données récupérées sont :
- Nombre de devises
- Capitalisation totale du marché
- Volume total du marché (24H)
- Numéro
- Nom
- Symbole
- Cours(USD)
- Capitalisation boursière
- Volume de la crypto-monnaie (24h)
- Volume total de la crypto-monnaie
- Variation(24h)
- Variation (7 jours)

Ce logiciel est régi par la licence CeCILL-B soumise au droit français et
respectant les principes de diffusion des logiciels libres. Vous pouvez
utiliser, modifier et/ou redistribuer ce programme sous les conditions
de la licence CeCILL-B telle que diffusée par le CEA, le CNRS et l'INRIA
sur le site "http://www.cecill.info".

En contrepartie de l'accessibilité au code source et des droits de copie,
de modification et de redistribution accordés par cette licence, il n'est
offert aux utilisateurs qu'une garantie limitée.  Pour les mêmes raisons,
seule une responsabilité restreinte pèse sur l'auteur du programme,  le
titulaire des droits patrimoniaux et les concédants successifs.

A cet égard  l'attention de l'utilisateur est attirée sur les risques
associés au chargement,  à l'utilisation,  à la modification et/ou au
développement et à la reproduction du logiciel par l'utilisateur étant
donné sa spécificité de logiciel libre, qui peut le rendre complexe à
manipuler et qui le réserve donc à des développeurs et des professionnels
avertis possédant  des  connaissances  informatiques approfondies.  Les
utilisateurs sont donc invités à charger  et  tester  l'adéquation  du
logiciel à leurs besoins dans des conditions permettant d'assurer la
sécurité de leurs systèmes et ou de leurs données et, plus généralement,
à l'utiliser et l'exploiter dans les mêmes conditions de sécurité.

Le fait que vous puissiez accéder à cet en-tête signifie que vous avez
pris connaissance de la licence CeCILL-B, et que vous en avez accepté les
termes.
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
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class Server extends AbstractVerticle
{
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
        router.get("/api/scraperInvestingCommodities").handler(this::scrapeDataInvestingCommodities);
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

    //Stop the server.
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    @Override
    public void stop(Future stopFuture) throws Exception
    {
        System.out.println("My Server stopped!");
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
}