<!DOCTYPE html>
<html>
<head>
    <title>Email Confirmation</title>
    <style>
        body {
            background-color: #333333;
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }

        form {
            background-color: #555555;
            color: white;
            padding: 20px;
            border-radius: 5px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            margin-bottom: 10px;
        }

        .form-group label {
            text-align: left;
            margin-bottom: 5px;
        }

        input[type="email"] {
            padding: 5px;
            border-radius: 3px;
        }

        input[type="submit"] {
            padding: 8px 20px;
            background-color: #777777;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #999999;
        }
    </style>
</head>
<body>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $email = $_POST["email"];
        $confirmEmail = $_POST["confirm_email"];

        if ($email !== $confirmEmail) {
            echo "Emails do not match. Please try again.";
        } else {
            // Emails match, do further processing here
            echo "Email successfully confirmed!";
        }
    }
    ?>
    
    <form method="POST" action="<?php echo $_SERVER['PHP_SELF']; ?>">
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" required>
        </div>
        
        <div class="form-group">
            <label for="confirm_email">Confirm Email:</label>
            <input type="email" name="confirm_email" id="confirm_email" required>
        </div>
        
        <input type="submit" value="Submit">
    </form>
</body>
</html>




<!-- <html>
    <head>
        @if ($title)
                <title>{{ $title }}</title>
        @else
                <title>Example Laravel App</title>
        @endif
    </head>
    <body>
        <div><a href="/home">Home</a> | <a href="/about">About</a>
        <hr/>
        <div class="container">
            @yield('content')
        </div>
    </body>
</html> -->
    