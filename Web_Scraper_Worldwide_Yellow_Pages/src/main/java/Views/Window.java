package Views;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import static Service.ExtractData.extractPagesJaunes;

public class Window extends Frame {
    private JTextField urlField = new JTextField();
    private JTextField destinationFolderField = new JTextField();

    public Window(){
        this.setTitle("Web scraper - Pages Jaunes");
        this.setSize(1400, 700);
        this.setLocationRelativeTo(null);
        this.setVisible(true);

        //Add components
        //Label Text URL
        final JLabel urlLabel = new JLabel("Insert the URL :");
        urlLabel.setBounds(50,50, 100,20);
        //Text Field URL
        urlField.setBounds(50,80, 600,20);

        //Label Text Destination Folder
        JLabel destinationFolderLabel = new JLabel("Insert the destination folder :");
        destinationFolderLabel.setBounds(50,120, 600,20);
        //Text Field Destination Folder
        destinationFolderField.setBounds(50,150, 600,20);

        //Button Erase URL Text
        JButton buttonEraseURL = new JButton("Erase URL Text");
        buttonEraseURL.setBounds(50,190,200,30);
        buttonEraseURL.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                urlField.setText("");
            }
        });

        //Button Extract Data
        JButton buttonExtractData = new JButton("Extract data");
        buttonExtractData.setBounds(50,230,200,30);
        buttonExtractData.addActionListener( new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                try
                {
                    String url = urlField.getText();
                    String destinationFolder = destinationFolderField.getText();
                    extractPagesJaunes(url,destinationFolder);
                }
                catch(Exception e1)
                {
                    System.out.println(e1);
                }
            }
        });

        //Button Erase DestinationFolder text
        JButton buttonEraseDestinationFolder = new JButton("Erase Destination folder");
        buttonEraseDestinationFolder.setBounds(50,270,300,30);
        buttonEraseDestinationFolder.addActionListener( new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                destinationFolderField.setText("");
            }
        });

        //Button Exit
        JButton buttonExit = new JButton("Exit");
        buttonExit.setBounds(50,310,200,30);
        buttonExit.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });

        add(urlLabel); add(urlField);
        add(destinationFolderLabel); add(destinationFolderField);
        add(buttonEraseURL); add(buttonExtractData); add(buttonEraseDestinationFolder); add(buttonExit);
    }
}
