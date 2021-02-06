#include <iostream>
#include <windows.h>
#include <tgmath.h>

using namespace std;

int getNumber() {
	int number;
	
	HANDLE hStdin = GetStdHandle(STD_INPUT_HANDLE);
	DWORD mode = 0;
	GetConsoleMode(hStdin, &mode);
	SetConsoleMode(hStdin, mode & (-ENABLE_ECHO_INPUT));
	
	cin >> number;
	
	SetConsoleMode(hStdin, mode);
	
	return number;
}

double getAverage(int nums[], int size) {
	int i, sum = 0;
	double avg;
	
	for (i = 0; i < size; i++) {
		sum += nums[i];
	}
	avg = double(sum) / size;
	
	return avg;
}

int getClosest(int nums[], int size, double value) {
	int i, closest;
	double diff, closestDiff;
	
	for (i = 0; i < size; i++) {
		diff = fabs(double(nums[i]) - value);
		closest = closestDiff < diff ? closest : nums[i];
		closestDiff = fabs(double(closest) - value);
	}
	
	return closest;
}

int main(int argc, char** argv) {
	int entries[3], closest;
	double avg, twoThirds;
	string winner;
	
	cout << "Hello and welcome to the game: Two Thirds of Average" << "\n";
	
	cout << "Player1, please enter a number: ";
	entries[0] = getNumber();
	
	cout << "\nPlayer2, please enter a number: ";
	entries[1] = getNumber();
	
	cout << "\nPlayer3, please enter a number: ";
	entries[2] = getNumber();
	
	avg = getAverage(entries, 3);
	twoThirds = (2 * avg) / 3;
	closest = getClosest(entries, 3, twoThirds);
	
	cout << "\nThe numbers are: ";
	cout << entries[0];
	cout << " ";
	cout << entries[1];
	cout << " ";
	cout << entries[2];
	
	cout << "\nThe average is: ";
	cout << avg;
	
	cout << "\nTwo thirds of the average is: ";
	cout << twoThirds;
	
	cout << "\nThe first closest guess is: ";
	cout << closest;
	
	if (closest == entries[0]) {
		winner = "Player1";
	}
	else if (closest == entries[1]) {
		winner = "Player2";
	}
	else if (closest == entries[2]) {
		winner = "Player3";
	}
	
	cout << "\nCongratulations " << winner;
	
	return 0;
}

