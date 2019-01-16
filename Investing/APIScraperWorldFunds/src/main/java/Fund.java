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

public class Fund {
    private String name;
    private String symbol;
    private String last;
    private String variationInPourcentage;
    private String totalVolume;
    private String date;
    private String hours;

    public Fund() {
    }

    public Fund(String name, String symbol, String last, String variationInPourcentage, String totalVolume, String date, String hours) {
        this.name = name;
        this.symbol = symbol;
        this.last = last;
        this.variationInPourcentage = variationInPourcentage;
        this.totalVolume = totalVolume;
        this.date = date;
        this.hours = hours;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public String getLast() {
        return last;
    }

    public void setLast(String last) {
        this.last = last;
    }

    public String getVariationInPourcentage() {
        return variationInPourcentage;
    }

    public void setVariationInPourcentage(String variationInPourcentage) {
        this.variationInPourcentage = variationInPourcentage;
    }

    public String getTotalVolume() {
        return totalVolume;
    }

    public void setTotalVolume(String totalVolume) {
        this.totalVolume = totalVolume;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getHours() {
        return hours;
    }

    public void setHours(String hours) {
        this.hours = hours;
    }
}
