#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
int main(){
    uint8_t c;
    std::vector<uint8_t> x;
    while((c = std::cin.get()) != '\n'){
        x.push_back(c);
    }
    std::vector<uint8_t> y;
    while((c = std::cin.get()) != '\n'){
        y.push_back(c);
    }
    std::vector <std::vector<uint16_t>> L(x.size() + 1, std::vector<uint16_t>(y.size() + 1));
    for (int16_t i = 0; i < x.size(); i++){
        for (int16_t j = 0; j < y.size(); j++){
            int16_t f_i = i - 1;
            int16_t f_j = j - 1;
            if (i == 0){
                f_i = x.size();
            }
            if (j == 0){
                f_j = y.size();
            }
            if (x[i] == y[j]){
                L[i][j] = L[f_i][f_j] + 1;
            }else{
                if (L[i][f_j] < L[f_i][j]){
                    L[i][j] = L[f_i][j];
                }else{
                    L[i][j] = L[i][f_j];
                }
            }
        }
    }
     
    std::vector <unsigned char>lcs;       
    int16_t i = x.size() - 1;
    int16_t j = y.size() - 1;
    while (i >= 0 && j >= 0){
        int16_t f_i = i - 1;
        int16_t f_j = j - 1;
        if (i == 0){
            f_i = x.size();
        }
        if (j == 0){
            f_j = y.size();
        }
        if (x[i] == y[j]){
            lcs.push_back(x[i]);
            i--;
            j--;
        }else if (L[f_i][j] > L[i][f_j]){
            i--;
        }else{
            j--;
        }
    }
    for (uint16_t i = lcs.size(); i > 0; i--){
        std::cout << lcs[i - 1];
    }
    std::cout << "\n";
    return 0;
}