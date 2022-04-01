#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main() {
    string userInput;

    cin >> userInput;

    for (int i = 0; i < userInput.length(); i++){
        if (isupper(userInput[i])){
            userInput[i] = tolower(userInput[i]);
        }
        else if (islower(userInput[i])){
            userInput[i] = toupper(userInput[i]);
        }
    }

    cout << userInput;

	return 0;
}