import 'dart:io'; // Import dart:io library to use stdin

void main() {
  // Prompt the user for a number
  print("Please enter a number:");

  // Read user input from the console
  String? userInput = stdin.readLineSync();

  // Check if user input is not null and is a valid number
  if (userInput != null && isNumeric(userInput)) {
    // Convert the user input to an integer
    int number = int.parse(userInput);

    // Print message based on the number entered
    if (number > 10) {
      print("Your number is greater than 10");
    } else if (number < 10) {
      print("Your number is less than 10");
    } else {
      print("Your number is equal to 10");
    }
  } else {
    // Inform the user if input is invalid
    print("Invalid input. Please enter a valid number.");
  }
}

// Function to check if a string is numeric
bool isNumeric(String s) {
  return double.tryParse(s) != null;
}
