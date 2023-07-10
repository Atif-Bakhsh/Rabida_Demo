<?php
// Language file selection
$languageFile = 'en.php'; // Default language file

// Check if the language toggle button is clicked
if (isset($_POST['toggle'])) {
    $languageFile = ($_POST['language'] === 'en') ? 'en.php' : 'ar.php';
}

// Get the language array from the selected language file
$language = require_once($languageFile);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <meta charset="UTF-8">
    <style>
        body {
            direction: <?php echo ($languageFile === 'ar.php') ? 'rtl' : 'ltr'; ?>;
            text-align: <?php echo ($languageFile === 'ar.php') ? 'right' : 'left'; ?>;
        }

        form {
            text-align: <?php echo ($languageFile === 'ar.php') ? 'right' : 'left'; ?>;
        }

        .rtl {
            direction: rtl;
            text-align: right;
        }
    </style>
</head>
<body>
    <h2><?php echo $language['LoginTitle']; ?></h2>

    <form>
        <label for="username" class="<?php if ($languageFile === 'ar.php') echo 'rtl'; ?>"><?php echo $language['Box1']; ?>:</label>
        <input type="text" name="username" id="username" required><br><br>

        <label for="password" class="<?php if ($languageFile === 'ar.php') echo 'rtl'; ?>"><?php echo $language['Box2']; ?>:</label>
        <input type="password" name="password" id="password" required><br><br>

        <input type="submit" value="<?php echo $language['Submit']; ?>">
    </form>

    <form method="POST" action="<?php echo $_SERVER['PHP_SELF']; ?>">
        <input type="hidden" name="language" value="<?php echo ($languageFile === 'en.php') ? 'ar' : 'en'; ?>">
        <input type="submit" name="toggle" value="<?php echo ($languageFile === 'en.php') ? 'Switch to ar' : 'التبديل إلى اللغة الإنجليزية'; ?>">
    </form>
</body>
</html>

