#include <iostream>
#include <string>

using namespace std;

int arr[10001];

int main() {
	int T;
	cin >> T;

	arr[1] = 1;
	arr[2] = 2;

	for (int i = 3; i <= T; i++) {
		arr[i] = arr[i - 1] % 10007 + arr[i - 2] % 10007;
	}

	cout << arr[T] % 10007;
}