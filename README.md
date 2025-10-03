# Login System (Python)

[EN] This is a module that implements a basic console authentication system with a limited number of attempts. It can be easily integrated as part of a larger project or used as a practice exercise.

## How it works:

The program prompts the user to enter a username and password. Before validation, it checks that neither field is empty. If an empty field is detected, the system displays a warning message without counting it as an attempt.

If both fields contain information, the entered credentials are verified. If they do not match, an error is displayed along with the number of remaining login attempts. Once the maximum number of attempts is reached, access is blocked.

## Default configuration:

**Registered username**: `admin`  
**Registered password**: `1234`  
**Maximum attempts**: `3`

## License:

This project is licensed under the [MIT License](LICENSE).
