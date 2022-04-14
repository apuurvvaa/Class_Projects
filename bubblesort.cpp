#include <iostream>

using namespace std;

void print(int *arr, int size) {
    int i;
    for (i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void bubbleSort(int *arr, int size) {
    int i, j, temp;
    for (i = 0; i < size; ++i) {
        for (j = 0; j < size - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[7], size = 7;
    for (int i = 0; i < size; ++i) {
        cout << "Enter " << i+1 << " number :- ";
        cin >> arr[i];
    }
    cout << "Numbers Before Bubble Sort:- ";
    print(arr, size);
    bubbleSort(arr, size);
    cout << "Numbers after Bubble Sort:- ";
    print(arr, size);
    return 0;
}
