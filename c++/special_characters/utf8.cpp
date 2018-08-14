#include<string>
#include<iostream>

int main(){
//__setmode(_fileno(stdout), _O_U8TEXT);
std::string test = "Greek: αβγδ; German: Übergrößenträger";
std::string test2 = "\u0651";
std::cout << "test1: " <<  test << ", test2: " << test2 << "\n";

return 0;
}

/*
test1: Greek: αβγδ; German: Übergrößenträger, test2: ّ
*/


