#include<iostream>
#define size 3
using namespace std;


void aa(int a[][size], int b[][size]) {
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			cout << a[i][j] + b[i][j] << " ";
		}
		cout << endl;
	}
}

void ab(int a[][size], int b[][size]) {
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			cout << a[i][j] - b[i][j] << " ";
		}
		cout << endl;
	}
}

void ac(int a[][size], int b[][size]) {
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			cout << a[i][j] * b[i][j] << " ";
		}
		cout << endl;
	}
}

void ad(int a[][size], int b[][size]) {
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			cout << a[i][j] / b[i][j] << " ";
		}
		cout << endl;
	}
}


int main() {
	int a[size][size] = { 0 };
	int b[size][size] = { 0 };
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			cin >> a[i][j];
		}
	}
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			cin >> b[i][j];
		}
	}
	cout << "Afhjwgerihfbwrijefbkj";
	int c;
	while (true) {
		cin >> c;
		bool d = false;
		switch (c)
		{
		case 1:
			aa(a, b);
			break;
		case 2:
			ab(a, b);
			break;
		case 3:
			ac(a, b);
			break;
		case 4:
			ad(a, b);
			break;
		default:
			d = true;
			break;
		}
		if (d) {
			break;
		}
	}
	return 0;
}

