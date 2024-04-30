public class CaesarCipher {
    public static String encrypt(String text, int shift) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);
            if (Character.isUpperCase(ch)) {
                ch = (char) ((ch - 'A' + shift) % 26 + 'A');
            }
            result.append(ch);
        }

        return result.toString();
    }
    
    public static String decrypt(String text, int shift) {
        return encrypt(text, 26 - shift); // Decryption is just encryption with the opposite shift
    }

    public static void main(String[] args) {
        String plaintext = "HELLO WORLD";
        int shift = 3;
        String encryptedText = encrypt(plaintext, shift);
        System.out.println("Encrypted text: " + encryptedText);
        
        String decryptedText = decrypt(encryptedText, shift);
        System.out.println("Decrypted text: " + decryptedText);
    }
}

