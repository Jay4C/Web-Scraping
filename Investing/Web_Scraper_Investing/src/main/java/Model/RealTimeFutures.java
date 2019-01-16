package Model;

public class RealTimeFutures {
    private String matierePremiere;
    private String mois;
    private String dernier;
    private String plusHaut;
    private String plusBas;
    private String variation;
    private String variationPourcentage;
    private String date;
    private String heure;

    public RealTimeFutures() {
    }

    public RealTimeFutures(String matierePremiere, String mois, String dernier, String plusHaut, String plusBas, String variation, String variationPourcentage, String date, String heure) {
        this.matierePremiere = matierePremiere;
        this.mois = mois;
        this.dernier = dernier;
        this.plusHaut = plusHaut;
        this.plusBas = plusBas;
        this.variation = variation;
        this.variationPourcentage = variationPourcentage;
        this.date = date;
        this.heure = heure;
    }

    public String getMatierePremiere() {
        return matierePremiere;
    }

    public void setMatierePremiere(String matierePremiere) {
        this.matierePremiere = matierePremiere;
    }

    public String getMois() {
        return mois;
    }

    public void setMois(String mois) {
        this.mois = mois;
    }

    public String getDernier() {
        return dernier;
    }

    public void setDernier(String dernier) {
        this.dernier = dernier;
    }

    public String getPlusHaut() {
        return plusHaut;
    }

    public void setPlusHaut(String plusHaut) {
        this.plusHaut = plusHaut;
    }

    public String getPlusBas() {
        return plusBas;
    }

    public void setPlusBas(String plusBas) {
        this.plusBas = plusBas;
    }

    public String getVariation() {
        return variation;
    }

    public void setVariation(String variation) {
        this.variation = variation;
    }

    public String getVariationPourcentage() {
        return variationPourcentage;
    }

    public void setVariationPourcentage(String variationPourcentage) {
        this.variationPourcentage = variationPourcentage;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getHeure() {
        return heure;
    }

    public void setHeure(String heure) {
        this.heure = heure;
    }
}
