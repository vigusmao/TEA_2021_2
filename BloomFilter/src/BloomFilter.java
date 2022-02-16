import java.util.Objects;

public class BloomFilter<T> {

    boolean[] filter;

    /** máximo de elementos que espero ter */
    int n;

    /** tamanho do filtro em bits */
    int m;

    /** número de funções computeHash que usaremos */
    int k;

    /** número de operações add() já feitas
     *  (não necessariamente o número de elementos distintos!)
     */
    private int currentSize;

    public BloomFilter(int expectedCapacity,
                       int bitsPerElement) {

        this(expectedCapacity, bitsPerElement,
                getOptimalNumberOfHashFunctions(
                        expectedCapacity, expectedCapacity * bitsPerElement));
    }

    public BloomFilter(int expectedCapacity,
                       int bitsPerElement,
                       int numberOfHasFunctions) {

        this.n = expectedCapacity;
        this.m = expectedCapacity * bitsPerElement;
        this.filter = new boolean[this.m];
        this.k = numberOfHasFunctions;

        System.out.println("number of hash functions = " + k);
    }

    public void add(T element) {
        for (int hashIndex = 1; hashIndex <= this.k; hashIndex++) {
            int pos = computeHash(element, hashIndex, this.m);
            this.filter[pos] = true;
        }
        this.currentSize++;
    }

    public boolean probablyContains(T element) {
        for (int hashIndex = 1; hashIndex <= this.k; hashIndex++) {
            int pos = computeHash(element, hashIndex, this.m);
            if (!this.filter[pos]) {
                return false;
            }
        }
        return true;
    }

    public int getSize() {
        return currentSize;
    }

    public static <T> int computeHash(T element, int hashIndex, int rangeSize) {
//        int result = MurmurHash3.hash32(element.hashCode(), hashIndex) % rangeSize;
        int result = Objects.hash(hashIndex, element) % rangeSize;
        if (result < 0) {
            result += rangeSize;
        }
        return result;
    }

    public static int getOptimalNumberOfHashFunctions(int n, int m) {
        return Math.max(1,
                Math.min(100,
                        (int) Math.ceil(Math.log(2) * m/n)));
    }
}
