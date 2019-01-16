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
public class Cryptocurrency {
    private String nombreDeDevise;
    private String capitalisationTotaleDuMarche;
    private String volumeTotal24H;
    private String numero;
    private String nom;
    private String symbole;
    private String coursUSD;
    private String capitalisationBoursiere;
    private String volume24H;
    private String volumeTotal;
    private String variation24H;
    private String variation7Jours;

    public Cryptocurrency(String nombreDeDevise, String capitalisationTotaleDuMarche, String volumeTotal24H, String numero, String nom, String symbole, String coursUSD, String capitalisationBoursiere, String volume24H, String volumeTotal, String variation24H, String variation7Jours) {
        this.nombreDeDevise = nombreDeDevise;
        this.capitalisationTotaleDuMarche = capitalisationTotaleDuMarche;
        this.volumeTotal24H = volumeTotal24H;
        this.numero = numero;
        this.nom = nom;
        this.symbole = symbole;
        this.coursUSD = coursUSD;
        this.capitalisationBoursiere = capitalisationBoursiere;
        this.volume24H = volume24H;
        this.volumeTotal = volumeTotal;
        this.variation24H = variation24H;
        this.variation7Jours = variation7Jours;
    }

    public Cryptocurrency() {
    }

    public String getNombreDeDevise() {
        return nombreDeDevise;
    }

    public void setNombreDeDevise(String nombreDeDevise) {
        this.nombreDeDevise = nombreDeDevise;
    }

    public String getCapitalisationTotaleDuMarche() {
        return capitalisationTotaleDuMarche;
    }

    public void setCapitalisationTotaleDuMarche(String capitalisationTotaleDuMarche) {
        this.capitalisationTotaleDuMarche = capitalisationTotaleDuMarche;
    }

    public String getVolumeTotal24H() {
        return volumeTotal24H;
    }

    public void setVolumeTotal24H(String volumeTotal24H) {
        this.volumeTotal24H = volumeTotal24H;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getSymbole() {
        return symbole;
    }

    public void setSymbole(String symbole) {
        this.symbole = symbole;
    }

    public String getCoursUSD() {
        return coursUSD;
    }

    public void setCoursUSD(String coursUSD) {
        this.coursUSD = coursUSD;
    }

    public String getCapitalisationBoursiere() {
        return capitalisationBoursiere;
    }

    public void setCapitalisationBoursiere(String capitalisationBoursiere) {
        this.capitalisationBoursiere = capitalisationBoursiere;
    }

    public String getVolume24H() {
        return volume24H;
    }

    public void setVolume24H(String volume24H) {
        this.volume24H = volume24H;
    }

    public String getVolumeTotal() {
        return volumeTotal;
    }

    public void setVolumeTotal(String volumeTotal) {
        this.volumeTotal = volumeTotal;
    }

    public String getVariation24H() {
        return variation24H;
    }

    public void setVariation24H(String variation24H) {
        this.variation24H = variation24H;
    }

    public String getVariation7Jours() {
        return variation7Jours;
    }

    public void setVariation7Jours(String variation7Jours) {
        this.variation7Jours = variation7Jours;
    }
}
