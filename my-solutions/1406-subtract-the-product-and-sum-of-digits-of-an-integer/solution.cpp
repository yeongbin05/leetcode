class Solution {
public:
    int subtractProductAndSum(int n) {
        int p = 1, s = 0;
        int divisor = 10;
        int quotient = n;
        int modulo  ;
        while(1){

            modulo = quotient % divisor;
            quotient = quotient/divisor;

            p = p * modulo;
            s = s + modulo;

            if (quotient <= 0){
                break;
            }
        }

        return p-s;
    }
};
