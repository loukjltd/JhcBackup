public class TestWhile3 {
    public static void main(String[] args) {
        for (int triangleLine = 1; triangleLine <= 5; triangleLine ++) {
            for (int triangleColumn = 1; triangleColumn <= triangleLine; triangleColumn ++) {
                System.out.print("※\t");
            }
            System.out.println("\t");
        }

        System.out.println("\t");

        for (int triangleLine = 1; triangleLine <= 5; triangleLine ++) {
            for (int triangleColumn = 1; triangleColumn <= 6 - triangleLine; triangleColumn ++) {
                System.out.print("※\t");
            }
            System.out.println("\t");
        }

        System.out.println("\t");

        int initialNum = 4;
        for (int triangleLine = 0; triangleLine <= 4; triangleLine ++) {
            for (int triangleColumn = 0; triangleColumn <= 10; triangleColumn++) {
                if (triangleColumn >= initialNum - triangleLine && triangleColumn <= initialNum + triangleLine) {
                    System.out.print("※\t");
                }else {
                    System.out.print("\t");
                }
            }
            System.out.println();
        }

        System.out.println("\t");

        for (int matrixLine = 0; matrixLine <=4; matrixLine ++) {
            for (int matrixColumn = 0; matrixColumn <= 4; matrixColumn ++) {
                if ((matrixColumn + 2) % 2 == 0) {
                    if ((matrixLine + 2) % 2 == 0) {
                        System.out.print("*\t");
                    } else {
                        System.out.print("#\t");
                    }
                } else {
                    if (matrixLine % 2 == 1) {
                        System.out.print("*\t");
                    } else {
                        System.out.print("#\t");
                    }
                }
            }
            System.out.println("\t");
        }
    }
}
