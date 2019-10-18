#include <iostream>
#include "basicOCR.h"

using namespace std;

bool contains(string str1, string str2) {
	// returns true if str1 contains str2, else false
	
	return (str1.find(str2) != string::npos);
}

bool imgContainsText(imgPath, text) {
	string imgText = getText(imgPath);
	
	return contains(imgText, text);
}

int main(int argc, char** argv) {
	string query, results;
	
	cout << "Please type in what you want to search for: ";
	cin >> query;
	results = "";
	
	for (int i = 1; i < argc) {
		if (imgContainsText(argv[i], query)) {
			results += argv[i];
		}
	}
 
    if (resuls.length())
    
    cout << outText;
    
	return 0;
}
