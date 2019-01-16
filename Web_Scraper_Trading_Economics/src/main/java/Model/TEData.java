package Model;

public class TEData {
    private String Country;
    private String Last;
    private String MonthYear;
    private String Previous;
    private String Highest;
    private String Lowest;
    private String Unit;
    private String Period;

    public String getCountry() {
        return Country;
    }

    public void setCountry(String country) {
        Country = country;
    }

    public String getLast() {
        return Last;
    }

    public void setLast(String last) {
        Last = last;
    }

    public String getMonthYear() {
        return MonthYear;
    }

    public void setMonthYear(String monthYear) {
        MonthYear = monthYear;
    }

    public String getPrevious() {
        return Previous;
    }

    public void setPrevious(String previous) {
        Previous = previous;
    }

    public String getHighest() {
        return Highest;
    }

    public void setHighest(String highest) {
        Highest = highest;
    }

    public String getLowest() {
        return Lowest;
    }

    public void setLowest(String lowest) {
        Lowest = lowest;
    }

    public String getUnit() {
        return Unit;
    }

    public void setUnit(String unit) {
        Unit = unit;
    }

    public String getPeriod() {
        return Period;
    }

    public void setPeriod(String period) {
        Period = period;
    }

    public TEData() {
    }

    public TEData(String country, String last, String monthYear, String previous, String highest, String lowest, String unit, String period) {
        Country = country;
        Last = last;
        MonthYear = monthYear;
        Previous = previous;
        Highest = highest;
        Lowest = lowest;
        Unit = unit;
        Period = period;
    }
}
