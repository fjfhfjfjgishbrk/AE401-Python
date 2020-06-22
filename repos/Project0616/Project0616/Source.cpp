#include<iostream>
using namespace std;

/*
int main() {
	int a;
	int b[16] = {0};
	cin >> a;
	int i = 0;
	while (a > 0) {
		b[i++] = a % 2;
		a = a / 2;
	}
	for (--i; i >= 0; i--) {
		cout << b[i];
	}
	return 0;
}
*/

int main() {
	char a[16] = {""};
	cin >> a;
	int b = 1;
	int sum = 0;
	for (int i = strlen(a) - 1; i >= 0; i--) {
		sum += b * ((int) a[i] - 48);
		b *= 2;
	}
	cout << sum;
	return 0;
}