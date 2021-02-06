#include <iostream>
#include <windows.h>

using namespace std;

const int BLUE = 1;
const int GREEN = 2;
const int RED = 4;
const int WHITE = 15;

void clearScreen(int characterLength) {
	for (int i = 0; i < characterLength; i++) {
		cout << "\b";
	}
}

void changeColour(int colour) {
	HANDLE hConsole;
	
	hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, colour);
}

void showLoadingScreen() {
	int i;
	string closed = "- - -", open = "* * *";
	int colour[] = {RED, GREEN, BLUE};
	
	cout << closed;
	
	for (i = 0; i < 3; i++) {
		Sleep(1000);
		
		clearScreen(5);
		changeColour(colour[i]);
		
		cout << open;
		
		Sleep(1000);
		
		clearScreen(5);
		changeColour(WHITE);
		
		cout << closed;
	}
	
	clearScreen(5);
	changeColour(WHITE);
}

void showBlinkingLights() {
	changeColour(RED);
	cout << "BLINK";
	Sleep(1000);
	
	changeColour(GREEN);
	cout << "ING";
	Sleep(1000);
	
	changeColour(BLUE);
	cout << " LIGHTS";
	Sleep(1000);
	
	changeColour(WHITE);
}

int main(int argc, char** argv) {
	cout << "\n\n\n";
	cout << "      ";
	
	showLoadingScreen();
	showBlinkingLights();
	
	cout << "\n\n\n";
	
	return 0;
}
