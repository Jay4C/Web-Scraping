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

import com.fasterxml.jackson.databind.ObjectMapper;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class TestCryptocurrency {
    public static void main(String args[]) throws IOException
    {
        //List of Cryptocurrencies
        List<Cryptocurrency> cryptocurrenciesList = new ArrayList<>();

        ObjectMapper mapper = new ObjectMapper();
        String arrayToJson;

        //URL
        String URL = "https://fr.investing.com/crypto/currencies";

        //Extract the main HTML page
        Document doc = Jsoup.connect(URL)
                .maxBodySize(0)
                .timeout(30000)
                .userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36")
                .get();

        //Extract the nombreDeDevise text
        String nombreDeDevise = doc.getElementsByClass("generalTopData").get(0)
                .getElementsByTag("li").get(0)
                .getElementsByTag("span").get(1)
                .getElementsByTag("a").get(0)
                .text();

        //Extract the capitalisationTotaleDuMarche text
        String capitalisationTotaleDuMarche = doc.getElementsByClass("generalTopData").get(0)
                .getElementsByTag("li").get(1)
                .getElementsByTag("span").get(1)
                .getElementsByTag("a").get(0)
                .text();

        //Extract the volumeTotal24H text
        String volumeTotal24H = doc.getElementsByClass("generalTopData").get(0)
                .getElementsByTag("li").get(2)
                .getElementsByTag("span").get(1)
                .getElementsByTag("a").get(0)
                .text();

        /*
            Extract the numero text, the nom text, the symbol text, the coursUSD text, the capitalisationBOursiere text,
            the volume24H text, the volumeTotal text, the variation24H text, the variation7Jours text
         */

        Elements cryptoCurrencies = doc.getElementById("top_crypto_tbl")
                .getElementsByTag("tbody").get(0)
                .getElementsByTag("tr");

        //Extract the numero text
        String numero;

        //Extract the nom text
        String nom;

        //Extract the symbol text
        String symbol;

        //Extract the coursUSD text
        String coursUSD;

        //Extract the capitalisationBOursiere text
        String capitalisationBOursiere;

        //Extract the volume24H text
        String volume24H;

        //Extract the volumeTotal text
        String volumeTotal;

        //Extract the variation24H text
        String variation24H;

        //Extract the variation7Jours text
        String variation7Jours;

        for (Element cryptocurrency : cryptoCurrencies)
        {
            //New instance for Cryptocurrency
            Cryptocurrency newCryptocurrency = new Cryptocurrency();

            numero = cryptocurrency.getElementsByTag("td").get(0)
                    .text();

            if (cryptocurrency.getElementsByTag("td").get(2).getElementsByTag("a").isEmpty())
            {
                nom = cryptocurrency.getElementsByTag("td").get(2)
                        .getElementsByTag("span").get(0)
                        .text();
            }
            else
                nom = cryptocurrency.getElementsByTag("td").get(2)
                        .getElementsByTag("a").get(0)
                        .text();

            symbol = cryptocurrency.getElementsByTag("td").get(3)
                    .text();

            if(cryptocurrency.getElementsByTag("td").get(4).getElementsByTag("a").isEmpty())
            {
                coursUSD = cryptocurrency.getElementsByTag("td").get(4)
                        .getElementsByTag("span").get(0)
                        .text();
            }
            else
                coursUSD = cryptocurrency.getElementsByTag("td").get(4)
                        .getElementsByTag("a").get(0)
                        .text();

            capitalisationBOursiere = cryptocurrency.getElementsByTag("td").get(5)
                    .text();

            volume24H = cryptocurrency.getElementsByTag("td").get(6)
                    .text();

            volumeTotal = cryptocurrency.getElementsByTag("td").get(7)
                    .text();

            variation24H = cryptocurrency.getElementsByTag("td").get(8)
                    .text();

            variation7Jours = cryptocurrency.getElementsByTag("td").get(9)
                    .text();

            //Set the new cryptocurrency
            newCryptocurrency.setNombreDeDevise(nombreDeDevise);
            newCryptocurrency.setCapitalisationTotaleDuMarche(capitalisationTotaleDuMarche);
            newCryptocurrency.setVolumeTotal24H(volumeTotal24H);
            newCryptocurrency.setNumero(numero);
            newCryptocurrency.setNom(nom);
            newCryptocurrency.setSymbole(symbol);
            newCryptocurrency.setCoursUSD(coursUSD);
            newCryptocurrency.setCapitalisationBoursiere(capitalisationBOursiere);
            newCryptocurrency.setVolume24H(volume24H);
            newCryptocurrency.setVolumeTotal(volumeTotal);
            newCryptocurrency.setVariation24H(variation24H);
            newCryptocurrency.setVariation7Jours(variation7Jours);

            //Add newCryptocurrency into cryptocurrenciesList
            cryptocurrenciesList.add(newCryptocurrency);
        }

        //Display all cryptocurrencies in JSON array string and pretty print
        arrayToJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(cryptocurrenciesList);
        System.out.println(arrayToJson);
    }
}