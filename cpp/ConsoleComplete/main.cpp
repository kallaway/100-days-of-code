#include <iostream>

using namespace std;

string DICTIONARY[] = {
	"alibaba",
	"alphabet",
	"amazon",
	"apple"
};

bool contains(string str1, string str2) {
	// returns true if str1 contains str2, else false
	
	return (str1.find(str2) != string::npos);
}

string getMatch(string text) {
	// returns the closest match in the DICTIONARY to text
	
	for (int i = 0; i < 4; i++) {
		if (contains(DICTIONARY[i], text)) {
			return DICTIONARY[i];
		}
	}
	
	return text;
}

int main(int argc, char** argv) {
	string input, closestMatch;
	
	cin >> input;
	
	closestMatch = getMatch(input);
	cout << closestMatch << "\n\n\n\n\n\n";
	
	return 0;
}
