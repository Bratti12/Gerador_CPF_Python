<?php

$dsn = 'mysql:host=localhost;dbname=example_db';
$username = 'root';
$password = 'password';

try {
    $pdo = new PDO($dsn, $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Conexão falhou: ' . $e->getMessage());
}


function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}
function generateCsrfToken() {
    return bin2hex(random_bytes(32));
}


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $csrfToken = $_POST['csrf_token'] ?? '';
    $storedCsrfToken = $_SESSION['csrf_token'] ?? '';

    
    if (!hash_equals($storedCsrfToken, $csrfToken)) {
        die('Token CSRF inválido');
    }

   
    $name = sanitizeInput($_POST['name']);
    $email = filter_var($_POST['email'], FILTER_VALIDATE_EMAIL);
    $message = sanitizeInput($_POST['message']);

    if (!$email) {
        die('Email inválido');
    }

   
    $stmt = $pdo->prepare('INSERT INTO feedback (name, email, message) VALUES (:name, :email, :message)');
    $stmt->execute([
        ':name' => $name,
        ':email' => $email,
        ':message' => $message
    ]);

    echo 'Dados salvos com sucesso!';
}

session_start();
$_SESSION['csrf_token'] = generateCsrfToken();
$csrfToken = $_SESSION['csrf_token'];
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Formulário de Feedback</title>
</head>
<body>
    <form method="post" action="">
        <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($csrfToken); ?>">
        <label for="name">Nome:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="message">Mensagem:</label>
        <textarea id="message" name="message" required></textarea>
        <br>
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
