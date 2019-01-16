package Model;

public class Wages
{
    private String country;
    private String last;
    private String monthYear;
    private String previous;
    private String highest;
    private String lowest;
    private String currencyPeriod;
    private String changePeriod;

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getLast() {
        return last;
    }

    public void setLast(String last) {
        this.last = last;
    }

    public String getMonthYear() {
        return monthYear;
    }

    public void setMonthYear(String monthYear) {
        this.monthYear = monthYear;
    }

    public String getPrevious() {
        return previous;
    }

    public void setPrevious(String previous) {
        this.previous = previous;
    }

    public String getHighest() {
        return highest;
    }

    public void setHighest(String highest) {
        this.highest = highest;
    }

    public String getLowest() {
        return lowest;
    }

    public void setLowest(String lowest) {
        this.lowest = lowest;
    }

    public String getCurrencyPeriod() {
        return currencyPeriod;
    }

    public void setCurrencyPeriod(String currencyPeriod) {
        this.currencyPeriod = currencyPeriod;
    }

    public String getChangePeriod() {
        return changePeriod;
    }

    public void setChangePeriod(String changePeriod) {
        this.changePeriod = changePeriod;
    }

    public Wages(String country, String last, String monthYear, String previous, String highest, String lowest, String currencyPeriod, String changePeriod) {
        this.country = country;
        this.last = last;
        this.monthYear = monthYear;
        this.previous = previous;
        this.highest = highest;
        this.lowest = lowest;
        this.currencyPeriod = currencyPeriod;
        this.changePeriod = changePeriod;
    }

    public Wages() {
    }
}
