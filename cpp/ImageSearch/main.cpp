#include <iostream>
#include <dirent.h>
#include "basicOCR.h"

using namespace std;

bool contains(string str1, string str2)
{
	// Returns true if str1 contains str2, else false

	return (str1.find(str2) != string::npos);
}

bool endsWith(string s, string endString) {
	// Returns true if s ends with endString, else false
	
	return s.length() >= endString.length() && s.substr(s.length() - endString.length()) == endString;
}

bool isImage(string fileName) {
	// Returns true if the file is a GIF, PNG or a JPG image, else false

	return endsWith(fileName, ".gif") || endsWith(fileName, ".png") || endsWith(fileName, ".jpg");
}

bool imgContainsText(string imgPath, string text)
{
	// Returns true if the text in the image contains the specified text, else false
	
	string imgText = getText(imgPath);

	return contains(imgText, text);
}

int main(int argc, char **argv)
{
	DIR *dir;
	struct dirent *ent;
	char *imFolder = argv[1];
	string fileName, query, results = "";
	
	cout << "Enter the text to search for: ";

	cin >> query;

	if ((dir = opendir(imFolder)) != NULL)
	{
		while ((ent = readdir(dir)) != NULL)
		{
			fileName = ent->d_name;
			if (isImage(fileName) && imgContainsText(imFolder + fileName, query)) {
				results += fileName + "\n";
			}
		}
		closedir(dir);
	}
	else
	{
		/* could not open directory */
		perror("");
		return EXIT_FAILURE;
	}

	cout << "\n\n\n";

	if (results.length() > 0) {
		cout << "The text was found in: \n" + results;
	}
	else
	{
		cout << "Sorry, the text was not found in any image.";
	}
	

	return 0;
}
