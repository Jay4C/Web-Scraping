import Model.Contact;
import jxl.Workbook;
import jxl.write.Label;
import jxl.write.WritableSheet;
import jxl.write.WritableWorkbook;
import jxl.write.WriteException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.File;
import java.io.IOException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Test1 {
    public static void main(String args[]) throws IOException
    {
        DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd_HH-mm-ss");
        Date date = new Date();

        final String EXCEL_FILE_LOCATION = "C:\\Users\\HP\\Downloads\\ContactsCustormers_" + dateFormat.format(date) + ".xls";

        //List of Contacts
        List<Contact> contactList = new ArrayList<Contact>();

        //Extract the main HTML page
        Document doc = null;
        try {
            String URL = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=editeur%20de%20logiciel&ou=Paris%208%C3%A8me%20arrondissement%20%20%2875008%29&idOu=A0750560008&page=15&contexte=nVvT8YGsiiO0twhXhj%2BTEA%3D%3D&proximite=0&quoiQuiInterprete=editeur%20de%20logiciel";
            doc = Jsoup.connect(URL)
                    .maxBodySize(0)
                    .timeout(15000)
                    .userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36")
                    .get();
        } catch (IOException e) {
            e.printStackTrace();
        }

        //Extract the tag "section" with the class "results"
        Element sectionResults = null;
        if (doc != null) {
            sectionResults = doc.getElementsByClass("results").get(0);
        }

        //Extract all the tag "article"
        Elements tagArticle = null;
        if (sectionResults != null) {
            tagArticle = sectionResults.getElementsByClass("bi-bloc");
        }

        //Extract the "name" text
        String companyName = null;

        //Extract the "telephone" text
        String companyTelephone = null;

        //Extract the "address" text
        String companyAddress = null;

        //Extract the "activity" text
        String companyActivity = null;

        if (tagArticle != null) {
            for(Element article : tagArticle)
            {
                companyName = article.getElementsByClass("zone-bi").get(0)
                        .getElementsByClass("v-card").get(0)
                        .getElementsByClass("row-denom").get(0)
                        .getElementsByClass("denomination").get(0)
                        .getElementsByClass("company-name").get(0)
                        .getElementsByClass("denomination-links").get(0).text();

                companyAddress = article.getElementsByClass("zone-bi").get(0)
                        .getElementsByClass("v-card").get(0)
                        .getElementsByClass("main-adresse-container").get(0)
                        .getElementsByClass("adresse-container").get(0)
                        .getElementsByClass("adresse").get(0).text();

                companyActivity = article.getElementsByClass("zone-bi").get(0)
                        .getElementsByClass("description").get(0)
                        .getElementsByClass("activites-mentions").get(0)
                        .getElementsByClass("activites").get(0).text();

                companyTelephone = article.getElementsByClass("zone-bi").get(0)
                        .getElementsByClass("bi-contact").get(0)
                        .getElementsByClass("bi-contact-numbers").get(0)
                        .getElementsByClass("item").get(0)
                        .getElementsByClass("tel-zone").get(0)
                        .getElementsByClass("num").get(0)
                        .text();

                Contact newContact = new Contact();

                newContact.setCompanyName(companyName);
                newContact.setConpanyAddress(companyAddress);
                newContact.setCompanyTelephone(companyTelephone);
                newContact.setCompanyActivity(companyActivity);

                contactList.add(newContact);
            }
        }

        //Create a Excel file
        WritableWorkbook myFirstWbook = null;
        try {
            myFirstWbook = Workbook.createWorkbook(new File(EXCEL_FILE_LOCATION));

            // create an Excel sheet
            WritableSheet excelSheet = myFirstWbook.createSheet("companies", 0);

            //Add something into the Excel sheet

            //Add the label "companyName"
            Label label = new Label(0, 0, "companyName");
            try {
                excelSheet.addCell(label);

            } catch (WriteException e) {
                e.printStackTrace();
            }

            //Add the label "companyAddress"
            label = new Label(1, 0, "companyAddress");
            excelSheet.addCell(label);

            //Add the label "companyTelephone"
            label = new Label(2, 0, "companyTelephone");
            excelSheet.addCell(label);

            //Add the label "companyActivity"
            label = new Label(3, 0, "companyActivity");
            excelSheet.addCell(label);

            //Add the label "companyEmail"
            label = new Label(4, 0, "companyEmail");
            excelSheet.addCell(label);

            //Add all the records into the sheet
            for (int i = 0; i<contactList.size(); i++)
            {
                Label companyNameContent = new Label(0,i+1,contactList.get(i).getCompanyName());
                Label companyAddressContent = new Label(1,i+1,contactList.get(i).getConpanyAddress());
                Label companyTelephoneContent = new Label(2, i+1, contactList.get(i).getCompanyTelephone());
                Label companyActivityContent = new Label(3, i+1, contactList.get(i).getCompanyActivity());

                excelSheet.addCell(companyNameContent);
                excelSheet.addCell(companyAddressContent);
                excelSheet.addCell(companyTelephoneContent);
                excelSheet.addCell(companyActivityContent);
            }

            myFirstWbook.write();

        } catch (IOException e) {
            e.printStackTrace();
        } catch (WriteException e) {
            e.printStackTrace();
        } finally {
            if (myFirstWbook != null) {
                try {
                    myFirstWbook.close();
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (WriteException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
