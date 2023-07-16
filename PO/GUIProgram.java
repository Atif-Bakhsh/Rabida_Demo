// package PO;

// import java.util.Locale;
// import java.util.ResourceBundle;
// import javax.swing.*;

// public class GUIProgram {
//     private static ResourceBundle bundle;

//     public static void main(String[] args) {
//         setLanguage("en"); // Set the desired language ('en' for English)

//         SwingUtilities.invokeLater(() -> {
//             createGUI();
//         });
//     }

//     private static void setLanguage(String lang) {
//         Locale locale = new Locale(lang);
//         bundle = ResourceBundle.getBundle("PO.resources.translations", locale);
//     }

//     private static void createGUI() {
//         JFrame frame = new JFrame(bundle.getString("LoginTitle"));
//         frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

//         JPanel panel = new JPanel();

//         JLabel emailLabel = new JLabel(bundle.getString("EnterEmail"));
//         panel.add(emailLabel);

//         JTextField emailField = new JTextField(20);
//         panel.add(emailField);

//         JLabel passwordLabel = new JLabel(bundle.getString("EnterPassword"));
//         panel.add(passwordLabel);

//         JPasswordField passwordField = new JPasswordField(20);
//         panel.add(passwordField);

//         JButton submitButton = new JButton(bundle.getString("SubmitButton"));
//         panel.add(submitButton);

//         frame.getContentPane().add(panel);
//         frame.pack();
//         frame.setVisible(true);
//     }
// }
