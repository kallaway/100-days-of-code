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

string getMatch(string partialWord) {
	// returns the closest match in the DICTIONARY to partialWord
	
	for (int i = 0; i < 4; i++) {
		if (contains(DICTIONARY[i], partialWord)) {
			return DICTIONARY[i];
		}
	}
	
	return partialWord;
}

int main(int argc, char** argv) {
	string input, closestMatch;
	int inputLength;
	
	cin >> input;
	inputLength = input.length();
	
	closestMatch = getMatch(input);
	cout << closestMatch << "\n\n\n\n\n\n";
	
	return 0;
}
