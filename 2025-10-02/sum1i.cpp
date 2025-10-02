#include <print>
#include <fstream>
#include <cmath>

float sumcre(int n);
float sumdec(int n);

int main()
    {
        std::ofstream fout("data.txt");

        for(int nmax = 1; nmax < 1000000000; nmax = 2*nmax)
        {
            float recre = sumcre(nmax);
            float redec = sumdec(nmax);
            float diff = std::fabs(1 - recre/redec);
            std::println(fout, "{:12} {:15.6e} {:15.6e} {:15.6e}", nmax, recre, redec, diff);
        }       

        fout.close();

        return 0;
    }

float sumcre(int n)
    {
        float sum1{0.0};
        
        for(int i=1; i<=n; i++)
            {
                sum1 = sum1 + (1.0/i);
            }
        
        return sum1;
    }

float sumdec(int n)
    {
        float sum2{0.0};
        
        for(int i=n; i>=1; i--)
            {
                sum2 = sum2 + (1.0/i);
            }
        
        return sum2;
    }