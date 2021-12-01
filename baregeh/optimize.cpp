// using the gmp library for multiple precision numbers
#include <gmp.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main(int argc, char *argv[])
{
    unsigned long a, b, c;
    // 
    mpz_t a_mpz, b_mpz, c_mpz, d_mpz, a4, b4, c4, d4;
    mpz_init(a_mpz);
    mpz_init(b_mpz);
    mpz_init(c_mpz);
    mpz_init(d_mpz);
    mpz_init(a4);
    mpz_init(b4);
    mpz_init(c4);
    mpz_init(d4);

    for (a = 1; a < 100000; a++)
    {
        for (b = 1; b < 300000; b++)
        {
            for (c = 1; c < 500000; c++)
            // I removed the fourth for loop because we didn't need it, we only
            // need to confirm only if the result of a^4 + b^4 + c^4 has a complete root of 4
            // and d is an integer number
            {

                // create mpz numbers for each iterated variable
                mpz_init_set_ui(a_mpz, a);
                mpz_init_set_ui(b_mpz, b);
                mpz_init_set_ui(c_mpz, c);

                // set each of the variables a^4 , b^4, c^4
                mpz_pow_ui(a4, a_mpz, 4);
                mpz_pow_ui(b4, b_mpz, 4);
                mpz_pow_ui(c4, c_mpz, 4);

                // d4 = a4 + b4 + c4
                mpz_add(d4, a4, b4);
                mpz_add(d4, d4, c4);

                // if d4 has a complete root of 4 ...
                if (mpz_root(d_mpz, d4, 4) != 0)
                {
                    // if d_mpz is lesser that 500000
                    int comparison = mpz_cmp_ui(d_mpz, 500000);
                    if (comparison < 0)
                        gmp_printf("Found It! a=%Zd b=%Zd c=%Zd d=%Zd", a_mpz, b_mpz, c_mpz, d_mpz);
                }
            }
        }
    }
    return 0;
}