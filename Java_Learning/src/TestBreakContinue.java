public class TestBreakContinue {
    public static void main(String[] args) {
        int animalCaughtCount = 0;
        while (true){
            String randomAnimalName = "";

            int randomAnimalNum = (int) (Math.random() * 5 + 1);
            switch (randomAnimalNum) {
                case 1:
                    randomAnimalName = "Tiger";
                    break;
                case 2:
                    randomAnimalName = "Eager";
                    break;
                case 3:
                    randomAnimalName = "Cat";
                    break;
                case 4:
                    randomAnimalName = "Dog";
                    break;
                case 5:
                    randomAnimalName = "Turtle";
                    break;
                default:
                    randomAnimalName = "The Game went wrong!";
                    break;
            }
            if (randomAnimalName.equals("Tiger")) {
                System.out.println("That is a Tiger, RUN!");
                break;
            } else if (randomAnimalName.equals("Eager")) {
                System.out.println("An Eager? Not bad!");
            } else {
                animalCaughtCount ++;
                System.out.println("You've caught a(n) " + randomAnimalName + "!");
            }
        }
        System.out.println("In total, the number you've caught is " + animalCaughtCount + "!");
    }
}
