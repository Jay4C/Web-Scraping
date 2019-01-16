package Model;

public class Contact {
    private String companyName;
    private String conpanyAddress;
    private String companyActivity;
    private String companyTelephone;

    public String getCompanyName() {
        return companyName;
    }

    public void setCompanyName(String companyName) {
        this.companyName = companyName;
    }

    public String getConpanyAddress() {
        return conpanyAddress;
    }

    public void setConpanyAddress(String conpanyAddress) {
        this.conpanyAddress = conpanyAddress;
    }

    public String getCompanyActivity() {
        return companyActivity;
    }

    public void setCompanyActivity(String companyActivity) {
        this.companyActivity = companyActivity;
    }

    public String getCompanyTelephone() {
        return companyTelephone;
    }

    public void setCompanyTelephone(String companyTelephone) {
        this.companyTelephone = companyTelephone;
    }

    public Contact() {
    }

    public Contact(String companyName, String conpanyAddress, String companyActivity, String companyTelephone) {
        this.companyName = companyName;
        this.conpanyAddress = conpanyAddress;
        this.companyActivity = companyActivity;
        this.companyTelephone = companyTelephone;
    }
}
