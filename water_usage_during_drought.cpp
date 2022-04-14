# include<iostream>

using namespace std;
void main()
{
       int sum=0, quarter ; float avg;
       cout<<"please enter your water bill for quarter 1  :";
       cin>>quarter;
       sum=sum+quarter;
       cout<<"please enter your water bill for quarter 2  :";
       cin>>quarter;
       sum=sum+quarter;
       cout<<"please enter your water bill for quarter 3  :";
       cin>>quarter;
       sum=sum+quarter;
       cout<<"please enter your water bill for quarter 4  :";
       cin>>quarter;
       sum=sum+quarter;
       avg=float(sum)/4;
       cout<<"your average monthly bill is "<<avg<<"$.";
       if(avg>75)
               cout<<"you are using excessive amounts of water."<<endl;
       else if(avg>=25 && avg <75)
               cout<<"you use a typical amount of water"<<"\n";
       else
               cout<<"Good you use a very small amount of water.\n Thanks for saving water.";

system("pause");
}
