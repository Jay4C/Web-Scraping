public class Parity
{
    private String parity, heure, bid, ask, l, h, pc, pcp;

    public String getParity() {
        return parity;
    }

    public void setParity(String parity) {
        this.parity = parity;
    }

    public String getHeure() {
        return heure;
    }

    public void setHeure(String heure) {
        this.heure = heure;
    }

    public String getBid() {
        return bid;
    }

    public void setBid(String bid) {
        this.bid = bid;
    }

    public String getAsk() {
        return ask;
    }

    public void setAsk(String ask) {
        this.ask = ask;
    }

    public String getL() {
        return l;
    }

    public void setL(String l) {
        this.l = l;
    }

    public String getH() {
        return h;
    }

    public void setH(String h) {
        this.h = h;
    }

    public String getPc() {
        return pc;
    }

    public void setPc(String pc) {
        this.pc = pc;
    }

    public String getPcp() {
        return pcp;
    }

    public void setPcp(String pcp) {
        this.pcp = pcp;
    }

    public Parity(String parity, String heure, String bid, String ask, String l, String h, String pc, String pcp) {
        this.parity = parity;
        this.heure = heure;
        this.bid = bid;
        this.ask = ask;
        this.l = l;
        this.h = h;
        this.pc = pc;
        this.pcp = pcp;
    }

    public Parity() {
    }
}
