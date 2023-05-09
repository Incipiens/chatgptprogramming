#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_LENGTH 32 // Maximum password length

char* generate_password(int length);

int main()
{
    srand(time(NULL)); // Seed the random number generator
    
    char* password = generate_password(MAX_LENGTH);
    
    printf("Generated password: %s\n", password);
    
    free(password);
    
    return 0;
}

char* generate_password(int length)
{
    char* password = malloc(sizeof(char) * (length + 1)); // Allocate memory for password string
    
    if (password == NULL) // Check for allocation errors
    {
        fprintf(stderr, "Error: Failed to allocate memory for password.\n");
        exit(1);
    }
    
    const char* allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-="; // Define allowed characters
    
    for (int i = 0; i < length; i++) // Generate password character by character
    {
        int rand_index = rand() % strlen(allowed_chars); // Generate random index
        password[i] = allowed_chars[rand_index]; // Add character to password string
    }
    
    password[length] = '\0'; // Add null terminator to end of password string
    
    return password;
}
