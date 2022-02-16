import org.junit.Test;

import java.util.HashSet;
import java.util.Random;
import java.util.Set;

import static org.junit.Assert.*;

public class BloomFilterTest {

    Random random = new Random(234765);

    final int TAMANHO = 1000;
    final int BITS_PER_ELEMENT = 12;
    final int RANGE_SIZE = 10000;

    @Test
    public void testarFuncionamentoBasico() {
        BloomFilter<Long> filtro = new BloomFilter<>(
                TAMANHO, BITS_PER_ELEMENT);
        Set<Long> conjunto = new HashSet<>();

        while (conjunto.size() < TAMANHO) {
            long element = random.nextInt(RANGE_SIZE);
            conjunto.add(element);
            filtro.add(element);
        }

        System.out.println(conjunto);

        for (long elementInSet : conjunto) {
            assertTrue(filtro.probablyContains(elementInSet));
        }

        // verifica a inexistência de falsos negativos
        // e conta quandos falsos positivos houve
        int contFalsePositives = 0;
        int contPositives = 0;
        for (long i = 0; i < RANGE_SIZE; i++) {
//            long element = random.nextInt(1000);
            boolean existsInSet = conjunto.contains(i);
            if (filtro.probablyContains(i)) {
//                System.out.printf("\n" + i);
                contPositives++;
                if (!existsInSet) {
                    contFalsePositives++;
//                    System.out.println(" (false!)");
                }
            } else {
                assertFalse(existsInSet);
            }
        }


        double falsePositivesOverTotal =
                contFalsePositives / (double) RANGE_SIZE;
        double falsePositivesOverPositives =
                contFalsePositives / (double) contPositives;
        double positivesOverTotal =
                contPositives / (double) RANGE_SIZE;
        double negativesOverTotal =
                (RANGE_SIZE - contPositives) / (double) RANGE_SIZE;

        System.out.printf("\ntotal queries = %d",
                RANGE_SIZE);
        System.out.printf("\ntotal numbers in set = %d",
                TAMANHO);


        System.out.printf("\n\ntotal negative answers = %d",
                (RANGE_SIZE - contPositives));
        System.out.printf("\nnegatives over total = %.1f%%",
                negativesOverTotal * 100);

        System.out.printf("\n\ntotal positive answers = %d",
                contPositives);
        System.out.printf("\npositives over total = %.2f%%",
                positivesOverTotal * 100);
        System.out.printf("\nfalse positives = %d",
                contFalsePositives);
        System.out.printf("\nfalse positives over total = %.2f%%",
                falsePositivesOverTotal * 100);
        System.out.printf("\nfalse positives over positives = %.2f%%",
                falsePositivesOverPositives * 100);

        System.out.printf("\n\nwrong answers over total = %.2f%%\n\n",
                falsePositivesOverTotal * 100);


    }
}