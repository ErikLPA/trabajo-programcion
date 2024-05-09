import java.util.Scanner;

public class caladora_de_trimestre {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicitar al usuario que introduzca el día, mes y año de nacimiento
        System.out.println("Ingresa el día de su nacimiento:");
        int dia = scanner.nextInt();
        System.out.println("Ingresa el mes de su nacimiento:");
        int mes = scanner.nextInt();
        System.out.println("Ingresa el año de su nacimiento:");
        int año = scanner.nextInt();

        // Calcular el trimestre de acuerdo al mes de nacimiento
        int trimestre = obtenerTrimestre(mes);

        // Imprimir el resultado
        System.out.println("Usted nació en el " + obtenerNombreTrimestre(trimestre) + " trimestre del año.");
    }

    // Función para determinar el trimestre de acuerdo al mes
    public static int obtenerTrimestre(int mes) {
        if (mes >= 1 && mes <= 3) {
            return 1;
        } else if (mes >= 4 && mes <= 6) {
            return 2;
        } else if (mes >= 7 && mes <= 9) {
            return 3;
        } else {
            return 4;
        }
    }

    // Función para obtener el nombre del trimestre
    public static String obtenerNombreTrimestre(int trimestre) {
        switch (trimestre) {
            case 1:
                return "primer";
            case 2:
                return "segundo";
            case 3:
                return "tercer";
            case 4:
                return "cuarto";
            default:
                return "trimestre inválido";
        }
    }
}
