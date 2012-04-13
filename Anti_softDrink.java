package anti_softdrink;

import java.util.Scanner;

public class Anti_softDrink {

public static void main(String[] args) 
{
Scanner input = new Scanner(System.in);

System.out.println("***********************************************");
System.out.println(" ANTI-SOFT DRINKS CAMPAIGN");
System.out.println("***********************************************");
System.out.println(" This is a console program that predicts when a user will be diabetic.");
//Introduction by Danny

System.out.println("");

String name;
int soft_num;

//Takes User's name and welcomes User
System.out.print(" Please enter your name : ");
name = input.next();
System.out.println("");
System.out.println(" Welcome " + name.toUpperCase() + ", this is a basic Python program that predicts when u are liable to be diabetic.");

System.out.println("");

//diabetic test begins
System.out.print(" Please enter the number of times you take soft drinks in a week : ");
soft_num = input.nextInt();

if (soft_num >= 21 & soft_num <= 30 )
{

System.out.println(" Stop taking soft drinks or you will have yourself to blame once you are diagnosed with diabetis");

} else if(soft_num >= 11 & soft_num <= 20)
{

System.out.println(" You have to reduce it to less than 5 in a week or you will be diabetic in not less than 5 years");

} else if(soft_num >= 3 & soft_num <= 10)
{

System.out.println(" Please Reduce your intake of soft drinks or in 15 yrs you will be diabetic");

} else
{

System.out.println(" Thanks " + name + " , for taking my Anti-Soft drink advice.");

}

}
}