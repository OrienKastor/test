#include<iostream>
#include<fstream>
#include<math.h>
#include<cstring>
#include<string>

using namespace std;

int main()
{

	/*string reading_lines;
	fstream myfile("example.txt");
	if (myfile.is_open()) {
		while (getline(myfile,reading_lines)) {
			cout << "Line: " << reading_lines << endl;
		}
		myfile.close();
	} 
	else {
		cout << "Unable to open file." << endl;
	}*/

	using namespace std;

	FILE* myFile = fopen("example.txt","w"); // read=r, write=w, append=a
	fprintf(myFile,"\nPrinting to file!\n");
	fclose(myFile);

	string a = "hello, how are you?";
	char b [] = stringToChar(a);
	fprintf(myFile,b);

	cin.get(); // or: system("Pause") but that limits the system to windows
	return 0;
}

char stringToChar (string a){
	int c = a.length();
	char b [c];
	for (int n = 0; n++; n<c){
		b[n] = a[n];
	}
	return b;
}
