#include<iostream>

#include<iomanip>

#include<fstream>

#include<cstdlib>

#include<string>

#define MAX 100 // Maximum number or records in file

using namespace std;

class Catastrophe

{

string name;

string disaster;

int year;

double propertyLoss;

int death;

public:

Catastrophe();

Catastrophe(string, string, int, int, int);

void readFile(Catastrophe [], int &);

void show(Catastrophe [], int);

void yearRange(Catastrophe [], int);

void lookUpDisaster(Catastrophe [], int);

};

Catastrophe::Catastrophe()

{

name = disaster = "";

year = propertyLoss = death = 0;

}

// Function to read file contents and stores it in array of object

// Returns number of number read from file &len call by reference

void Catastrophe::readFile(Catastrophe ca[], int &len)

{

string name;

string disaster;

int year;

double propertyLoss;

int death;

char symbol;

// ifstream objects declared to read data from files

ifstream fRead;

// Opens the file for reading

fRead.open("catastrophe.txt");

// Checks if the file unable to open for reading display's error message and stop

if(!fRead)

{

cout<<"\n Unable to open the file!";

exit(0);

}// End of if condition

// Loops till end of the file

while(!fRead.eof())

{

getline(fRead, ca[len].name, ',');

getline(fRead, ca[len].disaster, ',');

fRead>>ca[len].year;

fRead>>symbol;

fRead>>ca[len].propertyLoss;

fRead>>symbol;

fRead>>ca[len].death;

// Increase the record counter by one

len++;

}// End of while loop

// Close the file

fRead.close();

}// End of function

// Function to display complete information

void Catastrophe::show(Catastrophe ca[], int len)

{

cout<<"\n\n ***************** Catastrophe Information ***************** ";

// Loops till number of records

for(int c = 0; c < len; c++)

cout<<"\n\n Name: "<<ca[c].name<<"\n Disaster: "<<ca[c].disaster

<<"\n Year: "<<ca[c].year<<"\n Property Loss: $"<<ca[c].propertyLoss

<<"\n Death: "<<ca[c].death;

}// End of function

// Function to display disaster name between user entered year range

void Catastrophe::yearRange(Catastrophe ca[], int len)

{

int beginning, ending;

// Accepts beginning and ending year

cout<<"\n Enter beginning year: ";

cin>>beginning;

cout<<"\n Enter ending year: ";

cin>>ending;

cout<<"\n\n ***************** Year Range("<<beginning<<" - "<<ending<<") ***************** ";

// Loops till number of records

for(int c = 0; c < len; c++)

// Checks is current object year is greater then the beginning and less then ending

if(ca[c].year >= beginning && ca[c].year <= ending)

// Display name stored in current object

cout<<ca[c].name;

}// End of function

void Catastrophe::lookUpDisaster(Catastrophe ca[], int len)

{

string disasterName;

// To store the years

int years[len];

// years counter

int d = 0;

// Accepts disaster name

cout<<"\n Enter an disaster name: ";

cin>>disasterName;

cout<<"\n\n ***************** Disaster type: "<<disasterName<<" ***************** \n";

// Loops till number of records

for(int c = 0; c < len; c++)

{

// Checks if current object disaster name is equals to user entered disaster name

if(ca[c].disaster.compare(disasterName) == 0)

{

// To store found status for the year initial -1 for not found

int found = -1;

// To get unique year

// Loops till number of years stored

for(int e = 0; e < d; e++)

{

// Checks if current index position year is equals to

// current object year

if(years[e] == ca[c].year)

{

// Update the found status as found

found = e;

// Come out of the loop

break;

}// End of inner if condition

}// End of inner for loop

// Checks if found status is -1 then unique year

if(found == -1)

// Assigns the current object year to years array d index position

// Increase the index counter by one

years[d++] = ca[c].year;

}// End of outer if condition

}// End of outer for loop

cout<<"\n\n Years when disaster happened are: ";

// Loops till number of unique years stored

for(int e = 0; e < d; e++)

// Displays each year

cout<<years[e]<<", ";

}// End of function

// Function to display menu, accept user choice and return user choice

int menu()

{

int ch;

// Displays menu

cout<<"\n\n What would you like to do?";

cout<<"\n 1: Loop up year range.";

cout<<"\n 2: Loop up disaster.";

cout<<"\n 3: Display all disasters.";

cout<<"\n 4: Exit.";

// Accepts user choice

cout<<"\n Select an option: ";

cin>>ch;

// Returns user choice

return ch;

}// End of function

// main function definition

int main()

{

// Creates an array of size MAX to store numbers

// Len to store length of the array

Catastrophe ca[MAX];

int len = 0;

// Calls the function to read the file for insertion sort

ca[0].readFile(ca, len);

// Loops till user choice is not 4

do

{

// Calls the function to accept user choice

// checks the user choice and calls the appropriate function

switch(menu())

{

case 1:

ca[0].yearRange(ca, len);

break;

case 2:

ca[0].lookUpDisaster(ca, len);

break;

case 3:

ca[0].show(ca, len);

break;

case 4:

exit(0);

default:

cout<<"\n Invalid choice!!";

}// End of switch case

}while(1);// End of do while loop

return 0;

}// End of main function
