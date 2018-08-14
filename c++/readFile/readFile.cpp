#include<iostream>
#include<fstream>
#include<string>
#include<cstring> // used for introducing std::strcpy() which converts string to char*


/* // to convert from string to char* then can use fprintf of that char to print to a file
 * FILE* myFile = fopen("write_file.txt","w");
 * std::string a = "hello people";
 *char *b = new char[x.length()+1]; // could also just do char *b = new char[100]; or something else so large it will certainly be big enough
 * // the char* is just a pointer it doesn't actually contain the string so you gave to have the character managed elsewhere. std::string actuallly holds the string as has several operations such as: string.length(), string[0] that allow you to use the information in the string more directly
 *std::strcpy(b,a);
 *fprintf(myFile,b);
 */

/* // to convert from char* to string
 * const char* foo = "Whatever";
 * string bar = foo;
 */



using namespace std;
// std::string

int main(){
	
	FILE* myFile2 = fopen("example.txt","w");
	cout << "printing to file" << endl;
	string reading_lines;
	fstream myFile("read.txt");
	if (myFile.is_open()){
		cout << "OPEN!";
		while (getline(myFile,reading_lines)){
			//cout << "Line: " << reading_lines <<"\n";
			//cout << "starting value: " << reading_lines[0]<< "\n";
			
			char *y = new char[reading_lines.length()+1];

			std::strcpy(y,reading_lines.c_str());
			cout << "\ny = " << y;
			fprintf(myFile2,y);
			fprintf(myFile2,"\n");
		}
		myFile.close();
	}
	else{
		cout << "DIDN'T OPEN";
	}

	return 0;
}
